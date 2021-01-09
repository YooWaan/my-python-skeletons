"""
copy right

"""

from dataclasses import dataclass
from typing import Protocol, TypeVar, Generic


MyH = TypeVar("MyH")


@dataclass
class Hello(Generic[MyH]):
    value: MyH


class MyValue(Protocol):
    """ MyValue """

    def value(self) -> str:
        ...


class VStr:
    def __init__(self, v: str):
        self._value = Hello[str](v)

    def value(self) -> str:
        return self._value.value


class VInt:
    def __init__(self, v: int):
        self._value = Hello[int](v)

    def value(self) -> str:
        return f"{self._value.value}"
