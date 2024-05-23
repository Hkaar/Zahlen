# Basic commands for the zahlen console
# Author : Hkaar

import os

from .defs import ConsoleInterface

__export__ = [
    "Commands"
]

class Commands:
    @staticmethod
    def setup(console: ConsoleInterface):
        console.register("clear", Commands.clear)
        console.register("help", Commands.help)
        console.register("exit", Commands.exit)

    @staticmethod
    def clear(*args):
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
    
    @staticmethod
    def help(*args):
        args[0]._parser.print_help()

    @staticmethod
    def exit(*args):
        args[0].shell_active = False