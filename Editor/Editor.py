# fmt: off
from argparse import ArgumentParser, Namespace
from EditorEnums import EditorMode
import os, curses, curses.ascii, KeyCodes

class EditorInstance:
    def __init__(self, a_filepath: str):
        self.filepath: str = a_filepath
        self.mode: EditorMode = EditorMode.NORMAL
        self.running: bool = True
        self.screen: curses.window = curses.initscr()
        self.command_buffer: str = ""
        self.mouse_x_pos: int = 0
        self.mouse_y_pos: int = 0
        self.screen_x_pos: int = 0
        self.screen_y_pos: int = 0
        curses.noecho()
        self.screen.keypad(True)
        curses.cbreak(True)
        with open(self.filepath, "rb+") as file:
            self.content: list[str] = [line.decode().strip() for line in file.readlines()]
            if len(self.content) == 0: 
                self.content = [""]
    
    def Run(self):
        key: int = self.screen.getch()
        self.screen.clear()
        
        match self.mode:
            case EditorMode.NORMAL:
                match key:
                    case curses.KEY_LEFT | KeyCodes.KEY_h:
                        self.SetMousePosX(self.mouse_x_pos - 1)
                    case curses.KEY_RIGHT | KeyCodes.KEY_l:
                        self.SetMousePosX(self.mouse_x_pos + 1)
                    case curses.KEY_UP | KeyCodes.KEY_k:
                        self.SetMousePosY(self.mouse_y_pos - 1)
                    case curses.KEY_DOWN | KeyCodes.KEY_j:
                        self.SetMousePosY(self.mouse_y_pos + 1)
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
                        self.SetMousePosX(self.mouse_x_pos - 1)
                    case curses.KEY_RIGHT:
                        self.SetMousePosX(self.mouse_x_pos + 1)
                    case curses.KEY_UP:
                        self.SetMousePosY(self.mouse_y_pos - 1)
                    case curses.KEY_DOWN:
                        self.SetMousePosY(self.mouse_y_pos + 1)
                    case KeyCodes.KEY_BACKSPACE:
                        if self.mouse_x_pos > 0:
                            self.content[self.mouse_y_pos] = self.content[self.mouse_y_pos][:self.mouse_x_pos - 1] + self.content[self.mouse_y_pos][self.mouse_x_pos::]
                            self.SetMousePosX(self.mouse_x_pos - 1)
                        elif self.mouse_y_pos > 0:
                            new_mouse: int = len(self.content[self.mouse_y_pos - 1])
                            self.content[self.mouse_y_pos - 1] += self.content.pop(self.mouse_y_pos)
                            self.SetMousePosY(self.mouse_y_pos - 1)
                            self.SetMousePosX(new_mouse)
                    case 13 | 10:
                        if False:
                            self.content.insert(self.mouse_y_pos + 1, self.content[self.mouse_y_pos][self.mouse_x_pos + 1::])
                            self.content[self.mouse_y_pos] = self.content[self.mouse_y_pos][:self.mouse_x_pos]
                            self.SetMousePosX(self.mouse_x_pos + 1)
                        else:
                            self.content.insert(self.mouse_y_pos + 1, self.content[self.mouse_y_pos][self.mouse_x_pos::])
                            self.content[self.mouse_y_pos] = self.content[self.mouse_y_pos][:self.mouse_x_pos]
                            self.SetMousePosX(self.mouse_x_pos + 1)
                    case _:
                        if curses.ascii.isprint(key):
                            if False:
                                self.content[self.mouse_y_pos][self.mouse_x_pos] = chr(key)
                            else:
                                self.content[self.mouse_y_pos] = self.content[self.mouse_y_pos][:self.mouse_x_pos] + chr(key) + self.content[self.mouse_y_pos][self.mouse_x_pos::]
                                self.SetMousePosX(self.mouse_x_pos + 1)
            case EditorMode.COMMAND:
                match key:
                    case KeyCodes.KEY_ESCAPE:
                        self.mode = EditorMode.NORMAL
                        self.command_buffer = ""
                    case KeyCodes.KEY_BACKSPACE:
                        self.command_buffer = self.command_buffer[:-1]
                    case 13 | 10:
                        if self.command_buffer == "q":
                            self.running = False
                        elif self.command_buffer == "w":
                            with open(self.filepath, "wb") as file:
                                file.write("\n".join(self.content).encode())
                            self.mode = EditorMode.NORMAL
                            self.command_buffer = ""
                    case _:
                        if curses.ascii.isprint(key):
                            self.command_buffer += chr(key)
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
        for line in range(self.screen_y_pos, min(self.screen_y_pos + curses.LINES - 2, len(self.content))):
            self.screen.addstr(2 + line - self.screen_y_pos, 0, f"{line + 1:>5}. {self.content[line][self.screen_x_pos:min(curses.COLS - 8, len(self.content[line]) + 1)]}")
        if self.mode == EditorMode.COMMAND:
            self.screen.addstr(0, 10, self.command_buffer)
        else:
            self.screen.move(2 + self.mouse_y_pos - self.screen_y_pos, self.mouse_x_pos - self.screen_x_pos + 7)
        self.screen.refresh()

    def SetMousePosX(self, a_pos: int) -> None:
        self.mouse_x_pos = a_pos
        if self.mouse_x_pos < 0:
            if self.mouse_y_pos > 0:
                self.SetMousePosY(self.mouse_y_pos - 1)
                self.mouse_x_pos = len(self.content[self.mouse_y_pos])
            else:
                self.mouse_x_pos = 0
        elif self.mouse_x_pos > len(self.content[self.mouse_y_pos]):
            if self.mouse_y_pos < len(self.content) - 1:
                self.SetMousePosY(self.mouse_y_pos + 1)
                self.mouse_x_pos = 0
            else:
                self.mouse_x_pos = len(self.content[self.mouse_y_pos])

        if self.mouse_x_pos < self.screen_x_pos:
            self.screen_x_pos = self.mouse_x_pos
        elif self.mouse_x_pos >= self.screen_x_pos + curses.COLS - 8:
            self.screen_x_pos = self.mouse_x_pos - curses.COLS + 8
    
    def SetMousePosY(self, a_pos: int) -> None:
        self.mouse_y_pos = a_pos
        if self.mouse_y_pos < 0:
            self.mouse_y_pos = 0
        elif self.mouse_y_pos >= len(self.content):
            self.mouse_y_pos = len(self.content) - 1
        
        self.SetMousePosX(min(len(self.content[self.mouse_y_pos]), self.mouse_x_pos))
        
        if self.mouse_y_pos < self.screen_y_pos:
            self.screen_y_pos = self.mouse_y_pos
        elif self.mouse_y_pos >= self.screen_y_pos + curses.LINES - 3:
            self.screen_y_pos = self.mouse_y_pos - curses.LINES + 3
    
    def __del__(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()

def main():
    parser: ArgumentParser = ArgumentParser()
    parser.add_argument("filepath", type=str)
    namespace: Namespace = parser.parse_args()

    if not os.path.exists(namespace.filepath):
        folders: str = os.path.split(namespace.filepath)[0]
        if folders != "" and not os.path.exists(folders):
            os.makedirs(folders)
        with open(namespace.filepath, "w") as _:
            ...

    editor: EditorInstance = EditorInstance(namespace.filepath)
    while editor.running:
        editor.Run()
    
    del editor

if __name__ == "__main__":
    main()
# fmt: on

