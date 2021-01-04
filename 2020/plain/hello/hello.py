"""
copy right

"""
from abc import ABC, abstractmethod

"""
"""
class MyABC(ABC):
    def __init__(self):
        pass

    """
    """
    @abstractmethod
    def value(self) -> str:
        pass


class Value(MyABC):
    def __init__(self, v: str):
        super().__init__()
        self._value = v

    def value(self) -> str:
        return self._value


class VInt(MyABC):
    def __init__(self, v: int):
        super().__init__()
        self._value = v

    def value(self) -> str:
        return f"{self._value}"


print("aaaaa")

V = Value("aaa")

print(V.value())
