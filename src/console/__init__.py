import argparse, importlib, pkgutil

from typing import Callable, Optional

class Console:
    """A command line interface for the zahlen cli"""
     
    _root_parser = argparse.ArgumentParser(description="Zahlen Console Commands")
    _indexed_commands = {}

    @classmethod
    def exec(cls, cmd: Optional[str] = None):
        """Execute the console command based on the given arguments"""

        if not cmd:
            args = cls._root_parser.parse_args()
        else:
            args = cls._root_parser.parse_args(cmd.split(" "))
            
        args.func(args)

    @classmethod
    def register(cls, name: str, desc: Optional[str] = None) -> argparse._SubParsersAction:
        """Register a subcommand to the root parser"""

        if name in cls._indexed_commands:
            raise ValueError(f"Error while adding {name} to index. {name} already exists!")

        subcommand = cls._root_parser.add_subparsers(title=name, description=desc, required=True)
        cls._indexed_commands[name] = subcommand
        
        return subcommand

    @classmethod
    def append(cls, root: str, name: str, handler: Callable, desc: Optional[str] = None) -> argparse.ArgumentParser:
        """Append a command to the specified subparser"""

        if root not in cls._indexed_commands:
            raise ValueError(f"Error while appending command {name} to {root}. {root} does not exist!")

        subparser = cls._indexed_commands[root].add_parser(name, help=desc)
        subparser.set_defaults(func=handler)

        return subparser

    @classmethod
    def auto_import(cls, path, package: Optional[str] = None):
        """Automatically import all the included commands within the given path"""

        modules = filter(lambda mod: not mod.name.startswith("_"), pkgutil.iter_modules(path))

        for mod in modules:
            module = importlib.import_module(f".{mod.name}", package=package)

            if hasattr(module, "Export"):
                getattr(module, "Export").setup(Console)

