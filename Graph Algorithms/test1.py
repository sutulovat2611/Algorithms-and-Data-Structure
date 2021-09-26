import unittest
from assignment4 import best_trades, opt_delivery
import string
import random
import simplejson
from decimal import getcontext, Decimal
from decimal import *


getcontext().prec = 100
filename = "generated_cases.json"
use_autogenerated = True  # Set to false to not use.

# Open and load the data. This could take a while, so only do it once.
try:
    with open(filename) as file_cases:
        test_data = simplejson.loads(file_cases.read(), use_decimal=True)
except FileNotFoundError:
    print("Could not load {}".format(filename))
    use_autogenerated = False

#
class TestBestTrades(unittest.TestCase):
    def test_included(self):
        """ Tests with the included test case """
        prices = [10, 5, 1, 0.1]
        starting_liquid = 0
        max_trades = 6
        townspeople = [[(0, 1, 4), (2, 3, 30)], [(1, 2, 2.5), (2, 0, 0.2)]]
        result = best_trades(prices, starting_liquid, max_trades, townspeople)
        expected = 60
        self.assertEqual(result, expected)

        max_trades = 2
        result = best_trades(prices, starting_liquid, max_trades, townspeople)
        expected = 20
        self.assertEqual(result, expected)

    def test_single_liquid(self):
        """ Tests with a single liquid """
        prices = [20]
        starting_liquid = 0
        max_trades = 10
        townspeople = [[(0, 0, 1), (0, 0, 0.5)], [(0, 0, 1)]]
        result = best_trades(prices, starting_liquid, max_trades, townspeople)
        expected = 20
        self.assertEqual(result, expected)

        # Test with trading all the time
        townspeople = [[(0, 0, 2), (0, 0, 0.5)], [(0, 0, 1)]]
        result = best_trades(prices, starting_liquid, max_trades, townspeople)
        expected = 20 * 2 ** 10
        self.assertEqual(result, expected)

    def test_non_0_start(self):
        """ Tests with a non 0 starting position. Also tests for wise choices
        of volume. """
        prices = [10, 10, 10, 10, 10]
        starting_liquid = 1
        max_trades = 10
        townspeople = [[(1, 4, 3), (1, 2, 10), (4, 0, 10), (2, 3, 2)]]
        result = best_trades(prices, starting_liquid, max_trades, townspeople)
        expected = 300
        self.assertEqual(result, expected)

    def test_varying_price(self):
        """ Tests with constant volume and varying price of liquids """
        prices = [1, 3, 2, 5, 4]
        starting_liquid = 2
        max_trades = 3
        townspeople = [[(1, 4, 3), (1, 2, 10), (4, 0, 10), (2, 3, 2)]]
        result = best_trades(prices, starting_liquid, max_trades, townspeople)
        expected = 10
        self.assertEqual(result, expected)

    def test_manual(self):
        """ Something I calculated and came up with by hand that has moderately nice numbers (use fractions if doing by hand). """
        prices = [10, 2, 3, 5, 2]
        starting_liquid = 1
        max_trades = 4
        townspeople = [[(0, 4, 4), (4, 1, 1), (1, 3, 0.5), (3, 2, 3), (2, 1, 2), (3, 4, 5), (1, 4, 2), (4, 0, 0.5)]]
        result = best_trades(prices, starting_liquid, max_trades, townspeople)
        expected = 20
        self.assertEqual(result, expected)

    def test_0_max_trades(self):
        """ See https://edstem.org/courses/5287/discussion/487414
        if max_trades <= 0, should return the value of the first. """
        prices = [10, 2, 3, 5, 2]
        starting_liquid = 1
        max_trades = 0
        townspeople = [[(0, 4, 4), (4, 1, 1), (1, 3, 0.5), (3, 2, 3), (2, 1, 2), (3, 4, 5), (1, 4, 2), (4, 0, 0.5)]]
        result = best_trades(prices, starting_liquid, max_trades, townspeople)
        expected = 2
        self.assertEqual(result, expected)

    def test_generated(self):
        """ Tests an imported file of test cases
        """
        if not use_autogenerated or "best_trades" not in test_data:
            return

        test_count = 0
        for case in test_data["best_trades"]:
            result = best_trades(*case["arguments"])
            error_message = """Failed autogenerated test {0}.
PARAMETERS:
  - prices = {1}
  - starting_liquid = {2}
  - max_trades = {3}
  - townspeople = {4}

EXPECTED: {5}
GOT: {6}
""".format(test_count, case["arguments"][0], case["arguments"][1], case["arguments"][2], case["arguments"][3],
           case["expected"], result)
            # self.assertEqual(result, case["expected"], error_message)
            rel_tol = 1e-15  # Thanks to Hamish Self (https://edstem.org/courses/5287/discussion/470865?comment=1112178)
            self.assertAlmostEqual(float(result), float(case["expected"]), msg=error_message,
                                   delta=rel_tol * float(case['expected']))
            test_count += 1


class TestOptDelivery(unittest.TestCase):
    def test_included(self):
        """ Tests with the included test case """
        n = 4
        roads = [(0, 1, 3), (0, 2, 5), (2, 3, 7), (1, 3, 20)]
        start = 0
        end = 1
        delivery = (2, 3, 25)
        result = opt_delivery(n, roads, start, end, delivery)
        expected = (2, [0, 2, 3, 2, 0, 1])
        self.assertEqual(result, expected)

        delivery = (2, 3, 20)
        result = opt_delivery(n, roads, start, end, delivery)
        expected = (3, [0, 1])
        self.assertEqual(result, expected)

        delivery = (2, 3, 100)
        result = opt_delivery(n, roads, start, end, delivery)
        expected = (-73, [0, 2, 3, 2, 0, 1])
        self.assertEqual(result, expected)

    def test_equal_value(self):
        """ If the cost is equal, return the path without the parcel """
        n = 4
        roads = [(2, 3, 1), (3, 1, 2), (2, 0, 4), (1, 0, 2)]
        start = 2
        end = 0
        delivery = (3, 1, 1)
        expected = (4, [2, 0])
        result = opt_delivery(n, roads, start, end, delivery)
        self.assertEqual(result, expected)

    def test_generated(self):
        """ Tests an imported file of test cases
        """
        if not use_autogenerated or "opt_delivery" not in test_data:
            return

        test_count = 0
        for case in test_data["opt_delivery"]:
            result = opt_delivery(*case["arguments"])
            error_message = """Failed autogenerated test {0}.
PARAMETERS:
  - n = {1}
  - roads = {2}
  - start = {3}
  - end = {4}
  - delivery = {5}

EXPECTED: {6}
GOT: {7}
""".format(test_count, case["arguments"][0], case["arguments"][1], case["arguments"][2], case["arguments"][3],
           case["arguments"][4], case["expected"], result)
            self.assertEqual(result, tuple(case["expected"]), error_message)
            test_count += 1


if __name__ == '__main__':
    if not use_autogenerated:
        print("WARNING: Not using autogenerated tests for one reason or another")
    # Start the testing.
    unittest.main(exit=False)

    if use_autogenerated:
        if "best_trades" not in test_data or len(test_data["best_trades"]) == 0:
            print("WARNING: No autogenerated test cases for best trades")
        if "opt_delivery" not in test_data or len(test_data["opt_delivery"]) == 0:
            print("WARNING: No autogenerated test cases for optimal delivery")
    else:
        print("To reiterate: WARNING: Autogenerated tests not used for one reason or another")