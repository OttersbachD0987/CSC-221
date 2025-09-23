from dataclasses import dataclass
from enum import IntEnum, auto

class ModifierType(IntEnum):
    ADDITION = auto()
    MULTIPLY = auto()
    OVERRIDE = auto()
    OVERKILL = auto()

@dataclass
class AutograderModifier:
    criterion: str
    modifierType: ModifierType
    modifierValue: float
