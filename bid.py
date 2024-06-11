from typing import List, Dict
from house import House

class Bid:
    def __init__(self, item: House, max_investment: float) -> None:
        self.item: House = item
        self.max_investment = max_investment
        self.suggested_price = self.item.min_price
        self.profit = self.max_investment - self.suggested_price
    
    def raise_price(self, how_much: float) -> None:
        self.suggested_price += how_much
        self.profit = self.max_investment - self.suggested_price

class Bidder:
    InstanceCount = 0
    def __init__(self, max_invest_per_house: List[float], name: str | None = None) -> None:
        Bidder.InstanceCount += 1
        self.max_invest_per_house = max_invest_per_house
        self.id = Bidder.InstanceCount
        self.name = name if name else f'Bidder #{self.id}'
        self.possible_bids: List[Bid] = []

    def analyze(self, houses: List[House]):
        self.possible_bids = [Bid(house, self.max_invest_per_house[i]) for i, house in enumerate(houses)] 

    @staticmethod
    def ArrangeBidderInstances(max_invest_per_house_matrix: List[List[float]]):
        number_of_bidders: float
        try:
            number_of_bidders = len(max_invest_per_house_matrix[0])
        except:
            raise ValueError('Invalid invest per house matrix provided.')
        return [Bidder([row[j] for row in max_invest_per_house_matrix]) for j in range(number_of_bidders)]
