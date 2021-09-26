"""
__author__ = "Tatiana Sutulova"
date: 29/5/2021
"""

import heapq
from decimal import *

class Graph:
    """A Graph object"""
    def __init__(self, prices):
        # initializing the graph
        self.prices = prices  # edges
        self.liquids = [None] * len(prices)
        for i in range(len(prices)):
            self.liquids[i] = Liquid(i, prices[i])


class Liquid:
    """Vertex of a graph"""
    def __init__(self, id, price):
        self.id = id
        self.price = price
        self.volume = float("-Inf")
        self.previous_volume = float("-Inf")


def best_trades(prices, starting_liquid, max_trades, townspeople):
    """
    Input:
        - prices: an array of length n, where prices[i] is the value of 1L of the liquid with ID i.
        - starting_liquid: the ID of the liquid you arrive with (initially 1 L of that liquid)
        - max_trades: maximum number of trades that can be made
        - townspeople: a list of non-empty lists [[(give, receive, ratio), (give, receive, ratio)], [(give, receive, ratio)]], where
            - each sublist represents the trades offered by one person
            - each trade consists of:
                - give: ID of the liquid that the person is giving out
                - receive: ID of the liquid that the person is receiving
                - ratio: exchange ratio ( how much of "receive" u can get for amount of 'give' that u have)
    Output:
        - the maximum value that is obtained after performing at most max_trades trades.
    Short description: gets the highest possible income from trading with townspeople in max_trades
    Time complexity: O(T*M) time
        - T is the total number of trades available
        - M is max_trades
    """
    g = Graph(prices)

    # initializing the start liquid
    g.liquids[starting_liquid].volume = 1
    g.liquids[starting_liquid].previous_volume = 1

    # initialize the current_max to the start liquid price
    current_max = g.liquids[starting_liquid].volume * g.prices[starting_liquid]

    #maximum max_trades of trades
    for i in range(max_trades):
        # reinitialize the previous volumes to the volumes obtained in the previous iterations
        for liquid in g.liquids:
            liquid.previous_volume = liquid.volume
        # in each person
        for person in townspeople:
            #each trade
            for trade in person:
                #check if the trade is more beneficial than the one made in previous iteration and than the ones in this
                # iteration, but before that particular one
                if trade[2] * g.liquids[trade[0]].previous_volume * g.prices[trade[1]] > g.liquids[ trade[1]].previous_volume * g.prices[trade[1]] \
                        and trade[2] * g.liquids[trade[0]].previous_volume * g.prices[trade[1]] > g.liquids[
                    trade[1]].volume * g.prices[trade[1]]:
                    g.liquids[trade[1]].volume = trade[2] * g.liquids[trade[0]].previous_volume
                    # reset the maximum profit that the user can get
                    if current_max < g.liquids[trade[1]].volume * g.prices[trade[1]]:
                        current_max = g.liquids[trade[1]].volume * g.prices[trade[1]]
    return round(Decimal(current_max))

