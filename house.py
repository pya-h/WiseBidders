from typing import List


class House:
    InstanceCount = 0

    def __init__(self, min_price: float, name: str | None = None) -> None:
        House.InstanceCount += 1
        self.min_price = min_price
        self.id = House.InstanceCount
        self.name = name if name else f'House #{self.id}'

    @staticmethod
    def ArrangeHouseInstances(min_prices: List[float]):
        return [House(price) for price in min_prices]
