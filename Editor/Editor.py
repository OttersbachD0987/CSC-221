# fmt: off
from argparse import ArgumentParser, Namespace
from EditorEnums import EditorMode, CursorMode
import os
import curses
import curses.ascii
import KeyCodes

class EditorInstance:
    def __init__(self, a_filepath: str):
        self.filepath: str = a_filepath
        self.mode: EditorMode = EditorMode.NORMAL
        self.cursor_mode: CursorMode = CursorMode.INSERT
        self.running: bool = True
        self.screen: curses.window = curses.initscr()
        self.command_buffer: str = ""
        self.cursor_x_pos: int = 0
        self.cursor_y_pos: int = 0
        self.screen_x_pos: int = 0
        self.screen_y_pos: int = 0
        self.repeat_buffer: str = ""
        curses.noecho()
        self.screen.keypad(True)
        curses.cbreak(True)
        with open(self.filepath, "r") as file:
            self.content: list[str] = [line.rstrip() for line in file.readlines()]
            if len(self.content) == 0: 
                self.content = [""]
    
    def HandleInput(self) -> None:
        key: int = self.screen.getch()
        
        match self.mode:
            case EditorMode.NORMAL:
                match key:
                    case curses.KEY_LEFT | KeyCodes.KEY_h:
                        self.SetCursorPosX(self.cursor_x_pos - 1)
                    case curses.KEY_RIGHT | KeyCodes.KEY_l:
                        self.SetCursorPosX(self.cursor_x_pos + 1)
                    case curses.KEY_UP | KeyCodes.KEY_k:
                        self.SetCursorPosY(self.cursor_y_pos - 1)
                    case curses.KEY_DOWN | KeyCodes.KEY_j:
                        self.SetCursorPosY(self.cursor_y_pos + 1)
                    case KeyCodes.KEY_COLON:
                        self.mode = EditorMode.COMMAND
                    case KeyCodes.KEY_a:
                        self.SetCursorPosX(self.cursor_x_pos + 1)
                        self.mode = EditorMode.INSERT
                    case KeyCodes.KEY_i:
                        self.mode = EditorMode.INSERT
                    case KeyCodes.KEY_0 | KeyCodes.KEY_1 | KeyCodes.KEY_2 | KeyCodes.KEY_3 | KeyCodes.KEY_4 | KeyCodes.KEY_5 | KeyCodes.KEY_6 | KeyCodes.KEY_7 | KeyCodes.KEY_8 | KeyCodes.KEY_9:
                        self.repeat_buffer += chr(key)
            case EditorMode.VISUAL:
                match key:
                    case curses.ascii.ESC:
                        self.mode = EditorMode.NORMAL
                    case curses.KEY_LEFT:
                        ...
                    case KeyCodes.KEY_0 | KeyCodes.KEY_1 | KeyCodes.KEY_2 | KeyCodes.KEY_3 | KeyCodes.KEY_4 | KeyCodes.KEY_5 | KeyCodes.KEY_6 | KeyCodes.KEY_7 | KeyCodes.KEY_8 | KeyCodes.KEY_9:
                        self.repeat_buffer += chr(key)
            case EditorMode.INSERT:
                match key:
                    case curses.ascii.ESC:
                        self.mode = EditorMode.NORMAL
                    case curses.KEY_LEFT:
                        self.SetCursorPosX(self.cursor_x_pos - 1)
                    case curses.KEY_RIGHT:
                        self.SetCursorPosX(self.cursor_x_pos + 1)
                    case curses.KEY_UP:
                        self.SetCursorPosY(self.cursor_y_pos - 1)
                    case curses.KEY_DOWN:
                        self.SetCursorPosY(self.cursor_y_pos + 1)
                    case curses.ascii.BS:
                        if self.cursor_x_pos > 0:
                            self.content[self.cursor_y_pos] = self.content[self.cursor_y_pos][:self.cursor_x_pos - 1] + self.content[self.cursor_y_pos][self.cursor_x_pos::]
                            self.SetCursorPosX(self.cursor_x_pos - 1)
                        elif self.cursor_y_pos > 0:
                            new_mouse: int = len(self.content[self.cursor_y_pos - 1])
                            self.content[self.cursor_y_pos - 1] += self.content.pop(self.cursor_y_pos)
                            self.SetCursorPosY(self.cursor_y_pos - 1)
                            self.SetCursorPosX(new_mouse)
                    case 13 | 10:
                        match self.cursor_mode:
                            case CursorMode.REPLACE:
                                self.content.insert(self.cursor_y_pos + 1, self.content[self.cursor_y_pos][self.cursor_x_pos + 1::])
                                self.content[self.cursor_y_pos] = self.content[self.cursor_y_pos][:self.cursor_x_pos]
                                self.SetCursorPosX(self.cursor_x_pos + 1)
                            case CursorMode.INSERT:
                                self.content.insert(self.cursor_y_pos + 1, self.content[self.cursor_y_pos][self.cursor_x_pos::])
                                self.content[self.cursor_y_pos] = self.content[self.cursor_y_pos][:self.cursor_x_pos]
                                self.SetCursorPosX(self.cursor_x_pos + 1)
                    case _:
                        if curses.ascii.isprint(key):
                            match self.cursor_mode:
                                case CursorMode.REPLACE:
                                    self.content[self.cursor_y_pos] = self.content[self.cursor_y_pos][:self.cursor_x_pos] + chr(key) + self.content[self.cursor_y_pos][self.cursor_x_pos + 1::]
                                case CursorMode.INSERT:
                                    self.content[self.cursor_y_pos] = self.content[self.cursor_y_pos][:self.cursor_x_pos] + chr(key) + self.content[self.cursor_y_pos][self.cursor_x_pos::]
                                    self.SetCursorPosX(self.cursor_x_pos + 1)
            case EditorMode.COMMAND:
                match key:
                    case curses.ascii.ESC:
                        self.mode = EditorMode.NORMAL
                        self.command_buffer = ""
                    case curses.ascii.BS:
                        self.command_buffer = self.command_buffer[:-1]
                    case 13 | 10:
                        if self.command_buffer == "q":
                            self.running = False
                        elif self.command_buffer == "w":
                            with open(self.filepath, "w") as file:
                                file.write("\n".join(self.content))
                            self.mode = EditorMode.NORMAL
                            self.command_buffer = ""
                    case _:
                        if curses.ascii.isprint(key):
                            self.command_buffer += chr(key)
        
    def Render(self) -> None:
        self.screen.clear()
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
            self.screen.move(2 + self.cursor_y_pos - self.screen_y_pos, self.cursor_x_pos - self.screen_x_pos + 7)
        self.screen.refresh()

    def SetCursorPosX(self, a_pos: int) -> None:
        """
        """
        self.cursor_x_pos = a_pos
        if self.cursor_x_pos < 0:
            if self.cursor_y_pos > 0:
                self.SetCursorPosY(self.cursor_y_pos - 1)
                self.cursor_x_pos = len(self.content[self.cursor_y_pos])
            else:
                self.cursor_x_pos = 0
        elif self.cursor_x_pos > len(self.content[self.cursor_y_pos]):
            if self.cursor_y_pos < len(self.content) - 1:
                self.SetCursorPosY(self.cursor_y_pos + 1)
                self.cursor_x_pos = 0
            else:
                self.cursor_x_pos = len(self.content[self.cursor_y_pos])

        if self.cursor_x_pos < self.screen_x_pos:
            self.screen_x_pos = self.cursor_x_pos
        elif self.cursor_x_pos >= self.screen_x_pos + curses.COLS - 8:
            self.screen_x_pos = self.cursor_x_pos - curses.COLS + 8
    
    def SetCursorPosY(self, a_pos: int) -> None:
        self.cursor_y_pos = a_pos
        if self.cursor_y_pos < 0:
            self.cursor_y_pos = 0
        elif self.cursor_y_pos >= len(self.content):
            self.cursor_y_pos = len(self.content) - 1
        
        self.SetCursorPosX(max(min(len(self.content[self.cursor_y_pos]) - 1, self.cursor_x_pos), 0))
        
        if self.cursor_y_pos < self.screen_y_pos:
            self.screen_y_pos = self.cursor_y_pos
        elif self.cursor_y_pos >= self.screen_y_pos + curses.LINES - 3:
            self.screen_y_pos = self.cursor_y_pos - curses.LINES + 3
    
    def Cleanup(self) -> None:
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
        open(namespace.filepath, "w").close()

    editor = EditorInstance(namespace.filepath)
    while editor.running:
        editor.Render()
        editor.HandleInput()
    editor.Cleanup()

if __name__ == "__main__":
    main()
# fmt: on