""" 
__author__ = "Tatiana Sutulova"
date: 21/3/2021
"""

#%% Task 2
def words_with_anagrams(list1, list2):
    """ 
    pre-condition: neither list contains duplicate strings
    input: 
        list1 and list2 - lists of strings qith all characters are lowercase a-z..
    output: 
        output - a list of strings from list1 which have at least one anagram appearing in list2.
    Time complexity: O(L1M1 + L2M2) where
        - L1 is the number of elements in list1
        - L2 is the number of elements in list2
        - M1 is the number of characters in the longest string in list1
        - M2 is the number of characters in the longest string in list2
    """
    #initializing the empty array of the length of list1
    temp_list1=[]*len(list1)
    #go through both lists and sort every element
    for j in range(len(list1)):
        #temp_array is an array that is filled with characters of the string list[j]
        temp_array=[]*len(list1[j]) #initializing the temp_array of length of the string list[j]
        #filling with characters of the string list[j]
        for char in list1[j]:
            temp_array.append(char)
        #sorting the word list[j]
        radix_sort_stable_string(temp_array)
        temp_string=""
        for i in temp_array:
            temp_string+=i
        #adding the element to the temporary array, which consists of:
        # temp_string = word worted by letters
        # j = position of the following word in the array list1
        # 1, which represents that this word is from the first array
        temp_list1.append([temp_string, j, 1 ])

    #initializing the empty array of the length of list2
    temp_list2=[]*len(list2)
    #go through both lists and sort every element
    for j in range(len(list2)):
        #temp_array is an array that is filled with characters of the string list2[j]
        temp_array=[]*len(list2[j]) #initializing the temp_array of length of the string list2[j]
        #filling with characters of the string list[j]
        for char in list2[j]:
            temp_array.append(char)
        #sorting the word list[j]
        radix_sort_stable_string(temp_array)
        temp_string=""
        for i in temp_array:
            temp_string+=i
        #adding the element to the temporary array, which consists of:
        # temp_string = word worted by letters
        # j = position of the following word in the array list2
        # 2, which represents that this word is from the second array
        temp_list2.append([temp_string, j, 2 ])
    
    #combine two lists into one
    big_list=temp_list1+temp_list2
    #sort in alphabetical order
    radix_sort_stable_special(big_list)
    #initializing the output array
    output=[]
    #initializing the pointer as the first element in the big_list
    i=0 
    j=0
    #looping through the array till i reaches the last element
    while i<len(big_list)-1:
        #if elements that j and (i plus 1) are pointing at are the same
        if big_list[i+1][0]==big_list[j][0]:
            #if elements at i+1 and j are not from the same list and first of them is from the list 1
            if big_list[i+1][2]!=big_list[j][2] and big_list[j][2]==1 :
                #adding the element at j to the output list
                output.append(list1[big_list[j][1]])
                #increasing j
                j+=1
            elif big_list[i+1][2]==big_list[j][2]:
                #if elements at i+1 and j are the same increase i
                i+=1
        else:
           #if elements that j and (i plus 1) are pointing at are NOT the same
           big_list[i+1], big_list[j+1]= big_list[j+1], big_list[i+1] #swapping i+1 and j+1 
           #increase both pointers 
           j+=1
           i+=1
    return output 

#%% Function counting sort stable based on column for the list of elements which are [[word, its_index, the_list_it_is_from]], stable. It takes up the word to sort by
def sort_counting_stable_col_special(new_list,col):
    """ 
    * the following function specially made to sort the array, which has elements [[word, its_index, the_list_it_is_from]] in which word is the string used for sorting
    input: 
        new_list is an unsorted list of [[word, its_index, the_list_it_is_from]] elements, where word is the lowercase string, col - an integer which defines which column in the string will the list be sorted according to.
    output: 
        new_list, the array sorted based on col.
    Time complexity:
        O(nk), where n is the number of elements in the new_list list and k is the number of letters in the greatest element
    """
    #intialize count array for 26 alphabets and space
    count_array=[None]*(27)
    #fill the count_array with empty array as each element
    for i in range(27):
        count_array[i]=[]
    #fill the count_array with words based on letters at column 
    for item in new_list:
        value=ord(item[0][col])-96
        if value<0:
            value=0
        count_array[value].append(item)
    #update an input array
    index=0
    for item in count_array:
        if len(item)>0:
            for j in item:
                new_list[index]=j
                index+=1
    return new_list


 # %%Radix sort

