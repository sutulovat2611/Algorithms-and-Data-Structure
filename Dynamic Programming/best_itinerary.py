""" 
__author__ = "Tatiana Sutulova"
date: 15/4/2021
"""

def best_itinerary(profit, quarantine_time, home):
    """ 
    Input: 
        - profit is a list of lists. All interior lists are length n. Each interior list represents a different day. 
        profit[d][c] is the profit that the salesperson will make by working in city c on day d.
        - quarantime_time is a list of non-negative integers. quarantime_time[i] is the number of days city i requires visitors to quarantine before they can work there.
        - home is an integer between 0 and n-1 inclusive, which represents the city that the salesperson starts in. They can start working in this city without needing to quarantine on the first day. 
          If they leave and come back later, they will need to quarantine.
    Output:
        - integer, which is the maximum amount of money that can be earned by the salesperson.
    Short description: The following function builds up the memoization tables based on the comparison, which is the most profitable case for the current day: stay and work at the same city, 
                       go to the city from the side if there is any, quarantine and work there or travel through cities till reaching the most profitable case. 
    Time complexity: O(nd) space,  where n is the number of cities, and d is the number of days 
    Space complexity: O(nd) space,  where n is the number of cities, and d is the number of days
    """
    #memo1 is the two dimensional matrix, which will be filled with the maximum profit on the current_day at the current_city when the salesman is ready to work 
    memo1=[[0 for i in range(len(profit[0]))] for j in range(len(profit))]
    #memo2 is the two dimensional matrix, which will be filled with the maximum profit on the current_day at the current_city when the salesman is just arrive and still needs to quarantine 
    memo2=[[0 for i in range(len(profit[0]))] for j in range(len(profit))]
    
    for i in range(len(profit)):
        current_day=len(profit)-i-1
        for current_city in range(len(profit[0])):
            # the last day 
            if current_day==len(profit)-1:
                memo1[current_day][current_city]=profit[current_day][current_city] #the best option is to work on that day, not travel or quarantine. 
                if current_day+quarantine_time[current_city]<len(profit):
                    memo2[current_day][current_city]=memo1[current_day+quarantine_time[current_city]][current_city]
            else:
                #if there is a city from the right
                if current_city+1<len(profit[0]):
                    # finding the maximum value for the current day at the current city by taking the max value from: if we travel to the city from the right and quarantine, if we stay and work at the same city travel to the next city and continue travelling 
                    if current_day+1+quarantine_time[current_city+1]<len(profit):
                        memo1[current_day][current_city]=max(memo2[current_day+1][current_city+1], profit[current_day][current_city]+memo1[current_day+1][current_city], memo1[current_day][current_city], memo1[current_day+1+quarantine_time[current_city+1]][current_city+1])
                    else:
                        memo1[current_day][current_city]=max(memo2[current_day+1][current_city+1], profit[current_day][current_city]+memo1[current_day+1][current_city], memo1[current_day][current_city])
                       
                    # checking whether the salesman is on quarantine or not
                    if current_day+quarantine_time[current_city]<len(profit):
                        #if not, then we get maximum from: the value that the salesman will earn at that day after quarantine, value that the salesman travels to the city from the right
                        memo2[current_day][current_city]=max(memo2[current_day+1][current_city+1], memo2[current_day][current_city], memo1[current_day+quarantine_time[current_city]][current_city])
                    else:
                        #if the salesman is on quarantine we get the value which will be earned if we travel to the right
                        memo2[current_day][current_city]=max(memo2[current_day+1][current_city+1],memo2[current_day][current_city])
                                       

                #if there is a city from the left
                if current_city-1>=0:
                    # finding the maximum value for the current day at the current city by taking the max value from: if we travel to the city from the left and quarantine, if we stay and work at the same city travel to the next city and continue travelling 
                    if current_day+1+quarantine_time[current_city-1]<len(profit):
                        memo1[current_day][current_city]=max(memo2[current_day+1][current_city-1], profit[current_day][current_city]+memo1[current_day+1][current_city], memo1[current_day][current_city], memo1[current_day+1+quarantine_time[current_city-1]][current_city-1])
                    else:
                        memo1[current_day][current_city]=max(memo2[current_day+1][current_city-1], profit[current_day][current_city]+memo1[current_day+1][current_city], memo1[current_day][current_city])
            
                    # checking whether the salesman is on quarantine or not
                    if current_day+quarantine_time[current_city]>=len(profit):
                            #if not, then we get maximum from: the value that the salesman will earn at that day after quarantine, value that the salesman travels to the city from the left
                            memo2[current_day][current_city]=max(memo2[current_day+1][current_city-1],memo2[current_day][current_city])
                    else: 
                            memo2[current_day][current_city]=max(memo2[current_day+1][current_city-1], memo2[current_day][current_city], memo1[current_day+quarantine_time[current_city]][current_city])
                
                #if there is no city from the right nor from the left we just work at the same city 
                if not current_city+1<len(profit[0]) and not current_city-1>=0:
                    memo1[current_day][current_city]= memo1[current_day+1][current_city]+profit[current_day][current_city]
    return memo1[0][home]

  #test for task 2
  profit = [
      [6, 9, 7, 5, 9],
      [4, 7, 3, 10, 9],
      [7, 5, 4, 2, 8],
      [2, 7, 10, 9, 5],
      [2, 5, 2, 6, 1],
      [4, 9, 4, 10, 6],
      [2, 2, 4, 8, 7],
      [4, 10, 2, 7, 4]]
  quarantine = [3,1,1,1,1]
  print(best_itinerary(profit, quarantine, 2))
