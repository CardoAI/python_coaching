"""
__str__, __repr__, __len__, __iter__, __next__
__getitem__, __setitem__, __delitem__
__lt__, __le__, __eq__, __ne__, __gt__, __ge__
"""
from datetime import datetime


class A:

    def __str__(self):
        return 'thats my custom str method'


a = A()
print(str(a))

l = list([1, 2, 3])
len(l)

d = dict(a=1, b=2)
d['a']

a = 1
b = 2


class A:
    a: int
    b: str
    date_added: datetime

    def __lt__(self, other):
        return self.date_added < other.date_added
