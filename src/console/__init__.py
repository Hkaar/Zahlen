import importlib, pkgutil

from typing import Any, Callable, Dict, Optional
from argparse import ArgumentParser

class Console:
    def __init__(self, *args, **kwargs) -> None:
        self._root = ArgumentParser(*args, **kwargs)
        self._root_parser = self._root.add_subparsers(required=True)

        self._commands: Dict[str, Callable] = {}

    def exec_(self, cmd: Optional[str] = None):
        """Execute the console command based on the given arguments"""

        if not cmd:
            args = self._root.parse_args()
        else:
            args = self._root.parse_args(cmd.split(" "))
            
        args.func(args)

    def register(self, name: str, handler: Callable, desc: Optional[str] = None) -> ArgumentParser:
        """Append a command to the specified subparser"""
        
        if name in self._commands:
            raise ValueError(f"{name} already exists as a command!")

        subparser = self._root_parser.add_parser(name, help=desc)
        subparser.set_defaults(func=handler)

        self._commands[name] = handler
        return subparser

    def auto_import(self, path, package: Optional[str] = None):
        """Automatically import all the included commands within the given path"""

        modules = filter(lambda mod: not mod.name.startswith("_"), pkgutil.iter_modules(path))

        for mod in modules:
            module = importlib.import_module(f".{mod.name}", package=package)

            if hasattr(module, "Export"):
                getattr(module, "Export").setup(self)
