## Things Learned
* xrange() - xrange() functions returns an xrange object that evaluates lazily. That means xrange only stores the range arguments and generates the numbers on demand. It doesn’t generate all numbers at once like range(). Furthermore, this object only supports indexing, iteration, and the len() function.

* dict.popitem() - The popitem() returns and removes an arbitrary element (key, value) pair from the dictionary. The popitem()

    * returns an arbitrary element (key, value) pair from the dictionary
    * removes an arbitrary element (the same element which is returned) from the dictionary.

* dict.pop() - The pop() method removes and returns an element from a dictionary having the given key.
    * The pop() method takes two parameters:

        * key - key which is to be searched for removal
        * default - value which is to be returned when the key is not in the dictionary
    
    * The pop() method returns:

        * If key is found - removed/popped element from the dictionary
        * If key is not found - value specified as the second argument (default)
        * If key is not found and default argument is not specified - KeyError exception is raised