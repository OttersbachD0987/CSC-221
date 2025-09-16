from .file_type import FileType
from .python_file import PythonFile

class Project:
    def __init__(self, a_name: str, a_dir: str) -> None:
        self.name: str = a_name
        self.dir: str = a_dir
        self.files: list[FileType] = util.GetFiles(a_dir)

    def EvaluateImports(self) -> None:
        ...

import util