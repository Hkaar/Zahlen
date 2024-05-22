# Type definitions for zahlen
# Author : Hkaar

from dataclasses import dataclass, field
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

@dataclass(frozen=True)
class Result(Generic[T]):
    """A class to represent the result of a process"""
    
    ok: Optional[T] = None
    err: Optional[BaseException] = None

@dataclass(frozen=True)
class SumOfSquares:
    """A class to represent the result of the 'ss' function"""

    sum_x: int|float = 0
    sum_y: int|float = 0
    n: int = 0
    average_x: int|float = 0
    average_y: int|float = 0
    xy: tuple[int|float, ...] = field(default_factory=tuple)
    x2: tuple[int|float, ...] = field(default_factory=tuple)
    y2: tuple[int|float, ...] = field(default_factory=tuple)
    sum_xy: int|float = 0
    sum_x2: int|float = 0
    sum_y2: int|float = 0
    ss_xy: int|float = 0
    ss_x2: int|float = 0
    ss_y2: int|float = 0

    def __iter__(self):
        for val in self.__dataclass_fields__.keys():
            yield getattr(self, val)