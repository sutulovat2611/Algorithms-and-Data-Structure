from DNA_fragments import *
from orf_finder import *
import unittest
import random as rd
import statistics as st

# SequenceDatabase PARAMS
S_STRING_LEN = 6  # the maximum length of string to insert (4^STRING_LEN should be ~TEST_NUM for good tests)
S_TEST_NUM = 100# the number of tests to run per database
S_DATABASE_NUM = 100 # the number of databases to test

# OrfFinder PARAMS
O_STRING_LEN = 300  # length of the genome
O_TEST_NUM = 200  # number of tests per genome
O_DATABASE_NUM = 100  # number of genomes to test
O_INV_HAS_ADFIX_CHANCE = 10  # 1/chance that adfix isnt guaranteed to be in genome.
O_ADFIX_SCALING = 4  # exponential scaling applied to adfix length to make adfixes more likely to be shorter.

class TestAssignment3(unittest.TestCase):
    @staticmethod
    def listFailures(failures, test_num):
        if len(failures):
            print('\n The following failures arose:\n', *failures)
            raise AssertionError(f" - {len(failures)} failures out of {test_num} tests.")
# THIS ONE PASSES
    def testEdgeCases(self):
        print("\nTest Edge Cases", end="")
        failures = []
        SequenceDatabase
        db = SequenceDatabase()
        tests = [
            [SequenceDatabase().query(""), None],  # empty database, empty query
            [SequenceDatabase().query("A"), None],  # empty database, non-empty query
            [SequenceDatabase().query("D"), None],  # empty databse, non-empty query
            [db.addSequence("A"), None],  # single letter database queries
            [db.query("A"), "A"],         #  |
            [db.query("B"), None],        #  |
            [db.query("C"), None],        #  |
            [db.query("D"), None] ,       #  |
            [db.addSequence("AA"), None],    # Prefixed database queries
            [db.addSequence("AAA"), None],   # |
            [db.addSequence("AAAA"), None],  # |
            [db.query("A"), "A"] ,           # |
            [db.query("AA"), "AA"] ,         # |
            [db.addSequence("AAA"), None],   # |
            [db.query("A"), "AAA"]           # |
        ]
        for t in tests:
            try:
                self.assertEqual(t[0], t[1])
            except AssertionError as e:
                failures.append(str(e))

        # OrfFinder
        genome1 = OrfFinder("AAAAA")
        tests = [
            # [OrfFinder("A").find("A", "A"), []],  # single letter genome has no adfixes
            # [OrfFinder("AA").find("A", "A"), ["AA"]],  # len(genome) = len(start) + len(end) = 0 or 1 prefixes
            [genome1.find("A", "A"), ["A"*i for i in range(2, 6) for _ in range(6-i)]],  # single repeating letter genome has N^2 adfixes
            [genome1.find("A", "B"), []],  # no adfixes if start or end not in genome
            [genome1.find("A", "C"), []],  # no adfixes if start or end not in genome
            [genome1.find("A", "D"), []],  # no adfixes if start or end not in genome
            [genome1.find("B", "B"), []],  # no adfixes if start or end not in genome
            [genome1.find("C", "B"), []],  # no adfixes if start or end not in genome
        ]
        for t in tests:
            try:
                self.assertEqual(sorted(t[0]), sorted(t[1]))
            except AssertionError as e:
                failures.append(str(e))

        self.listFailures(failures, 15 + 8)
