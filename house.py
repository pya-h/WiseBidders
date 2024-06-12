from typing import List


class House:
    InstanceCount = 0

    def __init__(self, min_price: float, name: str | None = None) -> None:
        House.InstanceCount += 1
        self.min_price: float = min_price
        self.id: int = House.InstanceCount
        self.name: str = name if name else f'House #{self.id}'
        self.sold_to = None  # bidder
        self.best_bid = None
        
    @staticmethod
    def ArrangeHouseInstances(min_prices: List[float]):
        return [House(price) for price in min_prices]

    @property
    def is_sold(self):
        return self.sold_to is not None