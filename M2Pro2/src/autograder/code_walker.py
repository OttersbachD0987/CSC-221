import ast
from ast import NodeVisitor, While, Constant, Compare, expr, Call, UnaryOp, Not, Gt, GtE, Lt, LtE, Eq, NotEq, FunctionDef, ImportFrom, Name, Load, Set, Del
from typing import Any, cast

class FunctionPreWalker(NodeVisitor):
    def __init__(self) -> None:
        ...
    
    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        return

class ASTWalker(NodeVisitor):
    def __init__(self, a_):
        self.a = a_

class CodeWalker(NodeVisitor):
    def __init__(self) -> None:
        ...
    
    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        return

    def visit_ImportFrom(self, node: ImportFrom) -> Any:
        return
    
    def visit_While(self, node: While) -> Any:
        print(ast.dump(node.test, include_attributes=True, indent=2))
        
        return

def ParseExpression(a_node: expr) -> Any:
    if isinstance(a_node, Constant):
        return ast.literal_eval(a_node)

def IsExpressionTrue(a_node: expr) -> bool:
    if isinstance(a_node, Constant):
        return ast.literal_eval(a_node)
    elif isinstance(a_node, Compare):
        left = ParseExpression(a_node)
        right = ParseExpression(a_node.comparators[0])
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
            return not IsExpressionTrue(a_node.operand)
    return False