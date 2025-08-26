from argparse import ArgumentParser, Namespace
from EditorEnums import EditorMode
import os, curses, curses.ascii, sys, KeyCodes
from io import BytesIO


class EditorInstance:
    def __init__(self, a_filepath: str):
        self.filepath: str = a_filepath
        self.mode: EditorMode = EditorMode.NORMAL
        self.running: bool = True
        self.screen: curses.window = curses.initscr()
        self.command_buffer: str = ""
        self.mouse_pos: int = 0
        curses.noecho()
        self.screen.keypad(True)
        curses.cbreak(True)
        with open(self.filepath, "rb+") as file:
            print(file.read())
        with open(self.filepath, "rb+") as file:
            self.byte_stream: BytesIO = BytesIO(file.read().replace(b'\r\n', b'\n'))
    
    def Run(self):
        key: int = self.screen.getch()
        self.screen.clear()
        
        match self.mode:
            case EditorMode.NORMAL:
                match key:
                    case curses.KEY_LEFT | KeyCodes.KEY_h:
                        self.SetMousePos(self.mouse_pos - 1)
                    case curses.KEY_RIGHT | KeyCodes.KEY_l:
                        self.SetMousePos(self.mouse_pos + 1)
                    case curses.KEY_UP | KeyCodes.KEY_k:
                        self.SetMousePos(self.byte_stream.getvalue().rfind(b'\n', 0, self.mouse_pos) - 1)
                    case curses.KEY_DOWN | KeyCodes.KEY_j:
                        self.SetMousePos(self.mouse_pos + len(self.byte_stream.readline()))
                    case KeyCodes.KEY_COLON:
                        self.mode = EditorMode.COMMAND
                    case KeyCodes.KEY_i:
                        self.mode = EditorMode.INSERT
            case EditorMode.VISUAL:
                match key:
                    case KeyCodes.KEY_ESCAPE:
                        self.mode = EditorMode.NORMAL
                    case curses.KEY_LEFT:
                        ...
            case EditorMode.INSERT:
                match key:
                    case KeyCodes.KEY_ESCAPE:
                        self.mode = EditorMode.NORMAL
                    case curses.KEY_LEFT:
                        self.SetMousePos(self.mouse_pos - 1)
                    case curses.KEY_RIGHT:
                        self.SetMousePos(self.mouse_pos + 1)
                    case curses.KEY_UP:
                        self.SetMousePos(self.byte_stream.getvalue().rfind(b'\n', 0, self.mouse_pos) - 1)
                    case curses.KEY_DOWN:
                        self.SetMousePos(self.mouse_pos + len(self.byte_stream.readline()) + 1)
                    case _:
                        if curses.ascii.isprint(key):
                            self.byte_stream.write(bytes([key]))
            case EditorMode.COMMAND:
                match key:
                    case KeyCodes.KEY_ESCAPE:
                        self.mode = EditorMode.NORMAL
                        self.command_buffer = ""
                    case 8:
                        self.command_buffer = self.command_buffer[:-1]
                    case 13 | 10:
                        if self.command_buffer == "q":
                            self.running = False
                        elif self.command_buffer == "w":
                            with open(self.filepath, "wb") as file:
                                file.write(self.byte_stream.getbuffer())
                    case _:
                        if curses.ascii.isprint(key):
                            self.command_buffer += chr(key)
        a = max(self.byte_stream.getvalue().rfind(b'\n', 0, self.mouse_pos) + 1, 0)
        self.byte_stream.seek(a)
        match self.mode:
            case EditorMode.NORMAL:
                self.screen.addstr("NORMAL || ")
            case EditorMode.VISUAL:
                self.screen.addstr("VISUAL || ")
            case EditorMode.INSERT:
                self.screen.addstr("INSERT || ")
            case EditorMode.COMMAND:
                self.screen.addstr("COMMAND||>")
        self.screen.hline(0, 10, " ", curses.COLS - 9)
        self.screen.hline(1, 0, '=', curses.COLS - 1)
        self.screen.move(2, 0)
        index: int = self.byte_stream.getvalue().count(b'\n', 0, max(self.byte_stream.tell(), 0)) + 1
        for line in self.byte_stream:
            self.screen.addstr(f"{index:>5}. {line.decode()}")
            index += 1
        self.byte_stream.seek(self.mouse_pos)
        if self.mode == EditorMode.COMMAND:
            self.screen.addstr(0, 10, self.command_buffer)
        else:
            self.screen.move(2, self.mouse_pos - max(a, 0) + 7)
        self.screen.refresh()

    def SetMousePos(self, a_pos: int) -> None:
        self.mouse_pos = min(max(a_pos, 0), sys.getsizeof(self.byte_stream))
        self.byte_stream.seek(self.mouse_pos)
    
    def __del__(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()
        self.byte_stream.close()

def main():
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("filepath", type=str)
    namespace: Namespace = parser.parse_args()

    if not os.path.exists(namespace.filepath):
        os.makedirs(os.path.split(namespace.filepath)[0])
        with open(namespace.filepath, "w") as _:
            ...

    editor: EditorInstance = EditorInstance(namespace.filepath)
    while editor.running:
        editor.Run()
    
    del editor

if __name__ == "__main__":
    main()