"""
__author__ = "Tatiana Sutulova"
date: 7/5/2021
"""

class Node:
    """A node in the trie structure"""

    def __init__(self, char):
        # in case it is final
        # the character of the node
        self.char = char
        # in case it is final
        self.counter = 0  # times the word which ends at this node was added
        self.final_word = ''  # the entire word that ends at this node

        # children nodes of this node: A/B/C/D/$
        self.children = [None] * 5

        # the information stored in the node for the lexico check
        self.lexico_char = ' '  # character of the node which is the nearest child towards the final output
        self.lexico_node = None  # reference to the node which is the current output


class SequenceDatabase:
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = Node(' ')

    def addSequence(self, word):
        """
        Input:
            - word, a single nonempty string of uppercase letters in uppercase [A-D]
        Output:
            None
        Short description: Makes the recursive call in order to fill up the trie
        Time complexity: O(len(s)) time, where s is the input string
        """
        node = self.root
        self.addSequence_recursive(node, word, 0)
        # if the root node does not have any children nodes, references itself
        if node.lexico_node is None:
            node.lexico_node = node

    def addSequence_recursive(self, node, word, i):
        """
        Input:
            - node, instance of the Node class, which we are currently at
            - word, entire word that is being insert
            - i, pointer on which letter of the word we are at
        Output:
            - []: array, which holds the reference to the leaf node, which is the current output and
                        the character of the nearest child node from current node towards the leaf node
        Short description: Fills up the tree by checking whether trie has a sequence and add new nodes if it does not.
                           When the last character of the word is added, we recursively compare values in nodes of the
                           with the new added one, changing it accordingly:
                                - if the new word has greater count
                                - if the new word has the same count, but lexicographically smaller
                           In oder to check, whether one word is lexicographically smaller, in the current node we store
                           the character of the child node, which allows to compare it when the other word is added

        Time complexity: O(len(s)) time, where s is the input string
        """
        # reaches the end of the word. current node will be holding the last character of the word
        if i == len(word):
            # creating the terminal node
            node.children[0] = Node(' ')
            node.final_word = word
            node.counter += 1
            # if there is no lexico node, pointing at itself
            if node.lexico_node is None:
                node.lexico_node = node
            else:
                # if there is a lexico node compare it's counters
                if node.counter >= node.lexico_node.counter:
                    # this case is only accessed when the current node is the last char of one word and part of another
                    # therefore, if the counters are equal, we choose the shorter one
                    node.lexico_char = ' '
                    node.lexico_node = node
            return [node.lexico_node, node.char]


        else:
            # we go up till last character of the word
            index = ord(word[i]) - 65+1
            if node.children[index] is None:
                new_node = Node(word[i])
                node.children[index] = new_node
            # when the last character is set it will return current node, which holds the final word and the character
            # in the node, which is the nearest subnode towards the final node
            current_choice = self.addSequence_recursive(node.children[index], word, i + 1)

            # if current node does not have lexico node, we set it to the one returned previously
            if node.lexico_node is None:
                node.lexico_node = current_choice[0]
                node.lexico_char = current_choice[1]
            else:
                # if the current node does have the reference to the lexico node, we compare it's counters and reset lexico node accordingly
                if node.lexico_node.counter < current_choice[0].counter:
                    node.lexico_node = current_choice[0]
                    node.lexico_char = current_choice[1]
                # if counters are the same, we check the character, which is the closest one towards the lexico node
                elif node.lexico_node.counter == current_choice[0].counter:
                    if ord(node.lexico_char) >= ord(current_choice[1]):
                        # reset the lexico node accordingly
                        node.lexico_node = current_choice[0]
                        node.lexico_char = current_choice[1]

            return [node.lexico_node, node.char]

    def query(self, q):
        """
        Input:
                q, a single (possibly empty) string of uppercase letters in uppercase [A-D].
        Output:
            a string with the following properties:
                - has q as a prefix
                - higher frequency in the database than any other string with q as a prefix
                - or if two or more strings with a prefix q are most frequent, return lexicographically the smallest
            None, if there is no such string

        Short description: get the word, described in the Output. Since when inserting words we are updating
                           all the nodes accordingly, in order to get the word, we loop till the the last letter of the
                           prefix and get the word stored in this node.

        Time complexity: O(len(q)), where q is the input prefix
        """

        # start with the root node
        node = self.root

        # Check if the prefix is in the trie
        for char in q:
            index = ord(char) - 65+1  # leaving 0 for $
            if node.children[index] is not None:
                node = node.children[index]
            else:
                return None
        # in the case of no word inserted, root node's reference is set to None
        if node.lexico_node is None:
            return None
        return node.lexico_node.final_word
