from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
import json
from json import JSONDecodeError
import os

from data.Registry import Registry
from data.Mod import ModHeader, ModHeaderDict, Version

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Self, override
    from Typing import AnyDict, JSONSerializable, UInt

class Serializable[**PL, **PS](ABC):
    @abstractmethod
    @classmethod
    def FromDict(cls, a_data: AnyDict, *a_args: PL.args, **a_kwargs: PL.kwargs) -> Self:
        ...
    
    @abstractmethod
    def ToDict(self, *a_args: PS.args, **a_kwargs: PS.kwargs) -> AnyDict:
        ...

@dataclass
class EntityType(Serializable[[], []]):
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
class Entity(Serializable[[], []]):
    x: int
    y: int
    type: UInt

def main() -> None:
    entityTypeRegistry: Registry[EntityType] = Registry[EntityType]()
    modPath: str = os.path.join(os.getcwd(), "Mods")
    for I_file in os.scandir(".\\Mods"):
        if os.path.isdir(I_file) and (modDataPath := os.path.isfile(os.path.join(modPath, "mod.json"))):
            try:
                with open(modDataPath) as modDataFile:
                    data: ModHeaderDict = json.load(modDataFile)
                    mod: ModHeader = ModHeader(data["name"], data["description"], I_file.name.replace(" ", "_").lower(), data["version"])
                    
            except JSONDecodeError as e:
                print(e)
            except TypeError as e:
                print(e)

if __name__ == "__main__":
    main()