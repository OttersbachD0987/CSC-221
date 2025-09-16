import subprocess
import ast
import tokenize
import symtable
import os
from project.python_file import PythonFile
from project.project import Project
from typing import Any
from autograder.autograder_application import Autograder
from autograder.autograder_settings import Requirement
from autograder import code_test_kinds




# ===============================
# MAIN EXECUTION
# ===============================
if __name__ == "__main__":
    instructorProjectName: str = input("Internal name to use for the project: ")
    instructorProjectDirectory: str = input("Path to instructor project directory: ")
    instructorProject: Project = Project(instructorProjectName, f"{os.getcwd()}\\{instructorProjectDirectory}")
    studentProjectName: str = input("Internal name to use for the project: ")
    studentProjectDirectory: str = input("Path to student project directory: ")
    studentProject: Project = Project(studentProjectName, f"{os.getcwd()}\\{studentProjectDirectory}")

    grader: Autograder = Autograder()
    grader.SetConfigurationFromDict({
        "projects": {
            "default": {
                "import_default": Requirement.ALLOWED,
                "import_overrides": {},  #key: int(requirement) for key, requirement in self.importOverrides.items()
                "import_local": Requirement.ALLOWED
            },
            instructorProjectName: {
                "import_default": Requirement.ALLOWED,
                "import_overrides": {},  #key: int(requirement) for key, requirement in self.importOverrides.items()
                "import_local": Requirement.ALLOWED
            },
            studentProjectName: {
                "import_default": Requirement.ALLOWED,
                "import_overrides": {},  #key: int(requirement) for key, requirement in self.importOverrides.items()
                "import_local": Requirement.ALLOWED
            }
        },  #key: project.ToDict() for key, project in self.projects.items()
        "tests": {
            "first_assertion": {
                "type": "assert_output",
                "arguments": {
                    "test_project": {
                        "node_id": "project",
                        "project_name": instructorProjectName,
                        "project_entrypoint": "main.py",
                        "project_arguments": {
                            "node_id": "dictionary",
                            "nodes": {
                                "a": {
                                    "node_id": "literal",
                                    "literalType": "string",
                                    "literalValue": "a"
                                }
                            }
                        },
                        "project_inputs": [
                            "Moo",
                            "Conker"
                        ]
                    },
                    "stdout": {
                        "node_id": "literal",
                        "literalType": "string",
                        "literalValue": "a"
                    },
                    "stderr": {
                        "node_id": "literal",
                        "literalType": "string",
                        "literalValue": "b"
                    },
                    "return_code": {
                        "node_id": "literal",
                        "literalType": "string",
                        "literalValue": "c"
                    }
                }   #key: node.ToDict() for key, node in self.arguments.items()
            },
            "second_assertion": {
                "type": "assert_output",
                "arguments": {
                    "test_project": {
                        "node_id": "project",
                        "project_name": studentProjectName,
                        "project_entrypoint": "main.py",
                        "project_arguments": {
                            "node_id": "dictionary",
                            "nodes": {
                                "a": {
                                    "node_id": "literal",
                                    "literalType": "string",
                                    "literalValue": "a"
                                }
                            }
                        },
                        "project_inputs": [
                            "Moo",
                            "Conker"
                        ]
                    },
                    "stdout": {
                        "node_id": "literal",
                        "literalType": "string",
                        "literalValue": "a"
                    },
                    "stderr": {
                        "node_id": "literal",
                        "literalType": "string",
                        "literalValue": "b"
                    },
                    "return_code": {
                        "node_id": "literal",
                        "literalType": "string",
                        "literalValue": "c"
                    }
                }   #key: node.ToDict() for key, node in self.arguments.items()
            },
            "first_comparison": {
                "type": "compare_output",
                "arguments": {
                    "base_project": {
                        "node_id": "project",
                        "project_name": instructorProjectName,
                        "project_entrypoint": "main.py",
                        "project_arguments": {
                            "node_id": "dictionary",
                            "nodes": {
                                "a": {
                                    "node_id": "literal",
                                    "literalType": "string",
                                    "literalValue": "a"
                                }
                            }
                        },
                        "project_inputs": [
                            "Moo",
                            "Conker"
                        ]
                    },
                    "test_project": {
                        "node_id": "project",
                        "project_name": studentProjectName,
                        "project_entrypoint": "main.py",
                        "project_arguments": {
                            "node_id": "dictionary",
                            "nodes": {
                                "a": {
                                    "node_id": "literal",
                                    "literalType": "string",
                                    "literalValue": "a"
                                }
                            }
                        },
                        "project_inputs": [
                            "Moo",
                            "Conker"
                        ]
                    },
                    "stdout": {
                        "node_id": "literal",
                        "literalType": "string",
                        "literalValue": "a"
                    },
                    "stderr": {
                        "node_id": "literal",
                        "literalType": "string",
                        "literalValue": "b"
                    },
                    "return_code": {
                        "node_id": "literal",
                        "literalType": "string",
                        "literalValue": "c"
                    }
                }   #key: node.ToDict() for key, node in self.arguments.items()
            }
        },  #key: test.ToDict() for key, test in self.tests.items()
        "criteria": {
            "foo": 1
        }   #self.criteria
    })

    grader.instanceData.projects[instructorProjectName] = instructorProject
    grader.instanceData.projects[studentProjectName] = studentProject

    grader.settings.tests["first_assertion"].RunTest(grader.instanceData)
    grader.settings.tests["second_assertion"].RunTest(grader.instanceData)
    grader.settings.tests["first_comparison"].RunTest(grader.instanceData)

    #score, rubric = GradeFile(instructorFile, studentFile)
    print("=== Rubric ===")
    print(f"{'Criterion':<20} {'Passed':<8} {'Weight':<6} {'Points':<6} Feedback")
    print("-"*80)
    #for item in rubric:
    #    print(f"{item['Criterion']:<20} {str(item['Passed']):<8} {item['Weight']:<6} "
    #          f"{item['Points Earned']:<6} {item['Feedback']}")
    #print("\n=== Final Grade ===")
    #print(f"Score: {score}/100 (Breakdown: {CRITERIA})")
