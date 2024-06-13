from house import House
from bid import Bidder, Bid
from typing import List, Dict
from random import randint

class Auction:

    def __init__(self, items: List[House], bidders: List[Bidder], min_raise_amount: float, rounds_limit: int) -> None:
        self.bidders: List[Bidder] = bidders
        self.items: List[House] = items
        self.min_raise_amount: float = min_raise_amount
        self.rounds_limit: int = rounds_limit

    def start(self):
        # pre-analyze bidders and houses
        bids_per_bidder: Dict[Bidder, List[Bid]] = {}

        for bidder in self.bidders:
            bids_per_bidder[bidder] = self.analyze(bidder)
            Auction.randomize_first_bid_by_profit_if_needed(bids_per_bidder[bidder])

        bids_per_item: Dict[House, List[Bid]] = {}

        for bidder in bids_per_bidder:
            for bid in bids_per_bidder[bidder]:
                if bid.item not in bids_per_item:
                    bids_per_item[bid.item] = []
                bids_per_item[bid.item].append(bid)

        # # do first bid for all items
        for item in bids_per_item:
            bids_per_item[item] = self.accept_best_bid(bids_per_item[item], creterion=lambda bid: bid.profit, randomize_if_needed=False)

        # start raising, comapring and re-analyzing and etc.
        round: int = 2
        number_of_raises: int = 1
        close_countdown = 3
        while close_countdown > 0 and (round < self.rounds_limit) and bids_per_item:
            number_of_raises = 0
            print("Round", round, ":")
            # first bidders must perform raise on their best bid
            bids_per_item = {}
            for bidder in bids_per_bidder:
                if bids_per_bidder[bidder]:
                    bid = bids_per_bidder[bidder][0]
                    next_price = bid.item.best_bid.suggested_price + self.min_raise_amount
                    if bid != bid.item.best_bid:
                        if bid.can_raise(next_price):
                            number_of_raises += 1
                            close_countdown = 3
                            bid.raise_price(next_price)
                        else:
                            bid.lose()

                    if not bid.failed:
                        if bid.item not in bids_per_item:
                            bids_per_item[bid.item] = []
                        bids_per_item[bid.item].append(bid)
                    else:
                        del bids_per_bidder[bidder][0]
                        if bids_per_bidder[bidder][0]:
                            Auction.randomize_first_bid_by_profit_if_needed(bids_per_bidder[bidder])

            for item in bids_per_item:
                print("\tBid on", item, ":")
                item_bids = bids_per_item[item]
                for bid in item_bids:
                    print("\t\t", bid)
                bids_per_item[item] = self.accept_best_bid(item_bids)
                print(f"\t{item} for {item.best_bid.suggested_price} to {item.best_bid.bidder}")

            round += 1
            if not number_of_raises:
                close_countdown -= 1

        print('Finally:')
        self.declare_winners()
        for item in self.items:
            print(item, "Sold to", item.sold_to, "@ ", item.best_bid.suggested_price if item.best_bid and item.sold_to else None)

    def accept_best_bid(self, item_bids: List[Bid], creterion = lambda bid: bid.suggested_price, randomize_if_needed: bool = True) -> List[Bid]:
        item_bids = sorted(item_bids, key=creterion, reverse=True)
        if randomize_if_needed:
            Auction.randomize_first_bid_by_price_if_needed(item_bids)
        if item_bids:
            item_bids[0].temp_win()
        return item_bids

    @staticmethod
    def randomize_first_bid_by_price_if_needed(bids: List[Bid]):
        if len(bids) <= 1:
            return
        i, end = 1, len(bids)
        while i < end and (bids[0].suggested_price == bids[i].suggested_price):
            i += 1
        if i > 1:
            choice = randint(0, i - 1)
            temp = bids[0]
            bids[0] = bids[choice]
            bids[choice] = temp

    @staticmethod
    def randomize_first_bid_by_profit_if_needed(bids: List[Bid]):
        if len(bids) <= 1:
            return
        i, end = 1, len(bids)
        while i < end and (bids[0].profit == bids[i].profit):
            i += 1
        if i > 1:
            choice = randint(0, i - 1)
            temp = bids[0]
            bids[0] = bids[choice]
            bids[choice] = temp


    def declare_winners(self):
        for item in self.items:
            if item.best_bid is not None:
                item.best_bid.win()

    def analyze(self, bidder: Bidder) -> List[Bid]:
        possible_bids = [Bid(house, bidder, bidder.max_invest_per_house[i]) for i, house in enumerate(self.items)]
        # sort bids by profit
        possible_bids = list(filter(lambda bid: not bid.failed, possible_bids))
        return sorted(possible_bids, key=lambda bid: bid.profit, reverse=True)
