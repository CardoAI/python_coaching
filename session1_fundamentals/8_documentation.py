"""
comments are a way of documenting as well but they should be used sparingly
because a good code should be able to explain itself.

docstrings:
- module level docstring
- class level docstring
- function level docstring
- method level docstring

README for repository

read the docs:
 - markdown
 - reStructuredText
 - epydoc
 - sphinx
"""


class A:
    """

    """


def main(a, b, c):
    """
    >>> main(1, 2, 3)
    6

    Describe the function.
    Args:
        a:
        b:
        c:

    Returns:

    """
    return a + b + c
