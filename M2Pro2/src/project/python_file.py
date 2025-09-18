import ast
from ast import Module, Import, ImportFrom
import symtable
from symtable import SymbolTable
import tokenize
from tokenize import TokenInfo
from .file_type import FileType
from autograder import code_walker

class PythonFile(FileType):
    def __init__(self, a_path: str, a_name: str):
        super().__init__(a_path, a_name)

        try:
            with open(f"{a_path}\\{a_name}", "r") as file:
                self.contents: str = file.read()
                self.ast: Module = ast.parse(self.contents, a_name)
                file.seek(0)
                self.tokens: list[TokenInfo] = [token for token in tokenize.generate_tokens(file.read)]
                self.symtable: SymbolTable = symtable.symtable(self.contents, self.name, "exec")
        except FileNotFoundError as e:
            print(f"The file {e.filename} does not exist.")
        except PermissionError as e:
            print(f"You do not have sufficient permissions to access the file {e.filename}.")
        except IsADirectoryError as e:
            print(f"{e.filename} is not a file, it is a directory.")

        #print(ast.dump(self.ast, include_attributes=True, indent=1))
        #print(self.tokens)
        #print(self.symtable.get_symbols())
        
        for node in ast.walk(self.ast):
            if isinstance(node, Import):
                for name in node.names:
                    print(f"{name.name} as {name.asname}")
            elif isinstance(node, ImportFrom):
                print(f"Level: {node.level}")
                print(f"Module: {node.module}")
                for name in node.names:
                    print(f"{name.name} as {name.asname}")

        print(f"---------")

        code_walker.CodeWalker().visit(self.ast)
        
        self.imports = [name for node in ast.walk(self.ast) if isinstance(node, Import) for name in node.names]