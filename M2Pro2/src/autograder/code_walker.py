import ast
import re
from ast import NodeVisitor, While, Constant, Compare, expr, Call, UnaryOp, Not, Gt, GtE, Lt, LtE, Eq, NotEq, FunctionDef, ImportFrom, Name, Load, Set, Del, AST, Add, alias, And, AnnAssign, arg, arguments, Assert, Assign, AsyncFor, AsyncFunctionDef, AsyncWith, Attribute, AugAssign, Await, BinOp, BitAnd, BitOr, BitXor, BoolOp, boolop, Break, ClassDef, cmpop, comprehension, Continue, Delete, Dict, DictComp, Div, ExceptHandler, excepthandler, Expr, expr_context, Expression, FloorDiv, For, FormattedValue, FunctionType, GeneratorExp, Global, If, IfExp, Import, In, Interactive, Invert, Is, IsNot, JoinedStr, keyword, Lambda, List, ListComp, LShift, Match, match_case, MatchAs, MatchClass, MatchMapping, MatchOr, MatchSequence, MatchSingleton, MatchStar, MatchValue, MatMult, Mod, mod, Module, Mult, NamedExpr, NodeTransformer, Nonlocal, NotIn, operator, Or, ParamSpec, Pass, pattern, Pow, Raise, Return, RShift, SetComp, Slice, Starred, stmt, Store, Sub, Subscript, Try, TryStar, Tuple, type_ignore, type_param, TypeAlias, TypeIgnore, TypeVar, TypeVarTuple, UAdd, unaryop, USub, With, withitem, Yield, YieldFrom, iter_fields
from typing import Any, cast, TYPE_CHECKING, Self
from enum import StrEnum, auto
from dataclasses import dataclass

if TYPE_CHECKING:
    from project_settings import ProjectSettings
    from project.project import Project

class ASTNodeType(StrEnum):
    WHILE                    = auto()
    CONSTANT                 = auto()
    COMPARE                  = auto()
    CALL                     = auto()
    UNARY_OP                 = auto()
    NOT                      = auto()
    GREATER_THAN             = auto()
    GREATER_THAN_OR_EQUAL_TO = auto()
    LESS_THAN                = auto()
    LESS_THAN_OR_EQUAL_TO    = auto()
    EQUAL                    = auto()
    NOT_EQUAL                = auto()
    FUNCTION_DEF             = auto()
    IMPORT                   = auto()
    IMPORT_FROM              = auto()
    NAME                     = auto()
    LOAD                     = auto()
    SET                      = auto()
    DEL                      = auto()
    ADD                      = auto()
    ALIAS                    = auto()
    AND                      = auto()
    ANN_ASSIGN               = auto()
    ARG                      = auto()
    ARGUMENTS                = auto()
    ASSERT                   = auto()
    ASSIGN                   = auto()
    ASYNC_FOR                = auto()
    ASYNC_FUNCTION_DEF       = auto()
    ASYNC_WITH               = auto()
    ATTRIBUTE                = auto()
    AUG_ASSIGN               = auto()
    AWAIT                    = auto()
    BIN_OP                   = auto()
    BIT_AND                  = auto()
    BIT_OR                   = auto()
    BIT_XOR                  = auto()
    BOOL_OP                  = auto()
    BREAK                    = auto()
    CLASS_DEF                = auto()
    CMPOP                    = auto()
    COMPREHENSION            = auto()
    CONTINUE                 = auto()
    DELETE                   = auto()
    DICT                     = auto()
    DICT_COMP                = auto()
    DIV                      = auto()
    EXCEPT_HANDLER           = auto() # ExceptHandler
    EXPR                     = auto()
    EXPR_CONTEXT             = auto()
    EXPRESSION               = auto()
    FLOOR_DIV                = auto()
    FOR                      = auto()
    FORMATTED_VALUE          = auto()
    FUNCTION_TYPE            = auto()
    GENERATOR_EXP            = auto()
    GLOBAL                   = auto()
    IF                       = auto()
    IF_EXP                   = auto()
    IN                       = auto()
    INTERACTIVE              = auto()
    INVERT                   = auto()
    IS                       = auto()
    IS_NOT                   = auto()
    JOINED_STR               = auto()
    KEYWORD                  = auto()
    LAMBDA                   = auto()
    LIST                     = auto()
    LIST_COMP                = auto()
    L_SHIFT                  = auto()
    MATCH                    = auto()
    MATCH_CASE               = auto()
    MATCH_AS                 = auto()
    MATCH_CLASS              = auto()
    MATCH_MAPPING            = auto()
    MATCH_OR                 = auto()
    MATCH_SEQUENCE           = auto()
    MATCH_SINGLETON          = auto()
    MATCH_STAR               = auto()
    MATCH_VALUE              = auto()
    MAT_MULT                 = auto()
    MOD                      = auto() # Mod
    MODULE                   = auto()
    MULT                     = auto()
    NAMED_EXPR               = auto()
    NONLOCAL                 = auto()
    NOT_IN                   = auto()
    OPERATOR                 = auto()
    OR                       = auto()
    PARAM_SPEC               = auto()
    PASS                     = auto()
    PATTERN                  = auto()
    POW                      = auto()
    RAISE                    = auto()
    RETURN                   = auto()
    R_SHIFT                  = auto()
    SET_COMP                 = auto()
    SLICE                    = auto()
    STARRED                  = auto()
    STMT                     = auto()
    STORE                    = auto()
    SUB                      = auto()
    SUBSCRIPT                = auto()
    TRY                      = auto()
    TRY_STAR                 = auto()
    TUPLE                    = auto()
    TYPE_PARAM               = auto()
    TYPE_ALIAS               = auto()
    TYPE_IGNORE              = auto() # TypeIgnore
    TYPE_VAR                 = auto()
    TYPE_VAR_TUPLE           = auto()
    U_ADD                    = auto()
    UNARY_OPERATOR           = auto() # unaryop
    U_SUB                    = auto()
    WITH                     = auto()
    WITH_ITEM                = auto()
    YIELD                    = auto()
    YIELD_FROM               = auto()
    ERROR                    = auto()
    

