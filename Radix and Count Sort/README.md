1. best_schedule.py:
 General idea: 
   Consider a large dataset of transaction records. Given a number t, we wish to determine which
   interval of length t contains the most transactions. All times in this question are measured in
   whole seconds after midnight 1/1/1970, i.e. they are non-negative integers. The function best_interval(transactions, t),
   is based on stable counting and radix sort and it allows to find the start time of the time interval with the more
   transactions than interval of the same length starting at any other time. 
 1.1 Input
   - transactions is a unsorted list of non-negative integers. Each integer in transactions represents
     the time that some transaction occurred.
   - t is a non-negative integer, representing a length of time in seconds.
 1.2 Output
     tuple of (best_t, count):
          - best_t is the time such that the interval starting at best_t and ending at best_t + t contains more elements from transactions
            than any other interval of length t.
          - count is the number of elements in the interval of length t starting at best_t.
 1.3 Example
    t = 5
    transactions = [11, 1, 3, 1, 4, 10, 5, 7, 10]
    >>> best_interval(transaction, t)
    (0, 5)
1.4 Time Complexity
      O(nk) where
      - n is the number of elements in transactions
      - k is the greatest number of digits in any element in transactions
    
2. words_with_anagrams.py:
 General idea: 
    Given two lists of words, we wish to find all words in the firstlist which have an anagram in the second list.
    words_with_anagrams(list1, list2) is based on stable counting and radix sort and it allows to find
 2.1 Input
    Both arguments, list1 and list2, are lists of strings. All characters are lowercase a-z. Neither
    list contains duplicate strings, but there may be strings which appear in both lists.
 2.2 Output
  - a list of strings from list1 which have at least one anagram appearing in list2.
 2.3 Example
    list1 = [spot, tops, dad, simple, dine, cats]
    list2 = [pots, add, simple, dined, acts, cast]
    >>> words_with_anagrams(list1, list2)
    [cats, dad, simple, spot, tops]
2.4  Time complexity: O(L1M1 + L2M2) where
        - L1 is the number of elements in list1
        - L2 is the number of elements in list2
        - M1 is the number of characters in the longest string in list1
        - M2 is the number of characters in the longest string in list2
