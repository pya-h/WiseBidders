from house import House
from bid import Bidder
from typing import List

if __name__ == '__main__':
    # getting inputs
    number_of_houses = int(input('n = '))
    number_of_bidders = int(input('m = '))

    V = []
    print(f'Enter the V({number_of_houses}x{number_of_bidders}) matrix indicating the maximum profit each bidder can put on a house:')
    print('V = [')
    for i in range(number_of_houses):
        row = input('\t')
        V.append([float(x) for x in row.split()])
    print(']\nNow enter vector r indicating the minimum price for each house:')
    print('r = [')
    r = [float(x) for x in input('\t').split()]
    print(']')
    eps = float(input('Epsilon = '))

    # preprocess data
    houses: list[House] = House.ArrangeHouseInstances(r)
    bidders: List[Bidder] = Bidder.ArrangeBidderInstances(V)

    for house in houses:
        print(house.min_price, end='\t')

    print()

    for bidder in bidders:
        print(bidder.max_invest_per_house, end='\t')

