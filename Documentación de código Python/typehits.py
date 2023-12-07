'''
Type Hints
'''

class Person:
    first_name: str =  "john"
    last_name: str = "Does"
    age: int = 31

def headLine(text: str, aling: bool = True) -> str:
    pass

from typing import List

def average(numbers: List[float]) -> float:
    """Calculate the average value from a list of numbers"""
    if not numbers:
        # we must have values for this operation
        raise ValueError("Numbers can not be empty")
    return sum(numbers) / len(numbers)

