# hash-table-implementation


Why hello there! You might be wondering what this is. If the name of the repository did not clue you in, this is a hash table 
implementation. You see, I determined there were not enough half-abandoned repos floating around with various self-rolled implementations of hash tables of hash tables, so I decided to throw my own into the fray, fun!



## We get it, this is a hash table, how do I use it? 

Well, eager reader, let me shed some light there. The core code is in a file called ```ht.py```. To use the table, just import!

```from ht import HashTable```

Please note, hash table was designed for use with ***python 3!***

### End-User Methods
```table = HashTable()```

```1. table.get(key)```  Returns the value mapped to the key. Raises a KeyError if not present.

```2. table.set(key, value)```  Maps specific key to specific value in the hash table.

```3. table.delete(key)``` Deletes the key/value pair in the hash table. Raises a KeyError if not present.
### Tests
```
  "I confess I confess, writing documentation is not always the best. 
  But now it's time for the hash table tests!" - Engineer
```
You can run ```python3 test.py``` file for unit tests. No external dependencies needed. 

