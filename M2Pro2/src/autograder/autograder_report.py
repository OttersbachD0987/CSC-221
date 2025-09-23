import dataclasses
from dataclasses import dataclass
import time
from .autograder_modifier import AutograderModifier

@dataclass
class AutograderReport:
    messages:  list[tuple[int, str]]    = dataclasses.field(default_factory=list)
    modifiers: list[AutograderModifier] = dataclasses.field(default_factory=list)

    def PostLog(self, a_message: str) -> None:
        self.messages.append((time.time_ns(), a_message))
    
    def AddModifier(self, a_modifier: AutograderModifier) -> None:
        self.modifiers.append(a_modifier)
