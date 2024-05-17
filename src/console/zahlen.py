import re
from . import Console

from zahlen.stat import ss, corelation, determinate

class Export:
    @staticmethod
    def setup(console: Console):
        StatisticCommands.setup(console)

class StatisticCommands:
    @staticmethod
    def setup(console: Console):
        console.register("ss", StatisticCommands.ss_, "Get the sum of squares between x & y")
        console.register("cor", StatisticCommands.cor_, "Get the corelation between x & y")
        console.register("det", StatisticCommands.det_, "Get the determinate between x & y")

    @staticmethod
    def ss_(*args):
        x = tuple(map(int, input("x> ").split(" ")))
        y = tuple(map(int, input("y> ").split(" ")))

        result = ss(x, y)

        if result.err:
            print(result.err)
            return

        print(result.ok)

    @staticmethod
    def cor_(*args):
        x = tuple(map(int, input("x> ").split(" ")))
        y = tuple(map(int, input("y> ").split(" ")))

        result = corelation(x, y)

        if result.err:
            print(result.err)
            return

        print(result.ok)

    @staticmethod
    def det_(*args):
        x = tuple(map(int, input("x> ").split(" ")))
        y = tuple(map(int, input("y> ").split(" ")))

        result = determinate(x, y)

        if result.err:
            print(result.err)
            return

        print(result.ok)