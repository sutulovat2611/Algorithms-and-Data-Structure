"""
__author__ = "Tatiana Sutulova"
date: 7/5/2021
"""

class Node:
    """A node in the trie structure"""
    def __init__(self):
        self.link = [None] * 5
        # indexes in the word that the current letter is at, e.g "ABABA" -> A has indexes 0,2,4
        self.indexes = []


class OrfFinder:
    """The trie object"""
    def __init__(self, word):
        """
        Input:
            - word, the entire word that we are inserting
        Output:
            None
        Short description: fills up the trie and for each node sets the indexes accordingly
        Time complexity: O(N^2), where N is the length of the word
        """
        self.word = word
        self.root = Node()
        # inserting all the suffixes starting from each letter
        for letter_to_start in range(len(word)):
            self.insert(word, letter_to_start)

    def insert(self, word, letter_to_start):
        """
        Input:
            - word, the entire word that we are inserting
            - letter_to_start, the starting point from where teh loop starts
        Output:
            None
        Short description: fills up the trie and for each node sets the indexes accordingly
        Time complexity: O(N), where N is the length of the word
        """

        # start from the root
        current = self.root
        for i in range(letter_to_start, len(word)):
            index = ord(word[i]) - 65 + 1
            # if the node for current letter does not exist create a new node
            if current.link[index] is None:
                current.link[index] = Node()
            # i is the index of the current letter in the word
            current.link[index].indexes.append(i)
            current = current.link[index]

        # set for the leaf node
        if current.link[0] is None:
            current.link[0] = Node()

    def find(self, start, end):
        """
        Input:
            - start, single non-empty string consisting of only uppercase [A-D]
            - end, single non-empty string consisting of only uppercase [A-D].
        Output:
            - sub_words, a list of strings, which contains all the substrings of genome which have start
            as a prefix and end as a suffix (start and end do not overlap in the string)
        Time complexity: (len(start) + len(end) + U) time, where U is the number of characters in the output list.
        """
        # getting the indexes of the last character of the end
        current = self.root
        for char in end:
            index = ord(char) - 65 + 1
            if current.link[index] is None:
                # if the end is not in the word
                return []
            else:
                current = current.link[index]
        last_node_end = current.indexes

        # getting the indexes of the last character of the start
        current = self.root
        for char in start:
            index = ord(char) - 64
            if current.link[index] is None:
                # if the start is not in the word
                return []
            else:
                current = current.link[index]
        last_node_start = current.indexes

        sub_words = []

        leng_start = len(start)
        leng_end = len(end)
        # for each start index in the word we take the range from it to each index in the end
        for i in last_node_start:
            for j in last_node_end:
                # making sure that they do not overlap
                if i < j:
                    if i < j + 1 - leng_end:
                        word = self.word[i + 1 - leng_start:(j + 1)]
                        sub_words.append(word)
        return sub_words
