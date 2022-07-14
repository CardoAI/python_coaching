"""
The concept of Interface is to define the methods that are required to be
implemented by the subclasses.

How to implement an abstract class?
"""
from abc import ABC, abstractmethod


class Database(ABC):

    @abstractmethod
    def query(self, sql) -> list:
        raise NotImplementedError()


class MySQL(Database):

    def query(self, sql):
        print("MySQL query")


class Postgres(Database):

    def query(self, sql):
        print("POSTGRES query")


def main(db: Database):
    result = db.query(sql="SELECT * FROM users")


main(db=MySQL())
main(db=Postgres())d


class MyAbstractClass(ABC):

    @abstractmethod
    def my_abstract_method(self):
        raise NotImplementedError()
