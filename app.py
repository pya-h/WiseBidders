from house import House
from bid import Bidder
from typing import List
from auction import Auction


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
    epsilon = float(input('Epsilon = '))

    # preprocess data
    houses: List[House] = House.ArrangeHouseInstances(r)
    bidders: List[Bidder] = Bidder.ArrangeBidderInstances(V)

    # create auction
    auction = Auction(items=houses, bidders=bidders, min_raise_amount=epsilon)
    auction.start()