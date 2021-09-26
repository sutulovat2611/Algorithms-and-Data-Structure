1. liquid_trading.py:
 General idea: 
    Software that allows trading items at different ratio and maximise the amount of an item you have.
    You are only in the town for a limited time, and trading takes time, so you have a maximum
    number of trades you can conduct before you need to move on, though you may choose to trade
    fewer times than this maximum. You also only have one container (with unlimited capacity!),
    and you cannot mix liquids or they will become worthless, so you must trade all of your current
    liquid whenever you make a trade.
    best_trades(prices, starting_liquid, max_trades, townspeople) function is based in dijkstra algorithm and it allows to find 
    the maximum value that you can obtain after performing at most max_trades trades.
 1.1 Input
      Liquids each have an ID. There are n liquids, and each one has a unique ID from the range
      [0..n-1].
      - prices is an array of length n, where prices[i] is the value of 1L of the liquid with ID i.
      - starting_liquid is the ID of the liquid you arrive with. You always start with 1L of this liquid.
      - townspeople is a list of non-empty lists. Each interior list corresponds to the trades offered
        by a particular person. The interior lists contain 3 element tuples, (give, receive, ratio).
        - give is an id of the liquid you are willing to give
        - receive is an id of the liquid you are willing to receive
        - ratio is the ratio between the amount of liquid u will give and receive ( give -> ratio * receive) 
      For each liquid, there will be at least one townsperson who is willing to trade for that liquid.
    
 1.2 Output
     - best_trades should return the maximum value that you can obtain after performing at most max_trades trades.
 1.3 Example
      starting_liquid = 0
      max_trades = 6
      townspeople = [[(0,1,4),(2,3,30)],[(1,2,2.5),(2,0,0.2)]]
      best_trades(prices, starting_liquid, max_trades, townspeople)
      >>>60
      max_trades = 2
      best_trades(prices, starting_liquid, max_trades, townspeople)
      >>>20
1.4 Complexity
    - O(TM), where 
    - T is the total number of trades available
    - M is max_trades
    
2. optional_delivery.py:
 General idea: 
    Software that allows to travel from on city to another, while traveling is costly. We want to get
    to our destination as cheaply as possible. However, there is a way we can make some money on
    our way. We can pick up an item from one particular city, and deliver it to another particular
    city. We want to determine whether it will be cheaper to perform this delivery during our
    journey, or just go directly to our destination.
    A function opt_delivery(n, roads, start, end, delivery) is designed in order to find the cost of travelling and the cities we
    have to travel to in order to get the most money
 2.1 Input
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
 2.2 Output
    - tuple, that consists of :
         - the maximum possible profit travelling from current_city to end_city
         - list of all the cities travelled before reaching the end_city with the maximum profit
 2.3 Example
    n = 4
    roads = [(0,1,3),(0,2,5),(2,3,7),(1,3,20)]
    start = 0
    end = 1
    delivery = (2,3,25)
    profit = 25
    opt_delivery(n, roads, start, end, delivery)
    >>> (2, [0,2,3,2,0,1])
    delivery = (2,3,20)
    opt_delivery(n, roads, start, end, delivery)
    >>> (3, [0,1])
    delivery = (2,3,100)
    opt_delivery(n, roads, start, end, delivery)
    >>>(-73, [0,2,3,2,0,1])
2.4 Complexity
    Time complexity: O(Rlog(N)) where
        - R is the total number of roads
        - N is the total number of cities
