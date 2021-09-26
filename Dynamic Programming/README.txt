1. best_schedule.py:
 General idea: 
   There are two means of earning money: main job and competition. In order to maximise the amount of money, it's possible combine the main job
   with participating in competitions. best_schedule(weekly_income, competitions) function is based on dynamic programming approach and it allows
   to find the maximum money that may be earned considering both main job and competition.

 1.1 Input
    - weekly_income is a list of non-negative integers, where weekly_income[i] is the amount of
      money to be earned in week i working at your main job.
    - competitions is a list of tuples, each representing a competition. Each tuple contains
      3 non-negative integers, (start_time, end_time, winnings).
    - start_time is the is the week that you will need to begin preparing for this competition (i.e.
      the first week that you cannot do your regular job, if you compete in this
      competition).
    - end_time is the last week that you will need to spend recovering from this competition (i.e.
      the last week that you cannot do your regular job, if you compete in this
      competition).
    - winnings is the amount of money you will win if you compete in this competition.
 1.2 Output
    - best_schedule returns an integer, which is the maximum amount of money that can be earned.
 1.3 Example
    regular_work = [3,7,2,1,8,4,5]
    special_events = [(1,3,15),(2,2,8),(0,4,30),(3,5,19)]
    print(best_events(regular_work, special_events))
    >>> 42
    In the above example, the optimal schedule is to work as at your main job in weeks 0 and 1 (earning
    3+7), then compete in the (2,2,8) event in week 2 (earning 8), then compete in the (3,5,19)
    event from weeks 3 to 5 (earning 19), then work as a trainer in week 6 (earning 5).
1.4 Complexity
    - Time: O(Nlog(N)) 
    - Space: O(N)
    - where N is the total number of elements in weekly_income and competitions put together.
    
    
2. best_itinerary.py:
 General idea: 
    There are cities along the coast that a salesperson may travel to. The salesperson may work there for one or more days.
    Moreover, each city requires travlers to quarantine if they are willing to stay there to work (quarantine time varies from city to city). 
    The salesperson has an idea of how much money they can make by working in each city, for
    each day. They need to decide which cities to travel to, and which cities to work in, in order
    to make the most money. Each day, the salesperson can either work for the day in their current city (assuming they have
    finished quarantine), or they can travel to either adjacent city. Traveling always takes 1 day,
    and since the cities are along a coast, each city has two adjacent cities, except for two cities on
    the ends of the coast, which only have 1.
    function best_itinerary(profit, quarantine_time, home) function is based on dynamic programming approach and it allows
    to find the maximum money that may be earned by a salesperson.
 1.1 Input
     - profit is a list of lists. All interior lists are length n. Each interior list represents a different
       day. profit[d][c] is the profit that the salesperson will make by working in city c on day d.
     - quarantime_time is a list of non-negative integers. quarantime_time[i] is the number of
       days city i requires visitors to quarantine before they can work there.
     - home is an integer between 0 and n-1 inclusive, which represents the city that the salesperson
       starts in. They can start working in this city without needing to quarantine on the first day.
       If they leave and come back later, they will need to quarantine.
 1.2 Output
    - best_itinerary returns an integer, which is the maximum amount of money that can be earned by the salesperson.
 1.3 Example
    profit = [
    [6, 9, 7, 5, 9]
    [4, 7, 3, 10, 9]
    [7, 5, 4, 2, 8]
    [2, 7, 10, 9, 5]
    [2, 5, 2, 6, 1]
    [4, 9, 4, 10, 6]
    [2, 2, 4, 8, 7]
    [4, 10, 2, 7, 4]]
    quarantine = [3,1,1,1,1]
    best_itinerary(profit, quarantine, 0)
    >>> 39
    best_itinerary(profit, quarantine, 1)
    >>> 54
1.4 Complexity
    - Time: O(nd)
    - Space: O(nd)
    - where n is the number of cities, and d is the number of days
