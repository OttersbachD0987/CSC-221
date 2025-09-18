import dataclasses
from dataclasses import dataclass
from typing import Any
from .code_test import CodeTest
from .project_settings import ProjectSettings

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