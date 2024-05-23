# Core parts of the zahlen console
# Author : Hkaar

import importlib

from .defs import Result, ConsoleInterface

from typing import Callable, Dict, Optional
from argparse import ArgumentParser

class Console(ConsoleInterface):
    def __init__(self, **kwargs) -> None:
        self._parser = ArgumentParser(**kwargs)
        self._subparser = self._parser.add_subparsers(required=True)

        self._commands: Dict[str, Callable] = {}
        self.shell_active = False

        self._import(".commands", "src.console")

    def parse(self):
        """Execute the console command based on the given arguments"""

        args = self._parser.parse_args()
        args.func(args)

    def exec_(self, cmd: str, *args) -> Result[bool]:
        if cmd not in self._commands:
            return Result(err=ValueError(f"Command {cmd} does not exist!"))
        
        self._commands[cmd](*args)
        return Result(True)
    
    def register(self, name: str, handler: Callable, desc: Optional[str] = None) -> Result[ArgumentParser]:
        """Append a command to the specified subparser"""
        
        if name in self._commands:
            return Result(err=ValueError(f"{name} already exists as a command!"))

        subparser = self._subparser.add_parser(name, help=desc)
        subparser.set_defaults(func=handler)

        self._commands[name] = handler
        return Result(ok=subparser)
    
    def shell(self):
        self.shell_active = True

        while self.shell_active:
            user_cmd = input(">> ").strip().split(" ")

            if user_cmd[0] in self._commands:
                self.exec_(user_cmd[0], self, *user_cmd[1:])
                continue
            
            print(ValueError(f"Command {user_cmd[0]} does not exist!"))

    def _import(self, path: str, package: Optional[str] = None) -> Result[bool]:
        """Automatically import all the included commands within the given path"""

        if path.startswith("_"):
            return Result(err=ValueError("Invalid path!"))
        
        module = importlib.import_module(path, package)

        if hasattr(module, "__export__"):
            exports = getattr(module, "__export__")

            for ext in exports:
                getattr(module, ext).setup(self)
        
        return Result(True)