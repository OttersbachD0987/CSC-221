import os
from project.python_file import PythonFile
from project.directory_file import DirectoryFile
from project.file_type import FileType
from typing import Callable

def GetFiles(a_dir: str) -> list[FileType]:
    toReturn: list[FileType] = []
    for fileDescriptor in os.scandir(a_dir):
        if fileDescriptor.is_dir():
            toReturn.append(DirectoryFile(fileDescriptor.path.removesuffix(fileDescriptor.name).rstrip("\\"), fileDescriptor.name))
        elif fileDescriptor.is_file():
            match fileDescriptor.name.split(".")[-1]:
                case "py":
                    toReturn.append(PythonFile(fileDescriptor.path.removesuffix(fileDescriptor.name).rstrip("\\"), fileDescriptor.name))
    return toReturn

def TryGetCast[K, V, T](a_dict: dict[K, V], a_key: K, a_converter: Callable[[V], T], a_default: T) -> T:
    data: V|None = a_dict.get(a_key)
    if data is not None:
        try:
            return a_converter(data)
        except Exception as e:
            print(e)
    return a_default

def TryCast[V, R](a_value: V, a_converter: Callable[[V], R], a_default: R) -> R:
    try:
        return a_converter(a_value)
    except:
        return a_default