from .code_test import CodeTest, CodeTestNode
from subprocess import Popen, PIPE
from typing import TYPE_CHECKING
import re

if TYPE_CHECKING:
    from .autograder_application import Autograder
    from .code_test import ProjectTestNode, LiteralTestNode


def CompareOutput(a_arguments: dict[str, CodeTestNode], a_app: Autograder):
    baseProject:    ProjectTestNode|None = a_arguments["base_project"] if isinstance(a_arguments["base_project"], ProjectTestNode) else None
    testProject:    ProjectTestNode|None = a_arguments["test_project"] if isinstance(a_arguments["test_project"], ProjectTestNode) else None
    stdoutMode:     LiteralTestNode|None = a_arguments["stdout"]       if isinstance(a_arguments["stdout"],       LiteralTestNode) else None
    stderrMode:     LiteralTestNode|None = a_arguments["stderr"]       if isinstance(a_arguments["stderr"],       LiteralTestNode) else None
    returnCodeMode: LiteralTestNode|None = a_arguments["return_code"]  if isinstance(a_arguments["return_code"],  LiteralTestNode) else None

    if testProject is None or baseProject is None:
        return
    
    projectBase = a_app.instanceData.projects[baseProject.projectName]
    projectTest = a_app.instanceData.projects[testProject.projectName]

    subBase: Popen[str] = Popen(" ".join([
            "python", f"{projectBase.dir}\\{baseProject.projectEntrypoint}", 
            *[f"\"{node.literalValue}\"" for node in baseProject.projectArguments.nodes.values() if isinstance(node, LiteralTestNode)]]), 
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        cwd=projectBase.dir, 
        text=True)

    stdoutBase, stderrBase = subBase.communicate("\n".join(baseProject.projectInputs))
    
    subTest: Popen[str] = Popen(" ".join([
            "python", f"{projectTest.dir}\\{testProject.projectEntrypoint}", 
            *[f"\"{node.literalValue}\"" for node in testProject.projectArguments.nodes.values() if isinstance(node, LiteralTestNode)]]), 
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        cwd=projectTest.dir, 
        text=True)

    stdoutTest, stderrTest = subTest.communicate("\n".join(testProject.projectInputs))

    if True:
        print(stdoutBase == stdoutTest)
    
    if True:
        print(stderrBase == stderrTest)
    
    if True:
        print(subBase.returncode == subTest.returncode)

def AssertOutput(a_arguments: dict[str, CodeTestNode], a_app: Autograder):
    testProject:    ProjectTestNode|None = a_arguments["test_project"] if isinstance(a_arguments["test_project"], ProjectTestNode) else None
    stdoutMode:     LiteralTestNode|None = a_arguments["stdout"]       if isinstance(a_arguments["stdout"],       LiteralTestNode) else None
    stderrMode:     LiteralTestNode|None = a_arguments["stderr"]       if isinstance(a_arguments["stderr"],       LiteralTestNode) else None
    returnCodeMode: LiteralTestNode|None = a_arguments["return_code"]  if isinstance(a_arguments["return_code"],  LiteralTestNode) else None

    if testProject is None:
        return
    
    project = a_app.instanceData.projects[testProject.projectName]

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

    stdoutRegex     = re.compile(stdoutMode.literalValue     if stdoutMode     is not None else ".*")
    stderrRegex     = re.compile(stderrMode.literalValue     if stderrMode     is not None else ".*")
    returnCodeRegex = re.compile(returnCodeMode.literalValue if returnCodeMode is not None else ".*")

    print(F"{stdoutRegex.match(stdout.strip())}")
    print(F"{stderrRegex.match(stderr.strip())}")
    print(F"{returnCodeRegex.match(f"{sub.returncode}")}")

    print(f"Return Code: {sub.returncode} : {2}")
    
    
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