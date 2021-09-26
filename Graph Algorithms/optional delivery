"""
__author__ = "Tatiana Sutulova"
date: 29/5/2021
"""

import heapq
from decimal import *

class Graph:
    """A graph object"""

    def __init__(self, start_city, end_city, cities):
        self.cities = [None] * cities
        self.start_city = None
        self.end_city = None
        # seting up cities
        for i in range(cities):
            self.cities[i] = City(i)
            # set up start city
            if i == start_city:
                self.start_city = self.cities[i]
            if i == end_city:
                self.end_city = self.cities[i]

    def dijkstra(self, current_city, end_city):
        """
        Input:
            - current_city: the city to start with ( instance of the City class)
            - end_city: the city to arrive to( instance of the City class)
        Output:
            - tuple, that consists of :
                - the maximum possible profit travelling from current_city to end_city
                - list of all the cities travelled before reaching the end_city with the maximum profit
        Time complexity: O(Rlog(N)) where
            - R is the total number of roads
            - N is the total number of cities
        """
        current_city.set_discovered()
        # setting the route
        output = []
        discovered_cities = []
        heapq.heappush(discovered_cities, current_city)
        while len(discovered_cities) > 0:
            # heapify to make sure that the order is kept
            heapq.heapify(discovered_cities)
            current_city = heapq.heappop(discovered_cities)
            current_city.set_visited()  # setting the city to visited
            # end the loop when reaching the end city, looping back through the cities and getting the route which was
            # visited to get there
            if current_city == end_city:
                while current_city is not None:
                    output.append(current_city.id)
                    current_city = current_city.get_previous()
                break

            # check all the possible paths
            for road in current_city.roads:
                # setting up the money of the next city
                next_city = self.cities[road.end_city]
                temp_money = current_city.get_money() + road.travel_cost

                # if the vertix wasn't discovered yet, update the heap
                if not next_city.get_discovered():
                    next_city.set_discovered()  # resetting city to discovered
                    next_city.set_money(temp_money)
                    next_city.set_previous(current_city)
                    heapq.heappush(discovered_cities, next_city)
                else:
                    # if it was reset the money if the money is smaller
                    if next_city.get_money() > temp_money:
                        next_city.set_money(temp_money)
                        next_city.set_previous(current_city)
        return (end_city.get_money(), output[::-1])


class City:
    """Vertex of a graph"""

    def __init__(self, id):
        self.id = id

        self.discovered = False
        self.visited = False
        self.max_money = 0

        self.roads = []
        self.previous = None

    def __lt__(self, another_city):
        """Allows the comparison in heapq based on the money"""
        return self.get_money() < another_city.get_money()

    def __gt__(self, other):
        """Allows the comparison in heapq based in the money"""
        return other.__lt__(self)

    def set_discovered(self):
        """Sets up the following city as discovered"""
        self.discovered = True

    def set_visited(self):
        """Sets up the following city as visited"""
        self.visited = True

    def set_money(self, money):
        """Sets up the money that is received reaching following city"""
        self.max_money = money

    def set_previous(self, previous):
        """Set up the city that was visited before that city"""
        self.previous = previous

    def add_road(self, road):
        """Adds the edge  """
        self.roads.append(road)

    def get_money(self):
        """Get the money that is currently earned at that city"""
        return self.max_money

    def get_discovered(self):
        """ Checks whether the city is discovered"""
        return self.discovered

    def get_previous(self):
        """ Returns the city that was travelled previously"""
        return self.previous


class Road:
    """An edge of the graph"""

    def __init__(self, start_city, end_city, travel_cost):
        self.start_city = start_city  # from city, vertex
        self.end_city = end_city  # to city, vertex
        self.travel_cost = travel_cost  # cost


def opt_delivery(n, roads, start, end, delivery):
    """
    Input:
        - n: is the number of cities ([0..n-1])
        - roads: is a list of tuples (u,v,w):
           - Each tuple represents an road between cities u and v.
           - w: is the cost of traveling along that road, which is always non-negative. ( both ways)
        - start: the city to start with
        - end: the city to end with
        - delivery: is a tuple (pickup_city, delivery_city, money):
            - pickup_city:  the city where we can pick up the item
            - delivery_city: city where we can deliver the item
            - money: the amount of money we can make if we deliver the item from the pickup_city to the delivery_city.
    Output:
        - tuple, that consists of :
        - the maximum possible profit travelling from current_city to end_city
        - list of all the cities travelled before reaching the end_city with the maximum profit
    Time complexity: O(Rlog(N)) where
        - R is the total number of roads
        - N is the total number of cities
    """
    graph = Graph(start, end, n)
    # filling up the graph
    for i in range(len(roads)):
        graph.cities[roads[i][0]].add_road((Road(roads[i][0], roads[i][1], roads[i][2])))
        graph.cities[roads[i][1]].roads.append(Road(roads[i][1], roads[i][0], roads[i][2]))

    # from start to end
    start_to_end = graph.dijkstra(graph.start_city, graph.end_city)
    for city in graph.cities:  # resetting the graph
        city.discovered = False
        city.visited = False
        city.max_money = 0
        city.previous = None

    # from start to pick up
    start_to_pick_up = graph.dijkstra(graph.start_city, graph.cities[delivery[0]])
    for city in graph.cities:  # resetting the graph
        city.discovered = False
        city.visited = False
        city.max_money = 0
        city.previous = None

    # from pick up to delivery
    pick_up_to_delivery = graph.dijkstra(graph.cities[delivery[0]], graph.cities[delivery[1]])
    for city in graph.cities:  # resetting the graph
        city.discovered = False
        city.visited = False
        city.max_money = 0
        city.previous = None

    # from delivery to end
    delivery_to_end = graph.dijkstra(graph.cities[delivery[1]], graph.end_city)

    # calculating the total money with delivery
    with_delivery = start_to_pick_up[0] + pick_up_to_delivery[0] + delivery_to_end[0] - delivery[2]
    # compare money with delivery and without and return the smaller one
    if start_to_end[0] <= with_delivery:
        return start_to_end
    else:
        output = []
        for i in range(len(start_to_pick_up[1])):
            output.append(start_to_pick_up[1][i])

        for i in range(1, len(pick_up_to_delivery[1])):
            output.append(pick_up_to_delivery[1][i])

        for i in range(1, len(delivery_to_end[1])):
            output.append(delivery_to_end[1][i])
        return with_delivery, output
