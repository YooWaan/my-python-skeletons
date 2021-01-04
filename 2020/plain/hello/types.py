from typing import NewType

from .hello import MyABC


Val = NewType('Val', MyABC)
