from file_type import FileType
from python_file import PythonFile
import sys, os

def GetFiles(a_dir: str) -> list[FileType]:
    toReturn: list[FileType] = []
    for fileDescriptor in os.scandir(a_dir):
        if fileDescriptor.is_dir():
            ...
        elif fileDescriptor.is_file():
            match fileDescriptor.name.split(".")[-1]:
                case "py":
                    toReturn.append(PythonFile(a_dir, a_dir))
    return toReturn

class Project:
    def __init__(self, a_dir: str) -> None:
        