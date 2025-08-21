from argparse import ArgumentParser, Namespace
from Editor.EditorEnums import EditorMode
import sys, os, curses, keyboard

class EditorInstance:
    def __init__(self, a_filepath: str):
        self.filepath: str = a_filepath
        self.mode: EditorMode = EditorMode.NORMAL
    
    def OnPress(self):
        ...

keyboard.on_press()

if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("filepath", type=str)
    namespace: Namespace = parser.parse_args()
    
    if not os.path.exists(namespace.filepath):
        os.makedirs(os.path.split(namespace.filepath))
        with open(namespace.filepath, "w") as file:
            ...
        