def isTrue(a_node: expr, a_default: bool = False) -> bool:
    """Check if an expression is true, with a default.
    """
    try:
        if isinstance(a_node, UnaryOp) and isinstance(a_node.op, Not):
            return not isTrue(a_node.operand, a_default)
        else:
            return ast.literal_eval(a_node)
    except ValueError as e:
        print(e)
    return a_default

class ASTPattern:
    def __init__(self, a_nodeType: str|ASTNodeType, a_comparisonData: dict[str, Any]|None = None) -> None:
        self.nodeType: ASTNodeType = ASTNodeType(a_nodeType) if isinstance(a_nodeType, str) else a_nodeType
        self.comparisonData: dict[str, Any] = {} if a_comparisonData is None else a_comparisonData
    
    @classmethod
    def fromDict(cls, a_data: dict[str, Any]) -> "ASTPattern":
        """Load ASTPattern from dict.
        """
        #print(a_data)
        astTo: ASTPattern = ASTPattern(ASTNodeType(a_data["node_type"]), {})
        match astTo.nodeType:
            case ASTNodeType.WHILE:
                if "match_kind" in a_data:
                    astTo.comparisonData["match_kind"] = a_data["match_kind"]
                    match a_data["match_kind"]:
                        case "test_pattern":
                            astTo.comparisonData["test_pattern"] = ASTPattern.fromDict(a_data["test_pattern"])
                        case "test_patterns":
                            astTo.comparisonData["test_patterns"] = [ASTPattern.fromDict(testPattern) for testPattern in a_data["test_patterns"]]
            case ASTNodeType.CONSTANT:
                if "match_kind" in a_data:
                    astTo.comparisonData["match_kind"] = a_data["match_kind"]
                    match a_data["match_kind"]:
                        case "regex":
                            astTo.comparisonData["kind_match"] = a_data.get("kind_match", ".*")
                            astTo.comparisonData["value_match"] = a_data.get("value_match", ".*")
                        case "is_true":
                            astTo.comparisonData["default_val"] = a_data.get("default_val", False)
                            astTo.comparisonData["value"] = a_data.get("value", True)
            case ASTNodeType.NAME:
                astTo.comparisonData["name"] = a_data.get("name", ".*")
                if "context" in a_data:
                    astTo.comparisonData["context"] = ASTPattern.fromDict(a_data["context"])
            case ASTNodeType.BREAK:
                ...
            case ASTNodeType.CONTINUE:
                ...
            case ASTNodeType.ASSIGN:
                #print("A")
                if "match_kind" in a_data:
                    #print("B")
                    astTo.comparisonData["match_kind"] = a_data["match_kind"]
                    match a_data["match_kind"]:
                        case "target_pattern":
                            #print("C")
                            astTo.comparisonData["target_pattern"] = ASTPattern.fromDict(a_data["target_pattern"])
        
        return astTo

    def toDict(self) -> dict[str, Any]:
        """Convert to a dictionary.
        """
        return {
            "a": 1
        }