# %%Radix sort for the list of elements which are [[word, its_index, the_list_it_is_from]], stable. It takes up the word to sort by
def radix_sort_stable_special(new_list):
    """ 
    * the following function specially made to sort the array, which has elements [[word, its_index, the_list_it_is_from]] in which word is the string used for sorting
    input:
        new_list is an unsorted list of [[word, its_index, the_list_it_is_from]] elements, where word is the lowercase string
    output: 
        new_list, the array sorted based on col.
    Time complexity:
        O(nk), where n is the number of elements in the new_list list and k is the number of letters in the greatest element
    """
    #find the longest word in the array 
    longest=longest_word_special(new_list)
    #align all the words to the left, adding spaces to the right
    for i in range(len(new_list)):
        if len(new_list[i][0])<longest:
          temp=[new_list[i][0]+' '*(longest-len(new_list[i][0])), new_list[i][1],new_list[i][2]]
          new_list[i]=temp
    #sort based on place
    for i in range (longest):
        new_list=sort_counting_stable_col_special(new_list, (longest-i-1))
    #remove spaces in every word 
    for i in range(len(new_list)):
        temp=''
        for character in new_list[i][0]:
            if character!=' ': 
                temp+=character
        new_list[i]=[temp, new_list[i][1],new_list[i][2]]
    return new_list

# %% Find the longest word for the list of elements which are [[word, its_index, the_list_it_is_from]], stable. It takes up the word to find the longest word
def longest_word_special(new_list):
    """ 
    * the following function specially made to work on the array, which has elements [[word, its_index, the_list_it_is_from]]
    input: 
        new_list is an unsorted list of [[word, its_index, the_list_it_is_from]] elements, where word is the lowercase string
    output: 
        max, the longest word in the new_list
    Time complexity: 
        O(nk), where n is the number of elements in the new_list list and k is the number of letters in the greatest element
    """
    max=0
    for item in new_list:
        temp=len(item[0])
        if max<temp:
            max=temp
    return max


#%% Function counting sort stable based on column for strings
def sort_counting_stable_col_string(new_list,col):
    """ 
    input: 
        - new_list is an unsorted list of lowercase strings
        - col is an integer which defines which column in the  will the list be sorted according to.
    output:
         new_list, the array sorted based on col.
    Time complexity:
         O(nk), where n is the number of elements in the new_list list and k is the number of letters in the greatest element
    """
    #intialize count array for 26 alphabets and space 
    count_array=[None]*(27)
    #fill the count_array with empty array as each element
    for i in range(27):
        count_array[i]=[]
    #fill the count_array with words based on letters at column 
    for item in new_list:
        value=ord(item[col])-96
        if value<0:
            value=0
        count_array[value].append(item)
    #update input array
    index=0
    for item in count_array:
        if len(item)>0:
            for j in item:
                new_list[index]=j
                index+=1
    return new_list

# %%Radix sort for the list of string
def radix_sort_stable_string(new_list):
    """ 
    input:
        new_list is an unsorted list of lowercase strings
    output: 
        new_list, the array sorted based on col.
    Time complexity: 
        O(nk), where n is the number of elements in the new_list list and k is the number of letters in the greatest element
    """
    #find the longest word in the array 
    longest=longest_word_string(new_list)
    #find the longest word in the array 
    for i in range(len(new_list)):
        if len(new_list[i])<longest:
            new_list[i]=new_list[i]+' '*(longest-len(new_list[i]))
    #sort based on place
    for i in range (longest):
        new_list=sort_counting_stable_col_string(new_list, (longest-i-1))
    #remove spaces in every word 
    for i in range(len(new_list)):
        temp=''
        for character in new_list[i]:
            if character!=' ': 
                temp+=character
        new_list[i]=temp
    return new_list

# %% Find the longest word for the list of strings
def longest_word_string(new_list):
    """ 
    input: 
        new_list is an unsorted list of lowercase strings
    output: 
        max, the longest word in the new_list
    Time complexity:
         O(nk), where n is the number of elements in the new_list list and k is the number of letters in the greatest element
    """
    max=0
    for item in new_list:
        temp=len(item)
        if max<temp:
            max=temp
    return max

#test
list1 = ['spot', 'tops', 'dad', 'simple', 'dine','cats' ]
list2 = ['pots','add','simple','dined', 'acts','cast']
print(words_with_anagrams(list1, list2))

