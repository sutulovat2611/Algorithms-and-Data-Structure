import unittest
from assignment2 import best_schedule , best_itinerary
import random
import time


class MyTestCase(unittest.TestCase):
    def test_best_schedule_1(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5] #change
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 1)]  #change
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 42 #change
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + most_cash + "."

    def test_best_schedule_2(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 35), (3, 5, 19), (5, 6, 1)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 44
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_3(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 14)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 44
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_4(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (3, 4, 30), (3, 5, 19), (5, 6, 1)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 57
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_5(self):
        regular_work = [3, 7, 18, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 14)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 52
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_6(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 5, 14)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 49
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_7(self):
        regular_work = [3, 7, 2, 1, 18, 4, 5]
        special_events = [(1, 3, 15), (2, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 1)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 46
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_8(self):
        regular_work = [3, 7, 2, 1, 8, 4, 5]
        special_events = [(1, 3, 15), (1, 2, 8), (0, 4, 30), (3, 5, 19), (5, 6, 4)]  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 39
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."

    def test_best_schedule_9(self): # no work no time nothing
        regular_work = []
        special_events = []  #
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 0
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."


    def test_best_schedule_10(self):
        regular_work = [3, 7, 2, 5, 8, 4, 5]
        special_events = [(1, 3, 15), (1, 2, 14), (0, 4, 30), (3, 5, 19)]  
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 41
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."
    
    # compare competition within same week
    def test_best_schedule_11(self):
        regular_work = [1]
        special_events = [(0, 0, 7), (0,0,10)]  
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 10
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."
    
    def test_best_schedule_12(self):
        regular_work = [11,2]
        special_events = [(0, 0, 7), (0,0,10)]  
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 13
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."
    
    def test_best_schedule_13(self):
        regular_work = [11]
        special_events = [(0, 0, 7), (0,0,10)]  
        most_cash = best_schedule(regular_work, special_events)
        expected_output = 11
        assert most_cash == expected_output , "best_schedule(" + str(regular_work) +  "," + str(special_events) +") should be " + str(expected_output) + " not " + str(most_cash) + "."


    def test_best_itinerary1(self):
        profit = [
            [6, 9, 7, 5, 9],
            [4, 7, 3, 10, 9],
            [7, 5, 4, 2, 8],
            [2, 7, 10, 9, 5],
            [2, 5, 2, 6, 1],
            [4, 9, 4, 10, 6],
            [2, 2, 4, 8, 7],
            [4, 10, 2, 7, 4]] # change
        quarantine = [3, 1, 1, 1, 1] #change
        home = 0 #change

        output = best_itinerary(profit,quarantine , home)
        expected_val = 39 #change
        lst_str = "["
        for l in profit:
            lst_str+= str(l) + "\n"
        lst_str+= "]"
        assert output == expected_val , "\n\n\nbest_itenerary(\n" + lst_str + "\nshould be " + str(expected_val) + " not " + str(output) + "."

    def test_best_itinerary2(self):
        profit = [
            [6, 9, 7, 5, 9],
            [4, 7, 3, 10, 9],
            [7, 5, 4, 2, 8],
            [2, 7, 10, 9, 5],
            [2, 5, 2, 6, 1],
            [4, 9, 4, 10, 6],
            [2, 2, 4, 8, 7],
            [4, 10, 2, 7, 4]]
        quarantine = [3, 1, 1, 1, 1]
        home = 1

        output = best_itinerary(profit,quarantine , home)
        expected_val = 54
        lst_str = "["
        for l in profit:
            lst_str+= str(l) + "\n"
        lst_str+= "]"
        assert output == expected_val , "\n\n\nbest_itenerary(\n" + lst_str + "\nshould be " + str(expected_val) + " not " + str(output) + "."

    def test_best_itinerary3(self):
        profit = [
            [6, 9, 7, 5, 9],
            [4, 7, 3, 10, 9],
            [7, 5, 4, 2, 8],
            [2, 7, 10, 9, 5],
            [2, 5, 2, 6, 1],
            [4, 9, 4, 10, 6],
            [2, 2, 4, 8, 7],
            [4, 10, 2, 7, 4]]
        quarantine = [3, 1, 1, 1, 1]
        home = 2

        output = best_itinerary(profit,quarantine , home)
        expected_val = 47
        lst_str = "["
        for l in profit:
            lst_str+= str(l) + "\n"
        lst_str+= "]"
        assert output == expected_val , "\n\n\nbest_itenerary(\n" + lst_str + "\nshould be " + str(expected_val) + " not " + str(output) + "."

    def test_best_itinerary4(self):
        profit = [
            [6, 9, 7, 5, 9],
            [4, 7, 3, 10, 9],
            [7, 5, 4, 2, 8],
            [2, 7, 10, 9, 5],
            [2, 5, 2, 6, 1],
            [4, 9, 4, 10, 6],
            [2, 2, 4, 8, 7],
            [4, 10, 2, 7, 4]]
        quarantine = [3, 1, 1, 1, 1]
        home = 3

        output = best_itinerary(profit,quarantine , home)
        expected_val = 57
        lst_str = "["
        for l in profit:
            lst_str+= str(l) + "\n"
        lst_str+= "]"
        assert output == expected_val , "\n\n\nbest_itenerary(\n" + lst_str + "\nshould be " + str(expected_val) + " not " + str(output) + "."

    def test_best_itinerary5(self):
        profit = [
            [6, 9, 7, 5, 9],
            [4, 7, 3, 10, 9],
            [7, 5, 4, 2, 8],
            [2, 7, 10, 9, 5],
            [2, 5, 2, 6, 1],
            [4, 9, 4, 10, 6],
            [2, 2, 4, 8, 7],
            [4, 10, 2, 7, 4]]
        quarantine = [3, 1, 1, 1, 1]
        home = 4

        output = best_itinerary(profit,quarantine , home)
        expected_val = 51
        lst_str = "["
        for l in profit:
            lst_str+= str(l) + "\n"
        lst_str+= "]"
        assert output == expected_val , "\n\n\nbest_itenerary(\n" + lst_str + "\nshould be " + str(expected_val) + " not " + str(output) + "."

    def test_best_itinerary6(self):
        profit = [
            [6, 9, 7, 5, 9],
            [4, 7, 3, 10, 9],
            [7, 5, 4, 2, 8],
            [2, 7, 10, 9, 8],
            [2, 7, 10, 9, 8],
            [35, 5, 2, 6, 111]]
        quarantine = [3, 1, 5, 1, 2]
        home = 1

        output = best_itinerary(profit,quarantine , home)
        expected_val = 111
        lst_str = "["
        for l in profit:
            lst_str+= str(l) + "\n"
        lst_str+= "]"
        assert output == expected_val , "\n\n\nbest_itenerary(\n" + lst_str + "\nshould be " + str(expected_val) + " not " + str(output) + "."


    def test_best_itinerary7(self):
        profit = [
            [6, 9, 7, 5, 9],
            [4, 7, 3, 10, 9],
            [7, 5, 4, 2, 8],
            [2, 7, 10, 9, 8],
            [35, 5, 2, 6, 111]]
        quarantine = [3, 1, 1, 3, 2]
        home = 2

        output = best_itinerary(profit,quarantine , home)
        expected_val = 111
        lst_str = "["
        for l in profit:
            lst_str+= str(l) + "\n"
        lst_str+= "]"
        assert output == expected_val , "\n\n\nbest_itenerary(\n" + lst_str + "\nshould be " + str(expected_val) + " not " + str(output) + "."

    def test_best_itinerary8(self):
        profit = [
            [6, 9, 7, 5, 9],
            [4, 7, 3, 10, 9]
            ]
        quarantine = [3, 1, 1, 1, 2]
        home = 1

        output = best_itinerary(profit,quarantine , home)
        expected_val = 16
        lst_str = "["
        for l in profit:
            lst_str+= str(l) + "\n"
        lst_str+= "]"
        assert output == expected_val , "\n\n\nbest_itenerary(\n" + lst_str + "\nshould be " + str(expected_val) + " not " + str(output) + "."

    def test_best_itinerary9(self):
        profit = [
            [6, 9, 7, 5, 9],
            [4, 7, 3, 10, 9],
            [4, 7, 1, 10, 9],
            [7, 1, 100, 2, 8],
            [2, 7, 10, 9, 5],
            [2, 5, 2, 6, 1],
            [4, 9, 4, 10, 6],
            [2, 5, 2, 6, 1],
            [2, 2, 4, 8, 7],
            [1000, 10, 2, 7, 4]]
        quarantine = [3, 1, 1, 1, 1]
        home = 0

        output = best_itinerary(profit,quarantine , home)
        expected_val = 1100
        lst_str = "["
        for l in profit:
            lst_str+= str(l) + "\n"
        lst_str+= "]"
        assert output == expected_val , "\n\n\nbest_itenerary(\n" + lst_str + "\nshould be " + str(expected_val) + " not " + str(output) + "."

    def test_best_itinerary_nathan_from_ed(self):
        """Test from ed lecturer"""
        passed = False
        try:
            assert (best_itinerary(
                [[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7],
                 [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7],
                 [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7],
                 [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]], [2, 2, 1, 1, 1], 0) == 118)
            assert (best_itinerary(
                [[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7],
                 [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7],
                 [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7],
                 [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]], [2, 2, 1, 1, 1], 1) == 115)
            assert (best_itinerary(
                [[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7],
                 [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7],
                 [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7],
                 [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]], [2, 2, 1, 1, 1], 2) == 119)
            assert (best_itinerary(
                [[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7],
                 [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7],
                 [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7],
                 [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]], [2, 2, 1, 1, 1], 3) == 117)
            assert (best_itinerary(
                [[2, 2, 9, 2, 4], [9, 3, 6, 5, 7], [9, 2, 4, 9, 7], [5, 2, 10, 2, 3], [1, 8, 2, 7, 8], [2, 9, 2, 2, 7],
                 [9, 6, 1, 10, 1], [10, 9, 6, 7, 6], [9, 10, 1, 8, 6], [8, 4, 1, 7, 3], [5, 2, 5, 4, 7],
                 [5, 5, 9, 8, 3], [3, 4, 1, 6, 9], [7, 6, 9, 6, 5], [9, 2, 6, 6, 4], [1, 5, 6, 4, 3], [2, 7, 7, 5, 7],
                 [8, 2, 7, 4, 8], [3, 8, 9, 4, 4], [9, 9, 10, 9, 8]], [2, 2, 1, 1, 1], 4) == 111)
            assert (best_itinerary(
                [[5, 1, 10, 9, 10], [6, 3, 8, 2, 7], [4, 4, 2, 6, 9], [10, 2, 5, 8, 10], [4, 9, 4, 4, 8],
                 [2, 9, 5, 2, 4], [10, 7, 3, 8, 2], [2, 4, 1, 7, 10], [1, 9, 3, 3, 3], [5, 9, 2, 3, 2], [9, 4, 3, 6, 1],
                 [1, 7, 3, 10, 3], [5, 6, 7, 2, 1], [1, 2, 10, 4, 8], [3, 4, 7, 5, 4], [1, 6, 4, 3, 9],
                 [1, 10, 5, 4, 9], [4, 10, 6, 7, 3], [1, 8, 1, 2, 7], [8, 2, 10, 3, 6]], [3, 3, 2, 3, 5], 0) == 106)
            assert (best_itinerary(
                [[5, 1, 10, 9, 10], [6, 3, 8, 2, 7], [4, 4, 2, 6, 9], [10, 2, 5, 8, 10], [4, 9, 4, 4, 8],
                 [2, 9, 5, 2, 4], [10, 7, 3, 8, 2], [2, 4, 1, 7, 10], [1, 9, 3, 3, 3], [5, 9, 2, 3, 2], [9, 4, 3, 6, 1],
                 [1, 7, 3, 10, 3], [5, 6, 7, 2, 1], [1, 2, 10, 4, 8], [3, 4, 7, 5, 4], [1, 6, 4, 3, 9],
                 [1, 10, 5, 4, 9], [4, 10, 6, 7, 3], [1, 8, 1, 2, 7], [8, 2, 10, 3, 6]], [3, 3, 2, 3, 5], 1) == 116)
            assert (best_itinerary(
                [[5, 1, 10, 9, 10], [6, 3, 8, 2, 7], [4, 4, 2, 6, 9], [10, 2, 5, 8, 10], [4, 9, 4, 4, 8],
                 [2, 9, 5, 2, 4], [10, 7, 3, 8, 2], [2, 4, 1, 7, 10], [1, 9, 3, 3, 3], [5, 9, 2, 3, 2], [9, 4, 3, 6, 1],
                 [1, 7, 3, 10, 3], [5, 6, 7, 2, 1], [1, 2, 10, 4, 8], [3, 4, 7, 5, 4], [1, 6, 4, 3, 9],
                 [1, 10, 5, 4, 9], [4, 10, 6, 7, 3], [1, 8, 1, 2, 7], [8, 2, 10, 3, 6]], [3, 3, 2, 3, 5], 2) == 107)
            assert (best_itinerary(
                [[5, 1, 10, 9, 10], [6, 3, 8, 2, 7], [4, 4, 2, 6, 9], [10, 2, 5, 8, 10], [4, 9, 4, 4, 8],
                 [2, 9, 5, 2, 4], [10, 7, 3, 8, 2], [2, 4, 1, 7, 10], [1, 9, 3, 3, 3], [5, 9, 2, 3, 2], [9, 4, 3, 6, 1],
                 [1, 7, 3, 10, 3], [5, 6, 7, 2, 1], [1, 2, 10, 4, 8], [3, 4, 7, 5, 4], [1, 6, 4, 3, 9],
                 [1, 10, 5, 4, 9], [4, 10, 6, 7, 3], [1, 8, 1, 2, 7], [8, 2, 10, 3, 6]], [3, 3, 2, 3, 5], 3) == 99)
            assert (best_itinerary(
                [[5, 1, 10, 9, 10], [6, 3, 8, 2, 7], [4, 4, 2, 6, 9], [10, 2, 5, 8, 10], [4, 9, 4, 4, 8],
                 [2, 9, 5, 2, 4], [10, 7, 3, 8, 2], [2, 4, 1, 7, 10], [1, 9, 3, 3, 3], [5, 9, 2, 3, 2], [9, 4, 3, 6, 1],
                 [1, 7, 3, 10, 3], [5, 6, 7, 2, 1], [1, 2, 10, 4, 8], [3, 4, 7, 5, 4], [1, 6, 4, 3, 9],
                 [1, 10, 5, 4, 9], [4, 10, 6, 7, 3], [1, 8, 1, 2, 7], [8, 2, 10, 3, 6]], [3, 3, 2, 3, 5], 4) == 116)

            passed = True

        except:
            assert False,"Failed test from ed. Please refer to the link : " + "https://edstem.org/courses/5287/discussion/412570"
    
    def test_best_itinerary11(self):
        profit = [
            [6, 9, 70, 5, 3, 9],
            [4, 7, 3, 3, 10, 9],
            [4, 7, 1, 2, 10, 9],
            [7, 1100, 100, 2, 3, 8],
            [2 , 3, 7, 10, 9, 5],
            [2, 5, 2, 3, 6, 1],
            [4, 9, 4, 10, 3, 6],
            [2, 3, 7, 10, 9, 5],
            [2, 3, 5, 2, 6, 1],
            [2, 3, 2, 4, 8, 7],
            [10, 10, 2, 5, 7, 401]]
        quarantine = [3, 1, 5, 1, 7, 2]
        home = 2

        output = best_itinerary(profit,quarantine , home)
        expected_val = 1571
        lst_str = "["
        for l in profit:
            lst_str+= str(l) + "\n"
        lst_str+= "]"
        assert output == expected_val , "\n\n\nbest_itenerary(\n" + lst_str + "\nshould be " + str(expected_val) + " not " + str(output) + "."


if __name__ == '__main__':
    unittest.main()
