""" 
__author__ = "Tatiana Sutulova"
date: 21/3/2021
"""

#%% Task 1 
def best_interval(transactions, t):
    """ 
    Input: 
        - transactions is a unsorted list of non-negative integers, '
        - t is a non-negative integer, representing a length of time in seconds.
    Output:
        tuple of (best_t, count):
            - best_t is the time such that the interval starting at best_t and ending at best_t + t contains more elements from transactions
            than any other interval of length t.
            - count is the number of elements in the interval of length t starting at best_t.
    Time complexity: O(nk), where n is the number of elements in the transactions list and k is the number of digits in the greatest element
    """
    if len(transactions)==0:
        return (0,0)
    #sorting the transaction array in increasing order using radix sort
    radix_sort_stable_int(transactions)
    # print(transactions)
    #finding the first interval in the array 
    k=0
    for i in range(len(transactions)-1):
        if i+1==len(transactions):
            break 
        else:
            if (transactions[0]+t)<transactions[i+1]:
                break
        k+=1
    #setting up pointers
    j=k #setting j at the last element of the first interval 
    i=0 #setting pointer i at the first element of the array 
    best_t=transactions[j]-t
    max_counter=k+1  # represents the number of elements in the interval with the maximum number of elements
    current_counter=k+1  #represents the number of elements in the interval [transaction[i], transaction[j]]
    #loop ends when j reaches the second last element of transactions array 
    while j<len(transactions)-1:
        i+=1
        current_counter-=1
        while transactions[j+1]<=transactions[i]+t:
            j+=1
            current_counter+=1
            if j==len(transactions)-1:
                break
        #comparing if the current interval is greater than tha greatest of the previous ones
        if max_counter<current_counter:
            max_counter=current_counter
            if j==len(transactions):
                best_t=transactions[j]-t-1
            else:
                best_t=transactions[j]-t 
    if best_t<0:
        best_t=0
    return (best_t, max_counter)

def sort_counting_stable_col_int(new_list,col):
    """ 
    Input: 
        new_list is an unsorted list of non-negative integers, 
        col is an integer which defines which column in the integer will the list be sorted according to.
    Output:
        new_list the array sorted based on col.
    Time complexity: 
        O(nk), where n is the number of elements in the transactions list and k is the number of digits in the greatest element
    """
    #finds the maximum integer in the list of integers in the certain column
    max_item=find_max_in_col_int(new_list,col)
    #intialize count array of the length max_item+1
    count_array=[None]*(max_item+1)
    #fill the count array with empty arrays 
    for i in range(len(count_array)):
        count_array[i]=[]
    #fill each element in count array with items according to the number in col and index
    for item in new_list:
        num=(item//pow(10,col))%10
        count_array[num].append(item)
    #update input array based in the count array
    index=0
    for item in count_array:
        if len(item)>0:
            for j in item:
                new_list[index]=j
                index+=1
    return new_list

#%% Function that finds the maximum integer in the list of integers
def find_max_int(list):
    """ 
    input: 
        list - a list of non-negative integers
    output:
        max - maximum integer in the list of integers
    Big O complexity: O(nk), where n is the number of elements in the lists list and k is the number of digits in the greatest element
    """
    max=list[0] 
    for item in list:
        if item>max:
            max=item
    return max

#%% Function that finds the maximum integer in the list of integers in the certain column
def find_max_in_col_int(list,col):
    """ 
    input: 
        list - a list of non-negative integers, 
        col - an integer which defines which column in the integers we should consider
    output: 
        max - maximum integer in the list of integers based on the column 
    Time complexity: O(nk), where n is the number of elements in the list list and k is the number of digits in the greatest element
    """
    max=0
    for item in list:
        num=(item//pow(10,col))%10
        if num>max:
            max=num
    return max

# %%Radix sort for the list of integers, stable.
def radix_sort_stable_int(new_list):
    """ 
    input: 
        new_list is an unsorted list of non-negative integers
    output: 
        new_list is the array sorted in the increasing order
    Time complexity: 
        O(nk), where n is the number of elements in the transactions list and k is the number of digits in the greatest element
    """
    #find the max integer in the list
    max_item=find_max_int(new_list)
    #find the number of digits in the maximum integer
    digits_in_max=count_digit_int(max_item)
    #sort based on every column from the most right to the most left 
    for i in range (digits_in_max):
        new_list=sort_counting_stable_col_int(new_list, i)
    return new_list

# %%Finds the number of digits in the integer
def count_digit_int(n):
    """ 
    input:
        n - the non-negative integer 
    output: 
        count - number of digits in the integer n
    Time complexity:
        O(k), where k is the number of digits in the greatest element
    """
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


#test
t = 5
transactions = [11, 1, 3, 1, 4, 10, 5, 7, 10]
print(best_interval(transactions, t))
