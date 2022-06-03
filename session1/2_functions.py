"""
 - returning values from functions
    - return single value
    - return multiple values
    - base return
    - return None
    - no return statement

 - what are args and kwargs?
 - single responsibility principle
 - lambda functions
"""


def get_personal_info():
    name_ = input("Please enter your name ")
    age_ = int(input("Please enter your age "))
    return name_, age_


name, age = get_personal_info()
print(name, age)


def my_func():
    # statement 1
    if "condition":
        return None  # function is supposed to return, but not on this path
    # statement 2
    return  # early exit, sort of break statement
    # statement 3


# Tuple unpacking
info = ("John Doe", "35", "Male")
name, age, gender = info
print(name, age, gender)


def get_full_name(f_name, l_name):
    print(f_name, l_name)


# keyword arguments allow us to change order
get_full_name(l_name="Doe", f_name="Joe")


# Arbitrary number of normal and keyword arguments
def print_values(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key}-{value}')


print_values(1)
print_values(1, 2, 3, 4, 5, name="John", age="35")

"""
SRP (Single Responsibility Principle) states that a function or class
should have only one responsibility (i.e. should only do one thing),
and as a result, one reason to change.

Adopting it makes for code that is easier to read, understand, debug
and reuse. Common red flags of violating SRP are:

- functions taking many arguments, especially booleans like this:
    my_func(34, my_df, False, True, False, False, True)
-functions spreading over many lines of code (50+)
-functions that carry around a lot of state (should be a class instead)
"""

# Lambdas (anonymous functions)
square = lambda x: x ** 2  # don't assign them, use a proper function for that
print(square(7))


def raise_to_power(power):
    return lambda num: num ** power  # using lambdas inside traditional funcs


squared = raise_to_power(2)  # raise_to_power() used as a function generator
cubed = raise_to_power(3)

print(squared(3))
print(cubed(3))
