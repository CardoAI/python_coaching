"""
Video Tutorial: https://www.youtube.com/watch?v=p9ppfvHv2Us
common mistakes with default values
tuple vs list
"""

# strings are immutable
name = "John Doe"
print(name[0])
name[0] = 'H'  # raises TypeError


# lists are mutable
colors = ['blue', 'green', 'red', 'yellow']
colors.pop()
print(colors)
new_colors = colors
new_colors.pop()
print(new_colors)
print(colors)


# tuples are immutable
colors = ('blue', 'green', 'red', 'yellow')
new_colors = colors
del new_colors
print(colors)  # the original tuple is not affected


# sets are mutable
colors = {'blue', 'green', 'red', 'yellow'}
colors.pop()
print(colors)


# dicts are mutable
person = {
    'height': 1.60,
    'weight': '50kg',
    'age': 21
}
person.pop('weight')
print(person)


# for mutable data structures, use the copy() when you want a copy of the original,
# but you do not want the changes to be reflected
list_a = [1, 2, 3]
list_b = list_a.copy()
list_b.pop()
print(list_a)


# Mutable defaults (anti pattern)
def create_or_append(value, list_=[]):
    list_.append(value)
    return list_


colors = ['blue', 'green', 'red', 'yellow']
new_list = create_or_append('purple', colors)
print(new_list)

# but the problem with defaults starts when calling it without the default arg
second_list = create_or_append('grey')
print(second_list)  # list with one element, as expected
third_list = create_or_append('orange')
print(third_list)


# the solution
def create_or_append(value, list_=None):
    if list_ is None:
        list_ = []
    list_.append(value)
    return list_