class ASTWalker(NodeVisitor):
    def __init__(self, a_pattern: ASTPattern):
        self.pattern: ASTPattern = a_pattern
    
    def generic_visit(self, node: AST) -> int:
        collection: int = self.visiting(node, self.pattern)
        for field, value in iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, AST):
                        collection += self.visit(item)
            elif isinstance(value, AST):
                collection += self.visit(value)
        return collection
    
    def visiting(self, node: AST, a_pattern: ASTPattern) -> int:
        """Function to handle visiting a node.
        """
        #print(node)
        match a_pattern.nodeType:
            case ASTNodeType.WHILE:
                if isinstance(node, While):
                    if "match_kind" in a_pattern.comparisonData:
                        match a_pattern.comparisonData["match_kind"]:
                            case "test_pattern":
                                return self.visiting(node.test, a_pattern.comparisonData["test_pattern"])
                            case "test_patterns":
                                #print(ast.dump(node.test, indent="  "))
                                #print([testPattern for testPattern in a_pattern.comparisonData["test_patterns"]])
                                #print([self.visiting(node.test, testPattern) for testPattern in a_pattern.comparisonData["test_patterns"]])
                                #print([0 < self.visiting(node.test, testPattern) for testPattern in a_pattern.comparisonData["test_patterns"]])
                                #print(any([0 < self.visiting(node.test, testPattern) for testPattern in a_pattern.comparisonData["test_patterns"]]))
                                return 1 if any([0 < self.visiting(node.test, testPattern) for testPattern in a_pattern.comparisonData["test_patterns"]]) else 0
                    #print("Ending")
                    return 1
            case ASTNodeType.CONSTANT:
                if isinstance(node, Constant):
                    if "match_kind" in a_pattern.comparisonData:
                        match a_pattern.comparisonData["match_kind"]:
                            case "regex":
                                return 1 if re.search(cast(str, a_pattern.comparisonData["kind_match"]), str(node.kind)) and re.search(a_pattern.comparisonData["value_match"], str(node.value)) else 0
                            case "is_true":
                                return 1 if isTrue(node, a_pattern.comparisonData["default_val"]) == a_pattern.comparisonData["value"] else 0
                    return 1
            case ASTNodeType.COMPARE:
                if isinstance(node, Compare):
                    return 1
            case ASTNodeType.CALL:
                if isinstance(node, Call):
                    return 1
            case ASTNodeType.UNARY_OP:
                if isinstance(node, UnaryOp):
                    return 1
            case ASTNodeType.NOT:
                if isinstance(node, Not):
                    return 1
            case ASTNodeType.GREATER_THAN:
                if isinstance(node, Gt):
                    return 1
            case ASTNodeType.GREATER_THAN_OR_EQUAL_TO:
                if isinstance(node, GtE):
                    return 1
            case ASTNodeType.LESS_THAN:
                if isinstance(node, Lt):
                    return 1
            case ASTNodeType.LESS_THAN_OR_EQUAL_TO:
                if isinstance(node, LtE):
                    return 1
            case ASTNodeType.EQUAL:
                if isinstance(node, Eq):
                    return 1
            case ASTNodeType.NOT_EQUAL:
                if isinstance(node, NotEq):
                    return 1
            case ASTNodeType.FUNCTION_DEF:
                if isinstance(node, FunctionDef):
                    return 1
            case ASTNodeType.IMPORT:
                if isinstance(node, Import):
                    return 1
            case ASTNodeType.IMPORT_FROM:
                if isinstance(node, ImportFrom):
                    return 1
            case ASTNodeType.NAME:
                if isinstance(node, Name):
                    #print(ast.dump(node, indent="  "))
                    if "context" in a_pattern.comparisonData and self.visiting(node.ctx, a_pattern.comparisonData["context"]) == 0:
                        return 0
                    return 1 if re.search(a_pattern.comparisonData["name"], node.id) else 0
            case ASTNodeType.LOAD:
                if isinstance(node, Load):
                    return 1
            case ASTNodeType.SET:
                if isinstance(node, Set):
                    return 1
            case ASTNodeType.DEL:
                ...
            case ASTNodeType.ADD:
                ...
            case ASTNodeType.ALIAS:
                ...
            case ASTNodeType.AND:
                ...
            case ASTNodeType.ANN_ASSIGN:
                ...
            case ASTNodeType.ARG:
                ...
            case ASTNodeType.ARGUMENTS:
                ...
            case ASTNodeType.ASSERT:
                ...
            case ASTNodeType.ASSIGN:
                #print("Assign?")
                if isinstance(node, Assign):
                    if "match_kind" in a_pattern.comparisonData:
                        match a_pattern.comparisonData["match_kind"]:
                            case "target_pattern":
                                return self.visiting(node.targets[0], a_pattern.comparisonData["target_pattern"])
                    else:
                        return 1
            case ASTNodeType.ASYNC_FOR:
                ...
            case ASTNodeType.ASYNC_FUNCTION_DEF:
                ...
            case ASTNodeType.ASYNC_WITH:
                ...
            case ASTNodeType.ATTRIBUTE:
                ...
            case ASTNodeType.AUG_ASSIGN:
                ...
            case ASTNodeType.AWAIT:
                ...
            case ASTNodeType.BIN_OP:
                ...
            case ASTNodeType.BIT_AND:
                ...
            case ASTNodeType.BIT_OR:
                ...
            case ASTNodeType.BIT_XOR:
                ...
            case ASTNodeType.BOOL_OP:
                ...
            case ASTNodeType.BREAK:
                if isinstance(node, Break):
                    return 1
            case ASTNodeType.CLASS_DEF:
                ...
            case ASTNodeType.CMPOP:
                ...
            case ASTNodeType.COMPREHENSION:
                ...
            case ASTNodeType.CONTINUE:
                if isinstance(node, Continue):
                    return 1
            case ASTNodeType.DELETE:
                ...
            case ASTNodeType.DICT:
                ...
            case ASTNodeType.DICT_COMP:
                ...
            case ASTNodeType.DIV:
                ...
            case ASTNodeType.EXCEPT_HANDLER:
                ...
            case ASTNodeType.EXPR:
                ...
            case ASTNodeType.EXPR_CONTEXT:
                ...
            case ASTNodeType.EXPRESSION:
                ...
            case ASTNodeType.FLOOR_DIV:
                ...
            case ASTNodeType.FOR:
                ...
            case ASTNodeType.FORMATTED_VALUE:
                ...
            case ASTNodeType.FUNCTION_TYPE:
                ...
            case ASTNodeType.GENERATOR_EXP:
                ...
            case ASTNodeType.GLOBAL:
                ...
            case ASTNodeType.IF:
                ...
            case ASTNodeType.IF_EXP:
                ...
            case ASTNodeType.IN:
                ...
            case ASTNodeType.INTERACTIVE:
                ...
            case ASTNodeType.INVERT:
                ...
            case ASTNodeType.IS:
                ...
            case ASTNodeType.IS_NOT:
                ...
            case ASTNodeType.JOINED_STR:
                ...
            case ASTNodeType.KEYWORD:
                ...
            case ASTNodeType.LAMBDA:
                ...
            case ASTNodeType.LIST:
                ...
            case ASTNodeType.LIST_COMP:
                ...
            case ASTNodeType.L_SHIFT:
                ...
            case ASTNodeType.MATCH:
                ...
            case ASTNodeType.MATCH_CASE:
                ...
            case ASTNodeType.MATCH_AS:
                ...
            case ASTNodeType.MATCH_CLASS:
                ...
            case ASTNodeType.MATCH_MAPPING:
                ...
            case ASTNodeType.MATCH_OR:
                ...
            case ASTNodeType.MATCH_SEQUENCE:
                ...
            case ASTNodeType.MATCH_SINGLETON:
                ...
            case ASTNodeType.MATCH_STAR:
                ...
            case ASTNodeType.MATCH_VALUE:
                ...
            case ASTNodeType.MAT_MULT:
                ...
            case ASTNodeType.MOD:
                ...
            case ASTNodeType.MODULE:
                ...
            case ASTNodeType.MULT:
                ...
            case ASTNodeType.NAMED_EXPR:
                ...
            case ASTNodeType.NONLOCAL:
                ...
            case ASTNodeType.NOT_IN:
                ...
            case ASTNodeType.OPERATOR:
                ...
            case ASTNodeType.OR:
                ...
            case ASTNodeType.PARAM_SPEC:
                ...
            case ASTNodeType.PASS:
                ...
            case ASTNodeType.PATTERN:
                ...
            case ASTNodeType.POW:
                ...
            case ASTNodeType.RAISE:
                ...
            case ASTNodeType.RETURN:
                ...
            case ASTNodeType.R_SHIFT:
                ...
            case ASTNodeType.SET_COMP:
                ...
            case ASTNodeType.SLICE:
                ...
            case ASTNodeType.STARRED:
                ...
            case ASTNodeType.STMT:
                ...
            case ASTNodeType.STORE:
                ...
            case ASTNodeType.SUB:
                ...
            case ASTNodeType.SUBSCRIPT:
                ...
            case ASTNodeType.TRY:
                ...
            case ASTNodeType.TRY_STAR:
                ...
            case ASTNodeType.TUPLE:
                ...
            case ASTNodeType.TYPE_PARAM:
                ...
            case ASTNodeType.TYPE_ALIAS:
                ...
            case ASTNodeType.TYPE_IGNORE:
                ...
            case ASTNodeType.TYPE_VAR:
                ...
            case ASTNodeType.TYPE_VAR_TUPLE:
                ...
            case ASTNodeType.U_ADD:
                ...
            case ASTNodeType.UNARY_OPERATOR:
                ...
            case ASTNodeType.U_SUB:
                ...
            case ASTNodeType.WITH:
                ...
            case ASTNodeType.WITH_ITEM:
                ...
            case ASTNodeType.YIELD:
                ...
            case ASTNodeType.YIELD_FROM:
                ...
        return 0

