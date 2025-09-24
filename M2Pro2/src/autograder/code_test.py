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

class IExecutable(CodeTestNode, ABC):
    @abstractmethod
    def Execute(self, a_data: dict[str, Any]) -> None:
        pass

class ICanReturnAny(CodeTestNode, ABC):
    @abstractmethod
    def EvaluateAny(self, a_data: dict[str, Any]) -> Any:
        pass

class ICanReturnBool(ICanReturnAny, ABC):
    @abstractmethod
    def EvaluateBool(self, a_data: dict[str, Any]) -> bool:
        pass

class ICanReturnStr(ICanReturnAny, ABC):
    @abstractmethod
    def EvaluateStr(self, a_data: dict[str, Any]) -> str:
        pass

class ICanReturnInt(ICanReturnAny, ABC):
    @abstractmethod
    def EvaluateInt(self, a_data: dict[str, Any]) -> int:
        pass

class ICanReturnFloat(ICanReturnAny, ABC):
    @abstractmethod
    def EvaluateFloat(self, a_data: dict[str, Any]) -> float:
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
class LiteralTestNode(ICanReturnBool, ICanReturnStr, ICanReturnInt, ICanReturnFloat):
    literalType: str
    literalValue: Any
    
    def ToDict(self) -> dict[str, Any]:
        return {
            "node_id": self.nodeID,
            "literal_type": self.literalType,
            "literal_value": self.literalValue
        }
    
    def EvaluateBool(self, a_data: dict[str, Any]) -> bool:
        return self.literalValue if self.literalType == "boolean" else False

    def EvaluateStr(self, a_data: dict[str, Any]) -> str:
        return self.literalValue if self.literalType == "string" else ""
    
    def EvaluateInt(self, a_data: dict[str, Any]) -> int:
        return self.literalValue if self.literalType == "int" else -1
    
    def EvaluateFloat(self, a_data: dict[str, Any]) -> float:
        return self.literalValue if self.literalType == "float" else 0
    
    def EvaluateAny(self, a_data: dict[str, Any]) -> Any:
        return self.literalType

@dataclass
class ASTNodeTestNode(ICanReturnBool, ICanReturnStr, ICanReturnInt, ICanReturnFloat):
    toCall: str
    
    def ToDict(self) -> dict[str, str]:
        return {
            "node_id": self.nodeID,
            "to_call": "toCall"
        }
    
    def EvaluateBool(self, a_data: dict[str, Any]) -> bool:
        return eval(self.toCall)

    def EvaluateStr(self, a_data: dict[str, Any]) -> str:
        return eval(self.toCall)
    
    def EvaluateInt(self, a_data: dict[str, Any]) -> int:
        return eval(self.toCall)
    
    def EvaluateFloat(self, a_data: dict[str, Any]) -> float:
        return eval(self.toCall)
    
    def EvaluateAny(self, a_data: dict[str, Any]) -> Any:
        return eval(self.toCall)

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
    left: ICanReturnAny
    operator: str
    right: ICanReturnAny

    def ToDict(self) -> dict[str, Any]:
        return {
            "node_id": self.nodeID,
            "left": self.left.ToDict(),
            "operator": self.operator,
            "right": self.right.ToDict()
        }
    
    def EvaluateBool(self, a_data: dict[str, Any]) -> bool:
        left: Any = self.left.EvaluateAny(a_data)
        right: Any = self.right.EvaluateAny(a_data)
        match self.operator:
            case "GTE":
                return left >= right
            case "GT":
                return left > right
            case "LTE":
                return left <= right
            case "LT":
                return left < right
            case "EQ":
                return left == right
            case "NEQ":
                return left != right
            case "AND":
                return left and right
            case "OR":
                return left or right
            case "XOR":
                return (left or right) and (left != right)
            case "NAND":
                return not (left and right)
            case "NOR":
                return not (left or right)
        return False
    
    def EvaluateAny(self, a_data: dict[str, Any]):
        return self.EvaluateBool(a_data)

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

#region Execute
@dataclass
class PostMessageTestNode(IExecutable):
    nodeMessage: str

    def ToDict(self) -> dict[str, str]:
        return {
            "node_id": self.nodeID,
            "node_message": self.nodeMessage
        }

    def Execute(self, a_data: dict[str, Any]) -> None:
        cast("Autograder", a_data["autograder"]).instanceData.report.PostLog(self.nodeMessage.format(a_data))

@dataclass
class BlockTestNode(IExecutable):
    nodes: list[IExecutable]

    def ToDict(self) -> dict[str, Any]:
        return {
            "node_id": self.nodeID,
            "nodes": [node.ToDict() for node in self.nodes]
        }
    
    def Execute(self, a_data: dict[str, Any]) -> None:
        for node in self.nodes:
            node.Execute(a_data)
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
        case {"node_id": nodeID, "to_call": toCall} if nodeID == "ast_node":
            return ASTNodeTestNode(nodeID, toCall)
        case {"node_id": nodeID, "nodes": nodes} if nodeID == "list":
            return ListTestNode(nodeID, [ParseCodeTestNode(node) for node in nodes])
        case {"node_id": nodeID, "nodes": nodes} if nodeID == "block":
            return BlockTestNode(nodeID, [cast(IExecutable, ParseCodeTestNode(node)) for node in nodes if isinstance(ParseCodeTestNode(node), IExecutable)])
        case {"node_id": nodeID, "node_message": nodeMessage} if nodeID == "post_message":
            return PostMessageTestNode(nodeID, nodeMessage)
        case {"node_id": nodeID, "nodes": nodes} if nodeID == "dictionary" and isinstance(nodes, dict):
            return DictionaryTestNode(nodeID, {key: ParseCodeTestNode(node) for key, node in nodes.items()})
        case {"node_id": nodeID, "left": left, "operator": operator, "right": right} if nodeID == "comparison":
            leftParsed:  CodeTestNode|ICanReturnAny = ParseCodeTestNode(left)
            rightParsed: CodeTestNode|ICanReturnAny = ParseCodeTestNode(right)
            if isinstance(leftParsed, ICanReturnAny) and isinstance(rightParsed, ICanReturnAny):
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

def EvaluateCodeTestNode(a_node: ICanReturnAny, a_data: dict[str, Any]) -> Any:
    return a_node.EvaluateAny(a_data)
        
def ExecuteCodeTestNode(a_node: IExecutable, a_data: dict[str, Any]) -> None:
    a_node.Execute(a_data)