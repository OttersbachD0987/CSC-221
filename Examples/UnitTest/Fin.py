from unittest import TestCase
import unittest
import doctest

class ATest(TestCase):
    ...

def foobar() -> int:
    """Thing.
    
    >>> print(foobar())
    1
    
    """
    return 1

if __name__ == "__main__":
    #unittest.main()
    doctest.testmod()
