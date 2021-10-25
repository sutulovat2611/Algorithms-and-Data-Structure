# DNA_fragments.py:
## General idea: 
- There is a class _SeqeunceDatabase_, which represents the database. The database contains
numerous strings.
- SeqeunceDatabase has two methods: _addSequence(s)_ and _query(q)_, which are responsible 
for adding new sequence into the database and return the sequence in the database with q
as a prefix, with the highest frequency within the database among all the sequences with 
that prefix and if there are numerous sequences that suit these conditions, it should be 
lexicographically smallest of them.
## Input
* The input to _addSequence_ is a single nonempty string of uppercase letters in uppercase [A-D].
* The input to _query_ is a single (possibly empty) string of uppercase letters in uppercase [A-D].
## Output
- _addSequence(s)_: none
- _query(q)_: a string with the following properties:
  - has q as a prefix
  - has a higher frequency in the database than any other string with q as a prefix
  - if two or more strings with prefix q are tied for most frequent, return the lexicographically least of them
## Example
```python
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
 ```
### Time Complexity
- _init_ method of SequenceDatabase is O(1)
- _addSequence(s)_ is O(len(s))
- _query(q)_ is O(len(q))
    
# orf_finder.py:
## General idea: 
There is a class _OrfFinder_, which has a method _find(start, end)_, which finds all sections 
of a genome which start with a given sequence of characters (start), and end with a (possibly) 
different given sequence of characters (end).
## Input
- genome is a single non-empty string consisting only of uppercase [A-D]. 
  - genome is passed as an 
argument to the __init__ method of OrfFinder (i.e. it gets used when creating an instance of the class).
- start and end are each a single non-empty string consisting of only uppercase [A-D].
## Output
- _find()_ returns a list of strings, which contains all the substrings of genome which have start
as a prefix and end as a suffix
## Example
```python
    genome1 = OrfFinder("AAABBBCCC")
    genome1.find("AAA","BB")
    >>> ["AAABB","AAABBB"]
    genome1.find("BB","A")
    >>>[]
    genome1.find("AA","BC")
    >>>["AABBC","AAABBBC"]
    genome1.find("A","B")
    >>> ["AAAB","AAABB","AAABBB","AAB","AABB","AABBB","AB","ABB","ABBB"]
 ```
### Time Complexity
- _init_ method of _OrfFinder_ runs in O(N^2) time, where N is the length of genome.
- _find_ runs in (len(start) + len(end) + U) time, where U is the number of characters in the output list.
