from enum import Enum

class EditorMode(Enum):
    NORMAL  = 0
    VISUAL  = 1
    INSERT  = 2
    COMMAND = 3

class FileType(Enum):
    TEXT = ".txt"
    PYTHON = ".py"

class CursorMode(Enum):
    INSERT  = 0
    REPLACE = 1