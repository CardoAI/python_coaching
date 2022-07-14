"""
Video Tutorial: https://www.youtube.com/watch?v=QVdf0LgmICw
Article:        https://realpython.com/python-scope-legb-rule/#discovering-unusual-python-scopes

LEGB Rule:
L - Local
E - Enclosing
G - Global
B - Built-in
"""
from typing import Final

MY_CONSTANT: Final = 'global constant'

x = 'global x'

min([1, 2, 3])


def min():
    x = 'local x'
    print(x)


def main():
    min([1, 2, 3])
    x = 'local x'
    print(x)


print('before main', x)
main()
print('after main', x)