# This one also passes
    def testGivenTests(self):
        print("\nTest Provided Tests", end="")
        failures = []
        SequenceDatabase
        db = SequenceDatabase()
        tests = [
            [db.addSequence("ABCD"), None],
            [db.addSequence("ABC"), None],
            [db.addSequence("ABC"), None],
            [db.query("A"), "ABC"],
            [db.addSequence("ABCD"), None],
            [db.query("A"), "ABC", None],
            [db.addSequence("ABCD"), None],
            [db.query(""), "ABCD"],
            [db.query("A"), "ABCD"],
            [db.query("B"), None],
        ]
        for t in tests:
            try:
                self.assertEqual(t[0], t[1])
            except AssertionError as e:
                failures.append(str(e))

        # OrfFinder
        genome1 = OrfFinder("AAABBBCCC")
        tests = [
            ["AAA", "BB", ["AAABB", "AAABBB"]],
            ["BB", "A", []],
            ["AA", "BC", ["AABBBC", "AAABBBC"]],
            ["A", "B", ["AAAB", "AAABB", "AAABBB", "AAB", "AABB", "AABBB", "AB", "ABB", "ABBB"]],
            ["AA", "A", ["AAA"]],
            ["AAAB", "BBB", []],
            ["AB", "C", ["ABBBC", "ABBBCC", "ABBBCCC"]],
            ["BC", "C", ["BCCC", "BCC"]],
            ["AC", "C", []],
            ["A", "CB", []]
        ]
        for t in tests:
            try:
                self.assertEqual(sorted(genome1.find(t[0], t[1])), sorted(t[2]))
            except AssertionError as e:
                failures.append(str(e))

        self.listFailures(failures, 20)

    # def testSequenceDatabase(self):
    #     print()
    #     STRING_LEN = S_STRING_LEN  # the maximum length of string to insert (4^STRING_LEN should be ~TEST_NUM for good tests)
    #     TEST_NUM = S_TEST_NUM  # the number of tests to run per database
    #     DATABASE_NUM = S_DATABASE_NUM  # the number of databases to test
    #     failures = []
    #     for d in range(DATABASE_NUM):
    #         print("\rTest SequenceDatabase -", d+1, "/", DATABASE_NUM, end="")
    #
    #         db = SequenceDatabase()
    #         strings = []
    #         for _ in range(TEST_NUM):
    #             strings.append("".join(rd.choices("ABCD", k=rd.randint(1, STRING_LEN))))
    #             s = "".join(rd.choices("ABCD", k=rd.randint(0, len(strings[-1]))))
    #             db.addSequence(strings[-1])
    #             print("added: " + strings[-1])
    #             try:
    #                 self.assertEqual(db.query(s), min(st.multimode(max([x for x in strings if x.startswith(s)], [None], key=lambda x: len(x)))))
    #             except AssertionError as e:
    #                 print("query: " + s)
    #                 print("i get query: " + db.query(s))
    #                 failures.append("\n\n\nLast Added String: " + strings[-1] + "\nQueried String: " + s + " \n" + str(e))
    #     self.listFailures(failures, DATABASE_NUM*TEST_NUM)

    def testOrfFinder(self):
        print()
        STRING_LEN = O_STRING_LEN  # length of the genome
        TEST_NUM = O_TEST_NUM  # number of tests per genome
        DATABASE_NUM = O_DATABASE_NUM  # number of genomes to test
        INV_HAS_ADFIX_CHANCE = O_INV_HAS_ADFIX_CHANCE  # 1/chance that adfix isnt guaranteed to be in genome.
        ADFIX_SCALING = O_ADFIX_SCALING  # exponential scaling applied to adfix length to make adfixes more likely to be shorter.
        failures = []
        for d in range(DATABASE_NUM):
            print("\rTest OrfFinder -", d+1, "/", DATABASE_NUM, end="")
            genome_string = "".join(rd.choices("ABCD", k=rd.randint(1, STRING_LEN)))
            s_len = len(genome_string) - 1
            genome = OrfFinder(genome_string)
            for _ in range(TEST_NUM):
                if rd.randint(0, INV_HAS_ADFIX_CHANCE) < INV_HAS_ADFIX_CHANCE:
                    # there is at least one of the adfix in genome
                    mid = min(rd.randint(2, max(s_len-2, 2)), s_len)
                    left = rd.randint(1, max(mid - 1, 1))
                    right = rd.randint(mid, max(s_len-1, mid))
                    pre = genome_string[rd.randint(0, max(left - 1, 0)):left]
                    post = genome_string[rd.randint(right, max(s_len - 1, right)):s_len]
                else:
                    # there may or may not be the adfix in genome
                    pre = "".join(rd.choices("ABCD", k=int((rd.randint(1, STRING_LEN)/STRING_LEN)**ADFIX_SCALING)))
                    post = "".join(rd.choices("ABCD", k=int((rd.randint(1, STRING_LEN)/STRING_LEN)**ADFIX_SCALING)))

                # ensure adfixes arent empty
                pre = rd.choice("ABCD") if not pre else pre
                post = rd.choice("ABCD") if not post else post

                # do the test
                try:
                    self.assertEqual(sorted(genome.find(pre, post)), sorted([genome_string[x:i] for x in [i for i in range(s_len) if genome_string.startswith(pre, i, s_len + 1)] for i in range(x + len(pre) + len(post), s_len + 2) if genome_string.endswith(post, x, i)]))
                except AssertionError as e:
                    failures.append("\n\n\n" + genome_string + "  -  " + pre + "  :  " + post + " \n" + str(e))
        # output failures, if any
        self.listFailures(failures, DATABASE_NUM*TEST_NUM)


if __name__ == "__main__":
    rd.seed()
    unittest.main()
