"""
 copy right
"""
from .hello import MyValue


def pair(a: MyValue, b: MyValue) -> str:
    # pylint: disable=invalid-name,missing-function-docstring
    return a.value() + b.value()