@dataclass
class ImportData:
    local: bool
    name: str

class CodeWalker(NodeVisitor):
    def __init__(self, a_project: "Project", a_projectSettings: "ProjectSettings") -> None:
        self.project: "Project" = a_project
        self.filenames = [file.name for file in a_project.files]
        self.projectSettings: "ProjectSettings" = a_projectSettings
        self.imports: set[ImportData] = set()
    
    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        return
    
    def visit_Import(self, node: Import) -> Any:
        self.imports.update([ImportData(name.name in self.filenames, name.name) for name in node.names])

    def visit_ImportFrom(self, node: ImportFrom) -> Any:
        self.imports.update([ImportData(name.name in self.filenames, name.name) for name in node.names])
    
    def visit_While(self, node: While) -> Any:
        print(ast.dump(node.test, include_attributes=True, indent=2))
        
        return

def parseExpression(a_node: expr) -> Any:
    """Parse an expression.
    """
    if isinstance(a_node, Constant):
        return ast.literal_eval(a_node)

def isExpressionTrue(a_node: expr) -> bool:
    """Check if an expression is true.
    """
    if isinstance(a_node, Constant):
        return ast.literal_eval(a_node)
    elif isinstance(a_node, Compare):
        left = parseExpression(a_node)
        right = parseExpression(a_node.comparators[0])
        if left or right == None:
            return False
        if isinstance(a_node.ops[0], Gt):
            return left > right
        elif isinstance(a_node.ops[0], GtE):
            return left >= right
        elif isinstance(a_node.ops[0], Lt):
            return left < right
        elif isinstance(a_node.ops[0], LtE):
            return left <= right
        elif isinstance(a_node.ops[0], Eq):
            return left == right
        elif isinstance(a_node.ops[0], NotEq):
            return left != right
    elif isinstance(a_node, UnaryOp):
        if isinstance(a_node.op, Not):
            return not isExpressionTrue(a_node.operand)
    return False