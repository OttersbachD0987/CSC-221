import ast
from ast import NodeVisitor, While, Constant, Compare, expr, Call, UnaryOp, Not, Gt, GtE, Lt, LtE, Eq, NotEq, FunctionDef, ImportFrom
from typing import Any, cast

class FunctionPreWalker(NodeVisitor):
    def __init__(self) -> None:
        ...
    
    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        return

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

def IsExpressionTrue(a_node: expr) -> bool:
    if isinstance(a_node, Constant):
        return ast.literal_eval(a_node)
    elif isinstance(a_node, Compare):
        if isinstance(a_node.ops[0], Gt):
            ...
        elif isinstance(a_node.ops[0], GtE):
            ...
        elif isinstance(a_node.ops[0], Lt):
            ...
        elif isinstance(a_node.ops[0], LtE):
            ...
        elif isinstance(a_node.ops[0], Eq):
            ...
        elif isinstance(a_node.ops[0], NotEq):
            ...
    elif isinstance(a_node, UnaryOp):
        if isinstance(a_node.op, Not):
            return not IsExpressionTrue(a_node.operand)
    elif isinstance(a_node, Call):
        ...
        #compile()
        #eval()
    return False