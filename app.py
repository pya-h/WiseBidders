from house import House
from bid import Bidder
from typing import List
from auction import Auction


def get_user_inputs():
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
    return number_of_houses, number_of_bidders, V, r, epsilon

def get_test_input():
    V = [ [20, 30, 50],
         [10, 50, 40,],
         [30, 10, 90,],
    ]

    r = [20, 10, 15,]
    epsilon = 1

    return None, None, V, r, epsilon


if __name__ == '__main__':
    number_of_houses, number_of_bidders, V, r, epsilon = get_test_input()  # Todo: get_user_inputs()
    # preprocess data
    houses: List[House] = House.ArrangeHouseInstances(r)
    bidders: List[Bidder] = Bidder.ArrangeBidderInstances(V)

    # create auction
    auction = Auction(items=houses, bidders=bidders, min_raise_amount=epsilon, rounds_limit=100)
    auction.start()
    input()
