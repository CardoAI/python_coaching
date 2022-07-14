"""
try, except
try, except, finally
how to write custom exceptions
dont catch all exceptions
dont pass silently
"""
import logging

logger = logging.getLogger(__name__)

try:
    a = 1
    b = 0
    c = a / b

except ZeroDivisionError as e:
    c = 0


finally:
    logger.info('this code has been executed')


class BaseException(Exception):
    pass


class MyCustomError(BaseException):

    def __init__(self, message=None) -> None:
        self.message = message or 'My custom error'
