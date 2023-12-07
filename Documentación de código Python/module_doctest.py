'''
Doctest
'''

def divide(a, b):
    """Compute and return the division of two numbers
    
    Usage examples:
    >>> divide(84, 2)
    42.0
    >>> divide(15, 3)
    5.0
    >>> divide(42, -2)
    -21.0

    >>> divide(42, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return float(a / b)

def add(a, b):
    """
    This function calculate the sum of two values


    Usage examples:
    >>> add(8, 450)
    458.0
    >>> add(8, -666.6)
    -658.6
    >>> add()
    Traceback (most recent call last):
        ...
    TypeError: add() missing 3 requiered arguments: 'a' and 'b'

    """
    return float(a + b)


from collections import deque

class Queue:
    def __init__(self):
        """Define le atributo protegido"""
        self._elements = deque()

    
    def enqueue(self, element):
        """Add items to the right end of the queue.

        >>> numbers = Queue()
        >>> numbers
        Queue([])

        >>> for number in range(1, 4):
        ...     numbers.enqueue(number)

        >>> numbers
        Queue([1, 2, 3])
        """
        self._elements.append(element)


    def dequeue(self):
        """Remove and return an item from the left end of the queue

        >>> numbers = Queue()
        >>> for number in range(1, 4):
        ...     numbers.enqueue(number)
        >>> numbers
        Queue([1, 2, 3])

        >>> numbers.dequeue()
        1
        >>> numbers.dequeue()
        2
        >>> numbers.dequeue()
        3
        >>> numbers
        Queue([]) 
        """
        return self._elements.popleft()
    
    def __repr__(self):
        return f"{type(self).__name__}({list(self._elements)})"