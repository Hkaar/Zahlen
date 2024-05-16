import math
import time

from typing import Any, Collection, Tuple, Union
from dataclasses import dataclass, field

@dataclass(frozen=True)
class SumOfSquaresResult:
    """A class to represent the result of the 'ss' function"""

    sum_x: Union[int, float] = 0
    sum_y: Union[int, float] = 0
    n: int = 0
    xy: Tuple[Union[int, float], ...] = field(default_factory=tuple)
    x2: Tuple[Union[int, float], ...] = field(default_factory=tuple)
    y2: Tuple[Union[int, float], ...] = field(default_factory=tuple)
    sum_xy: Union[int, float] = 0
    sum_x2: Union[int, float] = 0
    sum_y2: Union[int, float] = 0
    ss_xy: Union[int, float] = 0
    ss_x2: Union[int, float] = 0
    ss_y2: Union[int, float] = 0

    def __iter__(self):
        for val in self.__dataclass_fields__.keys():
            yield getattr(self, val)

def ss(x: Collection[int|float], y: Collection[int|float]) -> SumOfSquaresResult:
    if not isinstance(x, Collection) or not isinstance(y, Collection):
        raise TypeError("x, y mus be a iterable!")
    
    if len(x) != len(y):
        raise ValueError("X and Y must be of the same length!")
    
    sum_x = sum(x)
    sum_y = sum(y)
    n = len(x)

    xy = tuple(xi*yi for xi, yi in zip(x, y))
    x2 = tuple(xi**2 for xi in x)
    y2 = tuple(yi**2 for yi in y)

    sum_xy = sum(xy)
    sum_x2 = sum(x2)
    sum_y2 = sum(y2)

    ss_xy = sum_xy - ((sum_x * sum_y)/n)
    ss_x2 = sum_x2 - ((sum_x**2)/n)
    ss_y2 = sum_y2 - ((sum_y**2)/n)

    return SumOfSquaresResult(
        n = n, sum_x = sum_x, sum_y = sum_y,
        xy = xy, x2 = x2, y2 = y2,
        sum_xy = sum_xy, sum_x2 = sum_x2, sum_y2 = sum_y2,
        ss_xy = ss_xy, ss_x2 = ss_x2, ss_y2 = ss_y2
    )

def corelation(x: Collection[int|float], y: Collection[int|float]) -> int|float:
    xy, x2, y2 = ss(x, y)

    result = xy/math.sqrt((x2*y2))
    return result

def determinate(x: Collection[int|float], y: Collection[int|float]) -> int|float:
    xy, x2, y2 = ss(x, y)

    result = (xy**2)/(x2*y2)
    return result

if __name__ == "__main__":
    x = [5, 10, 11, 7]
    y = [11, 4, 11, 6]

    start = time.time()
    n = ss(x, y)