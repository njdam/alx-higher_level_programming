# Python - Everything is object

In Python, everything is considered an object. This means that every entity in Python, whether it's a number, string, function, or even a module, is an object with its own type and associated attributes and methods. This object-oriented nature is one of the key features of Python.

## ADVANCED Tasks

[33. int 3/3 /105-line1.txt](https://chat.openai.com/)

In CPython, small integers ranging from `-5` to `256` are pre-allocated and cached for performance reasons. These integers are stored in an array called `small_ints`, and their references are reused throughout the execution of a program. The constants `NSMALLPOSINTS` and `NSMALLNEGINTS` represent the number of pre-allocated small positive and negative integers, respectively.

In CPython, the pre-allocated small integers are stored in an array called `small_ints`. The size of this array is determined by the constants `NSMALLPOSINTS` and `NSMALLNEGINTS`, which represent the number of pre-allocated small positive and negative integers, respectively.

The total pre-allocated memory size for small integers can be calculated as follows:
```
import sys

small_ints_size = sys.getsizeof(int()) * (sys.getsizeof(small_ints) - sys.getsizeof([]))
```

However, it's important to note that the size calculation above doesn't include the memory overhead of the array itself, and it assumes that all small integer slots are utilized.

The actual pre-allocated memory size for small integers depends on the Python implementation and version. In CPython 3.x, the default values are typically:

`NSMALLPOSINTS`: 257
`NSMALLNEGINTS`: 5
Using these default values, the pre-allocated memory size for small integers would be approximately:
```
import sys

small_ints_size = sys.getsizeof(int()) * (sys.getsizeof(range(-5, 257)) - sys.getsizeof([]))
```

Result found by as follows:
```
>>> num = small_ints
>>> print(num)
262  # 5 negative integers + zero (as 1 integer) + 256 positive integers
```
