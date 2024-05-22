import math
import time

from .defs import Result, SumOfSquares
from typing import Collection

def ss(x: Collection[int|float], y: Collection[int|float]) -> Result[SumOfSquares]:
    if not isinstance(x, Collection) or not isinstance(y, Collection):
        return Result(err=TypeError("x, y mus be a iterable!"))
    
    if len(x) <= 1 and len(y) <= 1:
        return Result(err=ValueError("X and Y must be atleast 2 elements long!"))
    
    if len(x) != len(y):
        return Result(err=ValueError("X and Y must be of the same length!")) 
    
    sum_x = sum(x)
    sum_y = sum(y)
    n = len(x)

    average_x = sum_x/n
    average_y = sum_y/n

    xy = tuple(xi*yi for xi, yi in zip(x, y))
    x2 = tuple(xi**2 for xi in x)
    y2 = tuple(yi**2 for yi in y)

    sum_xy = sum(xy)
    sum_x2 = sum(x2)
    sum_y2 = sum(y2)

    ss_xy = sum_xy - ((sum_x * sum_y)/n)
    ss_x2 = sum_x2 - ((sum_x**2)/n)
    ss_y2 = sum_y2 - ((sum_y**2)/n)

    return Result(SumOfSquares(
        sum_x, sum_y, n, average_x, average_y, xy, x2, y2, sum_xy, sum_x2, sum_y2, ss_xy, ss_x2, ss_y2
    ))

def corelation(x: Collection[int|float], y: Collection[int|float]) -> Result[int|float]:
    base = ss(x, y)

    if not base.ok:
        return Result(err=base.err)
    
    xy = base.ok.ss_xy
    x2 = base.ok.ss_x2
    y2 = base.ok.ss_y2

    result = xy/math.sqrt((x2*y2))
    return Result(result)

def determinate(x: Collection[int|float], y: Collection[int|float]) -> Result[int|float]:
    base = ss(x, y)

    if not base.ok:
        return Result(err=base.err)
    
    xy = base.ok.ss_xy
    x2 = base.ok.ss_x2
    y2 = base.ok.ss_y2

    result = (xy**2)/(x2*y2)
    return Result(result)

if __name__ == "__main__":
    x = [5, 10, 11, 7]
    y = [11, 4, 11, 6]

    start = time.time()
    n = ss(x, y)

    print(corelation(x, y))

    print(determinate(x, y))

    print(time.time() - start)