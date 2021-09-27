

from random import randint, seed
from best_itinerary import best_itinerary
from best_schedule import best_schedule 
from time import time


def generate_competition(weeks, min_winnings, max_winnings):
    return (start := randint(0, weeks)), randint(start, weeks), randint(min_winnings, max_winnings)


def generate_day(number_cities, min_profit, max_profit):
    return [randint(min_profit, max_profit) for _ in range(number_cities)]


if __name__ == "__main__":
    # Seed
    SEED = "FIT2004"

    # Constants for best schedule. Test your own and check how long it takes!
    MIN_WINNINGS = 0
    MAX_WINNINGS = 1000000
    MIN_EARNINGS = 0
    MAX_EARNINGS = 10000
    WEEKS = 10000
    COMPETITIONS = 10000

    # For best itinerary
    MIN_PROFIT = 0
    MAX_PROFIT = 100000
    CITIES = 100
    DAYS = 10000
    MIN_QUARANTINE = 0
    MAX_QUARANTINE = 14
    HOME = 0

    seed(SEED)

    competitions = [generate_competition(WEEKS, MIN_WINNINGS, MAX_WINNINGS) for _ in range(COMPETITIONS)]
    weekly_income = [randint(MIN_EARNINGS, MAX_EARNINGS) for _ in range(10000)]

    profit = [generate_day(CITIES, MIN_PROFIT, MAX_PROFIT) for _ in range(DAYS)]
    quarantine_time = [randint(MIN_QUARANTINE, MAX_QUARANTINE) for _ in range(CITIES)]

    # Actual calculations

    # competitions[4000] = (4000, 4000, 1000000000)
    start_time = time()
    bs = best_schedule(weekly_income, competitions)
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Best profit: {bs} | Took {elapsed_time} seconds")

    # profit[1000][40] = 1000000000
    start_time = time()
    bi = best_itinerary(profit, quarantine_time, HOME)
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Best itinerary: {bi} | Took {elapsed_time} seconds")
