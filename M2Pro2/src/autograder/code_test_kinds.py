from . import code_test
from .code_test import CodeTest, CodeTestNode, ProjectTestNode, ListTestNode, LiteralTestNode, DictionaryTestNode
from .autograder_instance_data import AutograderInstanceData
import subprocess
from subprocess import Popen, PIPE

def CompareOutput(a_arguments: dict[str, CodeTestNode], a_app: AutograderInstanceData):
    ...

def AssertOutput(a_arguments: dict[str, CodeTestNode], a_app: AutograderInstanceData):
    testProject: ProjectTestNode|None = a_arguments["test_project"] if isinstance(a_arguments["test_project"], ProjectTestNode) else None
    stdoutMode:      LiteralTestNode|None = a_arguments["stdout"]       if isinstance(a_arguments["stdout"],       LiteralTestNode) else None
    stderrMode:      LiteralTestNode|None = a_arguments["stderr"]       if isinstance(a_arguments["stderr"],       LiteralTestNode) else None
    returnCodeMode:  LiteralTestNode|None = a_arguments["return_code"]  if isinstance(a_arguments["return_code"],  LiteralTestNode) else None

    if testProject is None:
        return
    
    project = a_app.projects[testProject.projectName]

    sub: Popen[str] = Popen(" ".join([
            "python", f"{project.dir}\\{testProject.projectEntrypoint}", 
            *[f"\"{node.literalValue}\"" for node in testProject.projectArguments.nodes.values() if isinstance(node, LiteralTestNode)]]), 
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        cwd=project.dir, 
        text=True)

    stdout, stderr = sub.communicate("\n".join(testProject.projectInputs))
        
    if sub.stdout != None:
        print(f"stdout:\n {stdout.strip()}\n")
    if sub.stderr != None:
        print(f"stderr:\n {stderr.strip()}\n")

    print(f"Return Code: {sub.returncode}")
    
    
CodeTest.RegisterTestType("compare_output", CompareOutput)
CodeTest.RegisterTestType("assert_output", AssertOutput)

###
## Compare Output
# Baseline Project
# - Arguments
# - Inputs
# Test Project
# - Arguments
# - Inputs
# stdout
# * Match
# * Ignore
# stderr
# * Match
# * Ignore
# Return Code
# * Match
# * Ignore
###
## Assert Output
# Test Project
# - Arguments
# - Inputs
# stdout
# * Match (Regex)
# * Ignore
# stderr
# * Match (Regex)
# * Ignore
# Return Code
# * Match (Regex)
# * Ignore
###