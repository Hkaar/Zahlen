# Type definitions for the zahlen console
# Author : Hkaar

from abc import ABC, abstractmethod
from argparse import ArgumentParser

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar, Callable

T = TypeVar('T')

@dataclass(frozen=True)
class Result(Generic[T]):
    """A class to represent the result of a process"""
    
    ok: Optional[T] = None
    err: Optional[BaseException] = None

class ConsoleInterface(ABC):
    """The abstract interface for the console class"""
    
    @abstractmethod
    def parse(self) -> Result[bool]:
        ...

    @abstractmethod
    def exec_(self, cmd: str, *args) -> Result[bool]:
        ...
    
    @abstractmethod
    def register(self, name: str, handler: Callable, desc: Optional[str] = None) -> Result[ArgumentParser]:
        ...

    @abstractmethod
    def shell(self) -> Result[bool]:
        ...

    @abstractmethod
    def _import(self, path: str, package: Optional[str] = None) -> Result[bool]:
        ...