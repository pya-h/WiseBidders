from typing import List
from house import House


class Bidder:
    InstanceCount = 0
    def __init__(self, max_invest_per_house: List[float], name: str | None = None) -> None:
        Bidder.InstanceCount += 1
        self.max_invest_per_house = max_invest_per_house
        self.id = Bidder.InstanceCount
        self.name = name if name else f'Bidder #{self.id}'
        self.profit_per_house: List[float] = []
        self.targets: List[House] = []

    def organize_targets(self, houses: List[House]):
        pass

    @staticmethod
    def ArrangeBidderInstances(max_invest_per_house_matrix: List[List[float]]):
        number_of_bidders: float
        try:
            number_of_bidders = len(max_invest_per_house_matrix[0])
        except:
            raise ValueError('Invalid invest per house matrix provided.')
        return [Bidder([row[j] for row in max_invest_per_house_matrix]) for j in range(number_of_bidders)]
