1. DNA_fragments.py:
 General idea: 
    There is a class SeqeunceDatabase, which represents the database. The database contains numerous strings.
    SeqeunceDatabase has two methods, addSequence(s) and query(q), which are responsible for adding new sequence into the database 
    and return the sequence in the database with q as a prefix, with the highest frequency within the database among all the sequences with that prefix
    and if there are numerous sequences that suit these conditions, it should be lexicographically smallest of them.
 1.1 Input
    - The input to addSequence is a single nonempty string of uppercase letters in uppercase [A-D].
    - The input to query is a single (possibly empty) string of uppercase letters in uppercase [A-D].
 1.2 Output
    - addSequence(s): none
    - query(q) :a string with the following properties:
        -  has q as a prefix
        -  has a higher frequency in the database than any other string with q as a prefix
        -  if two or more strings with prefix q are tied for most frequent, return the lexicographically least of them
 1.3 Example
    db = SequenceDatabase()
    db.addSequence("ABCD")
    db.addSequence("ABC")
    db.addSequence("ABC")
    db.query("A")
    >>> "ABC"
    db.addSequence("ABCD")
    db.query("A")
    >>> "ABC"
    db.addSequence("ABCD")
    db.query("A")
1.4 Time Complexity
    - __init__ method of SequenceDatabase is O(1)
    - addSequence(s) is O(len(s))
    - query(q) is O(len(q))
    
2. orf_finder.py:
 General idea: 
 There is a class OrfFinder, which has a method find(start, end), which finds all sections of a genome which start with a given sequence of
 characters (start), and end with a (possibly) different given sequence of characters (end).
2.1 Input
    - genome is a single non-empty string consisting only of uppercase [A-D]. genome is passed as an
    argument to the __init__ method of OrfFinder (i.e. it gets used when creating an instance of the class).
    - start and end are each a single non-empty string consisting of only uppercase [A-D].
 2.2 Output
  - find() returns a list of strings, which contains all the substrings of genome which have start
    as a prefix and end as a suffix
 2.3 Example
    genome1 = OrfFinder("AAABBBCCC")
    genome1.find("AAA","BB")
    >>> ["AAABB","AAABBB"]
    genome1.find("BB","A")
    >>>[]
    genome1.find("AA","BC")
    >>>["AABBC","AAABBBC"]
    genome1.find("A","B")
    >>> ["AAAB","AAABB","AAABBB","AAB","AABB","AABBB","AB","ABB","ABBB"]
2.4  Time complexity: 
     - __init__ method of OrfFinder must run in O(N^2) time, where N is the length of genome.
     - find must run in (len(start) + len(end) + U) time, where U is the number of characters in the output list.
