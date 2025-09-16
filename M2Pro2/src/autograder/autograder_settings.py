import dataclasses
from dataclasses import dataclass
from enum import IntEnum, auto
from typing import Any, Self
from util import TryCast, TryGetCast
from .code_test import CodeTest

class Requirement(IntEnum):
    REQUIRED  = auto()
    ALLOWED   = auto()
    FORBIDDEN = auto()

@dataclass
class ProjectSettings:
    importDefault: Requirement
    importOverrides: dict[str, Requirement]
    importLocal: Requirement

    @classmethod
    def FromDict(cls, a_data: dict[str, Any]) -> Self:
        toReturn: ProjectSettings = cls(
            TryGetCast(
                a_data,
                "import_default",
                lambda a_key: Requirement(a_key),
                Requirement.FORBIDDEN
            ), 
            {
                key: TryCast(
                    value,
                    Requirement,
                    Requirement.ALLOWED
                ) for key, value in a_data.get("import_overrides", {}).items()
            }, 
            TryGetCast(
                a_data,
                "import_local",
                Requirement,
                Requirement.ALLOWED
            )
        )
        
        return toReturn
    
    def ToDict(self) -> dict[str, Any]:
        return {
            "import_default": int(self.importDefault),
            "import_overrides": {
                key: int(requirement) for key, requirement in self.importOverrides.items()
            },
            "import_local": int(self.importLocal)
        }

@dataclass
class AutograderSettings:
    projects: dict[str, ProjectSettings] = dataclasses.field(default_factory=dict)
    tests:    dict[str, CodeTest]        = dataclasses.field(default_factory=dict)
    criteria: dict[str, int]             = dataclasses.field(default_factory=dict)

    def UpdateFromDict(self, a_data: dict[str, Any]) -> None:
        self.projects = {key: ProjectSettings.FromDict(project) for key, project in a_data["projects"].items()}
        self.tests = {key: CodeTest.FromDict(test) for key, test in a_data["tests"].items()}
        self.criteria = a_data["criteria"]
    
    def ToDict(self) -> dict[str, Any]:
        return {
            "projects": {
                key: project.ToDict() for key, project in self.projects.items()
            },
            "tests": {
                key: test.ToDict() for key, test in self.tests.items()
            },
            "criteria": self.criteria
        }