"""
Explain the use case when to use a dataclass.
Implement a data class.
Explain that a dataclass is just a class after all.
"""
from dataclasses import dataclass


def decorator_to_do_something(func):
    def wrapper():
        # do something
        func()

    return wrapper


@decorator_to_do_something
def main1():
    pass


@decorator_to_do_something
def main2():
    pass


@decorator_to_do_something
def main3():
    pass


@dataclass
class A:
    a: int
    b: str
    c: dict
    d: bool
