import json

from dataclasses import dataclass
from typing import Any, Dict, Optional, Generic, TypeVar

T = TypeVar('T')

@dataclass(frozen=True)
class Result(Generic[T]):
    ok: Optional[T] = None
    err: Optional[BaseException] = None

class Storage:
    _stored: Dict[str, Any] = {}
    _selected: Optional[Any] = None
    
    @classmethod
    def store(cls, key: str, val: Any) -> Result[bool]:
        if key in cls._stored:
            return Result(err=KeyError(f"Stored key [{key}] already exists!"))
        
        cls._stored[key] = val
        return Result(True)

    @classmethod
    def use(cls, key: str) -> Result[bool]:
        if key not in cls._stored:
            return Result(err=KeyError(f"Stored key [{key}] does not exist!"))
        
        cls._selected = cls._stored[key]
        return Result(True)

    @classmethod
    def remove(cls, key: str) -> Result[bool]:
        if key not in cls._stored:
            return Result(err=KeyError(f"Stored key [{key}] does not exist!"))
        
        if cls._selected == cls._stored[key]:
            cls._selected = None
        
        cls._stored.pop(key)
        return Result(True)

    @classmethod
    def clear(cls) -> Result[bool]:
        cls._selected = None
        cls._stored.clear()

        return Result(True)

    @classmethod
    def all(cls) -> Result[Dict[str, Any]]:
        return Result(cls._stored)

    @classmethod
    def load(cls):
        ...

    @classmethod
    def save(cls):
        ...