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
class LiteralTestNode(CodeTestNode):
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
class CodeTest:
    TestTypes: ClassVar[dict[str, Callable[[dict[str, CodeTestNode], "Autograder"], None]]] = {}
    type: str
    arguments: dict[str, CodeTestNode]

    @classmethod
    def FromDict(cls, a_data: dict[str, Any]) -> Self:
        return cls(
            a_data["type"],
            {
                key: ParseCodeTestNode(argument) for key, argument in cast(dict[str, dict[str, Any]], a_data.get("arguments", {})).items()
            }
        )
    
    def ToDict(self) -> dict[str, Any]:
        return {
            "type": self.type,
            "arguments": {
                key: node.ToDict() for key, node in self.arguments.items()
            }
        }
    
    @classmethod
    def RegisterTestType(cls, a_id: str, a_testFunction: Callable[[dict[str, CodeTestNode], "Autograder"], None]) -> None:
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
        case {"node_id": nodeID, "project_name": projectName, "project_entrypoint": projectEntrypoint, "project_arguments": projectArguments, "project_inputs": projectInputs} if nodeID == "project":
            parsed: CodeTestNode|DictionaryTestNode = ParseCodeTestNode(projectArguments)
            if isinstance(parsed, DictionaryTestNode):
                return ProjectTestNode(nodeID, projectName, projectEntrypoint, parsed, projectInputs)
    return InvalidTestNode("invalid", a_node)