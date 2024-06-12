from typing import List, Dict
from house import House


class Bidder:
    InstanceCount = 0
    def __init__(self, max_invest_per_house: List[float], name: str | None = None) -> None:
        Bidder.InstanceCount += 1
        self.max_invest_per_house = max_invest_per_house
        self.id = Bidder.InstanceCount
        self.name = name if name else f'Bidder #{self.id}'
        self.purchased: House | None = None
        self.allowed_to_bid = True

    @staticmethod
    def ArrangeBidderInstances(max_invest_per_house_matrix: List[List[float]]):
        number_of_bidders: float
        try:
            number_of_bidders = len(max_invest_per_house_matrix[0])
        except:
            raise ValueError('Invalid invest per house matrix provided.')
        return [Bidder([row[j] for row in max_invest_per_house_matrix]) for j in range(number_of_bidders)]

    @property
    def locked(self):
        if self.purchased:
            return True
        if not self.allowed_to_bid:
            self.allowed_to_bid = True
            return True
        return False
    
    def lock(self):
        self.allowed_to_bid = False
    
    def unlock(self):
        self.allowed_to_bid = True



class Bid:
    def __init__(self, item: House, bidder: Bidder, max_investment: float) -> None:
        self.item: House = item
        self.max_investment = max_investment
        self.suggested_price = self.item.min_price
        self.profit = self.max_investment - self.suggested_price
        self.bidder: Bidder = bidder
        self.lose_count: int = 0
        self.failed: bool = False

    def raise_price(self, how_much: float) -> None:
        self.suggested_price += how_much
        self.profit = self.max_investment - self.suggested_price

    def win(self):
        self.item.sold_to = self.bidder
        self.bidder.purchased = self.item
        self.temp_win()
        
    def temp_win(self):
        self.item.best_bid = self
        self.bidder.lock()
        self.lose_count = 0
        
    def lose(self):
        self.lose_count += 1
        if self.lose_count >= 2:
            self.failed = True