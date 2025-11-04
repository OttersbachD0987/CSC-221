from __future__ import annotations

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Self, TypeAlias, Any, override
    from collections.abc import Callable
    
    AnyDict: TypeAlias = dict[str, Any]

class Registry[T]:
    def __init__(self) -> None:
        self.entries: list[T] = []
    
    def Register(self, a_registerable: T) -> int:
        self.entries.append(a_registerable)
        return len(self.entries) - 1
    
    def FindFirst(self, a_predicate: Callable[[T], bool]) -> int:
        for i in range(len(self.entries)):
            if a_predicate(self.entries[i]):
                return i
        return -1
    
    def FindAll(self, a_predicate: Callable[[T], bool]) -> list[int]:
        return [i for i in range(len(self.entries)) if a_predicate(self.entries[i])]
    
    def FindLast(self, a_predicate: Callable[[T], bool]) -> int:
        for i in range(len(self.entries) - 1, -1, -1):
            if a_predicate(self.entries[i]):
                return i
        return -1

class Serializable(ABC):
    @abstractmethod
    @classmethod
    def FromDict(cls, a_data: AnyDict) -> Self:
        ...
    
    @abstractmethod
    def ToDict(self) -> AnyDict:
        ...

@dataclass
class EntityType(Serializable):
    name: str
    description: str
    
    @override
    @classmethod
    def FromDict(cls, a_data: AnyDict) -> EntityType:
        return cls(a_data["name"], a_data["description"])
    
    @override
    def ToDict(self) -> AnyDict:
        return {
            "name": self.name,
            "description": self.description
        }

@dataclass
class Entity:
    x: int
    y: int
    type: int