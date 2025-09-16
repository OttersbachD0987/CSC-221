from project.project import Project
from .autograder_report import AutograderReport

class AutograderInstanceData:
    def __init__(self):
        self.projects: dict[str, Project] = {}
        self.report: AutograderReport = AutograderReport()