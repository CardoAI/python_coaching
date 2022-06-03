"""
abs, min, max, sum, len, sorted, reversed, enumerate, zip, any, all
breakpoint, getattr, setattr, hasattr, delattr, isinstance, issubclass
input, next, open, pow, print, range, round
functools.partial

conversion functions: int(), float(), str(), bool(), tuple(), type()
"""

# open a file manually and close it when you are done
f = open('/etc/passwd')
print(f.read())
f.close()

# open a file using `with` statement, it will automatically close the file
with open('/etc/passwd') as f:
    print(f.read())

# iterate in reverse order with a step of -2
for i in range(10, 1, -2):
    print(i)

# when checking for truthiness, keep in mind that 0 is False,
# if you check for variable a with 'if a' you will get a false value
a = 0
if a is not None:
    print('a is not none')

t = type(a)  # type of a, int

a = abs(-1)  # 1
m = min(1, 2, 3)  # 1
M = max(1, 2, 3)  # 3
s = sum([1, 2, 3])  # 6
l = len([1, 2, 3])  # 3  BigO(1)
sorted_list = sorted([3, 2, 1])  # [1, 2, 3]
reverse_sorted_list = sorted([1, 2, 1], reverse=True)  # [1, 1, 2]
reversed_list = reversed([1, 2, 3])  # [3, 2, 1]

# if you want both the index and the value, use enumerate
l = [1, 2, 3]
for index, item in enumerate(l):
    print(index, item)

# if you want to iterate through multiple lists at the same time, use zip
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
for i in range(len(a)):
    x = a[i]
    y = b[i]
    z = c[i]

for x, y, z in zip(a, b, c, strict=True):
    print(x, y, z)

any([True, False, False])  # True
any([False, False, False])  # False

all([True, True, True])  # True
all([True, True, False])  # False
