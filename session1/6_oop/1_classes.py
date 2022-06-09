"""
start with a simple class and add methods and attributes
class vs instance, what is cls vs self
class methods, static methods, instance methods, properties
class attributes, instance attributes, constants

Inheritance vs composition when to choose which one?
"""
from typing import Final


class DataProcessor:
    def process_data(self):
        pass


class MyMainClass:

    def __init__(self, data_processor):
        self.data_processor = data_processor

    def my_method(self):
        data = self.data_processor.process_data()


class Animal:
    def __init__(self, a):
        self.a = a


class Horse(Animal):
    c = 3
    PI: Final = 3.14

    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def my_custom_method(self, a, b, c):
        pass

    @classmethod
    def my_class_method(cls):
        pass

    @staticmethod
    def my_static_method(a, b, c):
        pass

    @property
    def c(self):
        return (self.a + self.b) * Horse.PI
