from dataclasses import dataclass
from typing import ClassVar, Callable, Any, Self, TYPE_CHECKING, cast
from abc import ABC, abstractmethod
if TYPE_CHECKING:
    from .autograder_application import Autograder



@dataclass
class CodeTestNode(ABC):
    nodeID: str

    @abstractmethod
    def ToDict(self) -> dict[str, Any]:
        pass

class ICanReturnBool(CodeTestNode, ABC):
    @abstractmethod
    def EvaluateBool(self) -> bool:
        pass

class ICanReturnStr(CodeTestNode, ABC):
    ...

class ICanReturnInt(CodeTestNode, ABC):
    ...

class ICanReturnFloat(CodeTestNode, ABC):
    ...

class ICanReturnAny(ICanReturnBool, ICanReturnStr, ICanReturnInt, ICanReturnFloat, ABC):
    ...

@dataclass
class ListTestNode(CodeTestNode):
    nodes: list[CodeTestNode]

    def ToDict(self) -> dict[str, Any]:
        return {
            "node_id": self.nodeID,
            "nodes": [node.ToDict() for node in self.nodes]
        }
    
@dataclass
class DictionaryTestNode(CodeTestNode):
    nodes: dict[str, CodeTestNode]

    def ToDict(self) -> dict[str, Any]:
        return {
            "node_id": self.nodeID,
            "nodes": {key: node.ToDict() for key, node in self.nodes.items()}
        }

@dataclass
class LiteralTestNode(ICanReturnAny):
    literalType: str
    literalValue: Any

    def ToDict(self) -> dict[str, Any]:
        return {
            "node_id": self.nodeID,
            "literal_type": self.literalType,
            "literal_value": self.literalValue
        }

@dataclass
class ProjectTestNode(CodeTestNode):
    projectName: str
    projectEntrypoint: str
    projectArguments: DictionaryTestNode
    projectInputs: list[str]

    def ToDict(self) -> dict[str, Any]:
        return {
            "node_id": self.nodeID,
            "project_name": self.projectName,
            "project_entrypoint": self.projectEntrypoint,
            "project_arguments": self.projectArguments.ToDict(),
            "project_inputs": self.projectInputs
        }

@dataclass
class InvalidTestNode(CodeTestNode):
    data: dict[str, Any]

    def ToDict(self) -> dict[str, Any]:
        return {
            "node_id": self.nodeID,
            **self.data
        }
    
@dataclass
class ComparisonTestNode(ICanReturnBool):
    left: ICanReturnBool
    operator: str
    right: ICanReturnBool

    def ToDict(self) -> dict[str, Any]:
        return {
            "node_id": self.nodeID,
            "left": self.left.ToDict(),
            "operator": self.operator,
            "right": self.right.ToDict()
        }
    
    def EvaluateBool(self) -> bool:
        match self.operator:
            case "GTE":
                ...
            case "GT":
                ...
            case "LTE":
                ...
            case "LT":
                ...
            case "EQ":
                ...
            case "NEQ":
                ...
            case "AND":
                ...
            case "OR":
                ...
            case "XOR":
                ...
            case "NAND":
                ...
            case "NOR":
                ...
        return False

#region AST Related Nodes
@dataclass
class ASTWalkTestNode(CodeTestNode):
    nodeType: str
    test: ICanReturnBool

    def ToDict(self) -> dict[str, Any]:
        return {
            "node_id": self.nodeID,
            "node_type": self.nodeType,
            "test": self.test.ToDict()
        }
#endregion

@dataclass
class CodeTest:
    TestTypes: ClassVar[dict[str, Callable[[dict[str, CodeTestNode], "Autograder"], tuple[float, bool]]]] = {}
    type: str
    arguments: dict[str, CodeTestNode]

    @classmethod
    def FromDict(cls, a_data: dict[str, Any]) -> Self:
        return cls(
            a_data["type"],
            {key: ParseCodeTestNode(argument) for key, argument in cast(dict[str, dict[str, Any]], a_data.get("arguments", {})).items()}
        )
    
    def ToDict(self) -> dict[str, Any]:
        return {
            "type": self.type,
            "arguments": {key: node.ToDict() for key, node in self.arguments.items()}
        }
    
    @classmethod
    def RegisterTestType(cls, a_id: str, a_testFunction: Callable[[dict[str, CodeTestNode], "Autograder"], tuple[float, bool]]) -> None:
        CodeTest.TestTypes[a_id] = a_testFunction
    
    def RunTest(self, a_grader: "Autograder"):
        CodeTest.TestTypes[self.type](self.arguments, a_grader)


def ParseCodeTestNode(a_node: dict[str, Any]) -> CodeTestNode:
    match a_node:
        case {"node_id": nodeID, "literal_type": literalType, "literal_value": literalValue} if nodeID == "literal":
            return LiteralTestNode(nodeID, literalType, literalValue)
        case {"node_id": nodeID, "nodes": nodes} if nodeID == "list":
            return ListTestNode(nodeID, [ParseCodeTestNode(node) for node in nodes])
        case {"node_id": nodeID, "nodes": nodes} if nodeID == "dictionary" and isinstance(nodes, dict):
            return DictionaryTestNode(nodeID, {key: ParseCodeTestNode(node) for key, node in nodes.items()})
        case {"node_id": nodeID, "left": left, "operator": operator, "right": right} if nodeID == "comparison":
            leftParsed:  CodeTestNode|ICanReturnBool = ParseCodeTestNode(left)
            rightParsed: CodeTestNode|ICanReturnBool = ParseCodeTestNode(right)
            if isinstance(leftParsed, ICanReturnBool) and isinstance(rightParsed, ICanReturnBool):
                return ComparisonTestNode(nodeID, leftParsed, operator, rightParsed)
        case {"node_id": nodeID, "node_type": nodeType, "test": test} if nodeID == "ast_walk":
            testParsed: CodeTestNode|ICanReturnBool = ParseCodeTestNode(test)
            if isinstance(testParsed, ICanReturnBool):
                return ASTWalkTestNode(nodeID, nodeType, testParsed)
        case {"node_id": nodeID, "project_name": projectName, "project_entrypoint": projectEntrypoint, "project_arguments": projectArguments, "project_inputs": projectInputs} if nodeID == "project":
            parsed: CodeTestNode|DictionaryTestNode = ParseCodeTestNode(projectArguments)
            if isinstance(parsed, DictionaryTestNode):
                return ProjectTestNode(nodeID, projectName, projectEntrypoint, parsed, projectInputs)
    return InvalidTestNode("invalid", a_node)

def EvaluateCodeTestNode(a_node: ICanReturnBool) -> bool:
    return a_node.EvaluateBool()
        

def ExecuteCodeTestNode(a_node: CodeTestNode) -> None:
    ...

def EvaluateCodeTestNode(a_node: CodeTestNode) -> Any:
    if isinstance():
        ...