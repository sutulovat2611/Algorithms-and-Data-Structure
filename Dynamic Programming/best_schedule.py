""" 
__author__ = "Tatiana Sutulova"
date: 15/4/2021
"""

def best_schedule(weekly_income, competitions):
    """ 
    Input: 
        - weekly_income is a list of non-negative integers, where weekly_income[i] is the amount of money you will earn working as a personal trainer in week i.
        - competitions is a list of tuples, each representing a sporting competition. Each tuple contains 3 non-negative integers, (start_time, end_time, winnings):
                - start_time is the is the week that you will need to begin preparing for this competition (i.e. the first week that you cannot do your regular 
                job as a personal trainer, if you compete in this competition).
                - end_time is the last week that you will need to spend recovering from this competition (i.e. the last week that you cannot do your regular 
                job as a personal trainer, if you compete in this competition).
                - winnings is the amount of money you will win if you compete in this competition.
    Output:
        - integer, which is the maximum amount of money that can be earned.
    Short description: The following function merges both competition ond weekly_income arrays into the same array, where each element will be a tuple of (start_time, end_time, winnings),
                       each value is explained above. The merged array is sorted by the end_time ( the sorting algorihtm that was used is Merge Sort, which has the worst time complexity of NlogN
                       where N is the number of elements). After sorting the memoization table is created. It allows to store the total income earned day by day, so when 
                       we compare what is more beneficial at certain period of time: compete or be a personal training, we can refer back to the other days.
        
    Time complexity: O(Nlog(N)) time, where N  is the total number of elements in weekly_income and competitions put together.
    Space complexity:  O(N) space, where N is the total number of elements in weekly_income and competitions put together.
    """
    #making each element of weekly_income into tuples of form (start_day, end_day, income) and create a new array with these tuples
    weekly_income_tuples=len(weekly_income)*[0] 
    for i in range(len(weekly_income)):
        temp=(i,i,weekly_income[i])
        weekly_income_tuples[i]=temp
    #merge competitions and the weekly_income_tuples into one list
    merged_array=[]
    for i in competitions:
        merged_array.append(i)
    for i in weekly_income_tuples:
        merged_array.append(i)
    #sort that list with the merge sort algorithm (O(nlogn) worst case complexity, n is the total num of elements in the list)
    merge_sort(merged_array)
    #initiailze memo
    memo=[0]*(len(weekly_income)+1)
    #loop through each element in the merged array
    for i in range(len(merged_array)):
        if i==0:
            memo[i+1]=merged_array[i][2]
        else:

            if memo[merged_array[i][1]+1]<=memo[merged_array[i][0]]+merged_array[i][2]:
                memo[merged_array[i][1]+1]=memo[merged_array[i][0]]+merged_array[i][2]
    return memo[len(memo)-1]

def merge_sort(arr):
    """ 
    Input: 
        - arr is an array, which is to be sorted
    Output:
        - this is the void function, meaning it has no output, however the input array will be changed (sorted) after this function finishes running
    Short description: The following function is the Merge Sort algorithm, which works as following:
                       1) Divide the unsorted list into n sublists, each containing one element (a list of one element is considered sorted). 
                       2) Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining
    Time complexity: O(Nlog(N)) time, where N  is the total number of elements in arr
    Space complexity:  O(N) space, where N is the total number of elements in arr
    """
    if len(arr) > 1:
         # finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements into 2 halves
        left = arr[:mid]
        right = arr[mid:]
        # Sorting the first half
        merge_sort(left)
        # Sorting the second half
        merge_sort(right)
        i = j = k = 0
        # upload data to temporary arrays left and right
        while i < len(left) and j < len(right):
            if left[i][1] < right[j][1]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        # Checking if any element was left out
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            

#test for task 1
regular_work = [3,7,2,1,8,4,5]
special_events = [(1,3,15),(2,2,8),(0,4,30),(3,5,19)]
print(best_schedule(regular_work, special_events))
