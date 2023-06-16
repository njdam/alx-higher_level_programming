# 0x04. Python - More Data Structures: Set, Dictionary

This project is for helping us as Alx Student to understand more about data structures and how to set and use dictionaries in Python, also and how lambda, map, and reduce is simple for simplifying function.

## Main functions to be used in this project

1. `set()`: is used to find and return unique values. eg:
```
lists = [1, 2, 1, 3, 2]
uniqlist = set(lists)  # result to [1, 2, 3]
```

2. `lambda`: is like def used to define a function in simple way, e.g:
```
sum = lambda x, y: x + y  # to work like add(a, b) function.
```

3. `map()`: is used to iterate elements in a list and present it to a function. eg:
```
# allows us to execute a function on each item in a list

lists = [1, 2, 3, 4, 5]  # or range(1, 6)
oddlist = list(map(lambda x: True if x % 2 != 0 else False, lists)
```

4. `filter()`: is a function to receive a list and return filtered list. eg:
```
list = [1, 2, 3, 4, 5]  # or range(1, 6)
oddlist = list(filter(lambda x: x % 2 != 0, list))  # filter will return only odd number.
```

5. `reduce()`: is a function to receive a list and return one result. eg:
```
from functools import reduce  # reduce imported from functools module

list = [1, 2, 3, 4, 5]  # or range(1, 6)
result = reduce(lambda x, y: x + y, list)  # result = 15
```

6. `lambda` in a dictionaries. eg:
```
attack = {'quick': (lambda: print("Quick Attack")),
           'power': (lambda: print("Power Attack")),
           'miss': (lambda: print("The Attack Missed"))}
				 
attack['quick']()  # This print "Quick Attack"

# You could get a random dictionary

import random

attackKey = random.choice(list(attack.keys()))
# where:
	# keys() returns an iterable so we convert it into a list
	# choice() picks a random value from that list

attack[attackKey]()  # this will print randomly according to called function in attack dictionary.
```

## MANDATORY

**3. Present in both: other option**
```
#!/usr/bin/python3
# A function to returns a set of common elements in two sets.


def common_elements(set_1, set_2):
	return (set_1 & set_2)
```

**4. Only differents**
```
Only print exclusive (^) elements in only one set of elements.
```

## ADVANCED

** 103-python.c **

***line 12***: `Py_ssize_t` is `Py_ssize_t`.

***line 22***: `((PyVarObject *)(p))->ob_size` to replace `PyBytes_Size(p)` for returning length or size of string (object) to be printed with it's bytes.

***line 24***: `((PyBytesObject *)p)->ob_sval` to replace `PyBytes_AsString(p) for returning a string (object) to be printed with it's bytes.`

***line 67***: `((PyListObject *)p)->ob_item[i]` to replace `PyList_GetItem(p, i);` for returning object item at index `i`.

***line 69***: `(object)->ob_type)->tp_name` to replace `Py_TYPE(object)->tp_name` for returning type name of object's item at index `i` to be printed with it's index `i`.

----------------------------------Thank You !!!----------------------------------

