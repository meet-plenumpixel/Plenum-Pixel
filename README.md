# Python

## Variables

- ### Type Casting

  - **Implicit Type Casting**\
    type casting can be done with operation

  - **Explicit Type Casting**\
    type casting can be done with data type function

- ### Variable scopes
    
  - **L**ocal | **E**nclosing | **G**lobal | **B**uilt-in (LEGB)

## Data Types

- **Text Type**: str

- **Numeric Types**: int, float, complex

- **Sequence Types**: list, tuple, range

- **Mapping Type**: dict

- **Set Types**: set, frozenset
   
  **set VS frozenset**:

  In Python, frozenset is the same as set except the **frozensets are immutable** which means that elements from the **frozenset cannot be added or removed once created.** This function takes input as any iterable object and converts them into an immutable object. The order of elements is not guaranteed to be preserved.

- **Boolean Type**: bool

- **Binary Types**: bytes, bytearray, memoryview

  ```
  x = b"Hello"
  print(x)        # b'Hello'
  print(type(x))  # <class 'bytes'>

  y = bytearray(5)
  print(y)        # bytearray(b'\x00\x00\x00\x00\x00')
  print(type(y))  # <class 'bytearray'>

  z = memoryview(bytes(5))
  print(z)        # bytearray(b'\x00\x00\x00\x00\x00')
  print(type(z))  # <class 'bytearray'>

  ```


## String Formatting
- [Python String Formatting Best Practices](https://realpython.com/python-string-formatting/)
- [Python 3's f-Strings: An Improved String Formatting Syntax (Guide)](https://realpython.com/python-f-strings/)
- [escape-sequences](https://www.python-ds.com/python-3-escape-sequences)
- [string-operators](https://www.python-ds.com/python-3-string-operators)
- [string-methods](https://www.python-ds.com/python-3-string-methods)


## Types of Arguments
- [5 Types of Arguments in Python Function Definitions](https://levelup.gitconnected.com/5-types-of-arguments-in-python-function-definition-e0e2a2cafd29)


## Class and object

- \_\_init\_\_ vs \_\_new\_\_
- \_\_str\_\_ vs \_\_repr\_\_
- [Iterators vs Iterables]()
- [Mutable Default Arguments in Python](https://betterprogramming.pub/mutable-default-arguments-in-python-643ae2583e00)


## Method Resolution Order (MRO)

Method resolution order(MRO) in both the declaration style is different. Old style (<python2.3) classes use **DLR or depth-first left to right algorithm** whereas new style (python 3.x) classes use **C3 Linearization algorithm** for method resolution while doing multiple inheritances.


  - [The Python 2.3 Method Resolution Order](https://www.python.org/download/releases/2.3/mro/)
  - [Method Resolution Order in Python 3](https://medium.com/@__hungrywolf/mro-in-python-3-e2bcd2bd6851)


## Lazy loading 
