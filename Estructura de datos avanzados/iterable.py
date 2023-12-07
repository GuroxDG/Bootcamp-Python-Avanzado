'''
Iterable
'''

class Iterable:
    def __init__(self, sequence = []):
        self._item = sequence

    def __iter__(self):
        return iter(self._item)