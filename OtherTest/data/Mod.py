from __future__ import annotations

#fmt: off

from dataclasses import dataclass

#

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import NamedTuple, TypedDict, Required, Final
    from Typing import UInt

class Version(NamedTuple):
    major: UInt
    minor: UInt
    patch: UInt
    build: UInt

class ModHeaderDict(TypedDict):
    name: Required[str]
    description: Required[str]
    version: Required[Version]

@dataclass
class ModHeader:
    name: str
    description: str
    id: Final[str]
    version: Version