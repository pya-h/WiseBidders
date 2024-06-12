from house import House
from bid import Bidder, Bid
from typing import List, Dict


class Auction:

    def __init__(self, items: List[House], bidders: List[Bidder], min_raise_amount: float) -> None:
        self.bidders: List[Bidder] = bidders
        self.items: List[House] = items
        self.min_raise_amount: float = min_raise_amount

    def start(self):
        # pre-analyze bidders and houses
        bids: Dict[Bidder, List[Bid]] = {}

        for bidder in self.bidders:
            bids[bidder] = self.analyze(bidder)

        bids_per_item: Dict[House, List[Bid]] = {}

        for bidder in bids:
            for bid in bids[bidder]:
                if bid.item not in bids_per_item:
                    bids_per_item[bid.item] = []
                bids_per_item[bid.item].append(bid)

        # compare and analyze all possible bids on an item and select one, and etc.
        for item in self.items:
            item_bids = bids_per_item[item]
            # find best price and temp win
            
    def analyze(self, bidder: Bidder) -> List[Bid]:
        possible_bids = [Bid(house, bidder, bidder.max_invest_per_house[i]) for i, house in enumerate(self.houses)] 
        # sort bids by profit
        return sorted(possible_bids, key=lambda bid: bid.profit, reverse=True)
