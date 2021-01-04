"""
 copy right
"""
from typing import Type
from .hello import MyABC


def c_abc(a: MyABC, b: MyABC) -> str:
    # pylint: disable=invalid-name,missing-function-docstring
    return a.value() + b.value()


def c_type(a: Type[MyABC], b: Type[MyABC]) -> str:
    return a.value() + b.value()
