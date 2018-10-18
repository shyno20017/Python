import unicurses
from typing import Tuple as _Tuple
import time as _time

global stdscr
global _ALL_WINDOWS
global _BASE_SCREEN
global _COLOR_COUNTER
_ALL_WINDOWS = []
_COLOR_COUNTER = 1

class Screen:
    def __init__(self):
        global stdscr
        global _BASE_SCREEN

        stdscr = unicurses.initscr()
        unicurses.start_color()
        unicurses.use_default_colors()
        self.screen = stdscr

        _BASE_SCREEN = self

    @property
    def width(self) -> int:
        """The max width of the screen (The number of columns)."""
        return self.screen.getmaxyx()[1]

    @property
    def height(self) -> int:
        """The max height of the screen (The number of rows)."""
        return self.screen.getmaxyx()[0]

    def set_cursor_position(self, x: int, y: int):
        """Set the cursor position to the specified x, y coordinateself.
        Raises an error if either x or y are out of bounds (less than 0 or greater than the screen boundaries)."""
        self.screen.move(y, x)

    def addstr(self, s: str, x: int = None, y: int = None, mod: int = None):
        """Draws the specified string at the current cursor position.
        If x and y coordinates are passed, the cursor position is set to these coordinates.
        To combine string modifiers (such as a color and an effect), simply add them together and pass them to mod."""
        if x is not None and y is not None:
            self.set_cursor_position(x, y)

        if mod is not None:
            self.screen.addstr(s, mod)
        else:
            self.screen.addstr(s)

    def end(self):
        """Ends the current window (Has no effect if called on a window)."""
        unicurses.endwin()

    def getch(self, call_refresh: bool = True) -> int:
        """Gets the character code of the user's keypress.
        If nodelay is true, returns -1 if no keypress was registered."""
        if call_refresh:
            self.update_all()

        return self.screen.getch()

    def getkey(self, call_refresh: bool = True) -> str:
        """Gets the character of the user's keypress.
        If nodelay is true, raises an error if no keypress was registered."""
        if call_refresh:
            self.refresh()

        return self.screen.getkey()

    def create_window(self, xoff: int, yoff: int, width: int, height: int, name: str = None):
        """Creates a window with (width) number of columns, (height) number of rows
        at (xoff) and (yoff) from the origin of the screen."""
        return Window(xoff, yoff, width, height, name)

    def create_panel(self):
        """Creates a panel using this window (currently does nothing)."""
        return
        # return Panel(self)

    def echo(self, yes: bool = True):
        """If False, then all keypresses by the user are not drawn on the screen."""
        if yes:
            unicurses.echo()
        else:
            unicurses.noecho()

    def noecho(self):
        """Prevents keypresses made by the user from being drawn on the screen.
        Equivalent to echo(False)."""
        self.echo(False)

    def cursor_set(self, yes: bool = True):
        """Sets wether or not to display the blinking cursor at cursor position."""
        unicurses.curs_set(False)

    def keypad(self, yes: bool = False):
        """If True, then detects ALL keypresses made by the userself.
        Otherwise, Does not detect non-character keys (such as arrow keys or f1 through f15 keys)."""
        self.screen.keypad(yes)

    def nodelay(self, yes: bool = False):
        """Sets wether getch() and getkey() wait for user input."""
        self.screen.nodelay(yes)

    def refresh(self, redraw = True):
        """Refreshes the screen to draw all changes made.
        Automatically called when getch() or getkey() are called"""
        if redraw:
            self.screen.redrawwin()
            
        self.screen.refresh()

    def clear(self):
        """Clears the entire window of all characters"""
        self.screen.clear()

    def box(self):
        """Draws a box surrounding the window"""
        self.screen.box()

    def bkgd(self, ch, mod: int = None):
        try:
            ch = ord(ch)
        except:
            pass

        if mod is not None:
            self.screen.bkgd(ch, mod)
        else:
            self.screen.bkgd(ch)

    @classmethod
    def update_all(cls, clear = True, refresh_base = True):
        global _BASE_SCREEN
        global _ALL_WINDOWS
        if clear:
            _BASE_SCREEN.clear()

        if refresh_base:
            _BASE_SCREEN.refresh()

        for window in _ALL_WINDOWS:
            window.refresh()

    def __str__(self):
        return "Standard screen"


class Window(Screen):
    def __init__(self, xoff: int, yoff: int, ncols: int, nrows: int, name: str = None) :
        global _ALL_WINDOWS

        self.screen = unicurses.newwin(nrows, ncols, yoff, xoff)
        _ALL_WINDOWS.append(self)

        self.name = name

    def end(self):
        """Ends the current window (Has no effect if called on a window)"""
        return

    def move(self, x: int, y: int):
        self.screen.mvwin(y, x)

    def top(self):
        """Sets this window to the top of the drawing buffer (In other words, it will be drawn above everything else)."""
        # We remove ourselves from the list then insert ourselves to the end of the list
        current_index = _ALL_WINDOWS.index(self)
        _ALL_WINDOWS.pop(current_index)
        _ALL_WINDOWS.append(self)


    def bottom(self):
        """Sets this window to the bottom of the drawing buffer (In other words, it will be drawn under everything else)."""
        # We remove ourselves from the list then insert ourselves to the beggining of the list
        current_index = _ALL_WINDOWS.index(self)
        _ALL_WINDOWS.pop(current_index)
        _ALL_WINDOWS.insert(0, self)

    def get_above(self):
        """Returns the window above this window in the drawing buffer.
        If this window is at the top, returns the None."""
        current_index = _ALL_WINDOWS.index(self)
        if current_index == len(_ALL_WINDOWS) - 1:
            return None

        return _ALL_WINDOWS[current_index + 1]

    def get_below(self):
        """Returns the window below this window in the drawing buffer.
        If this window is at the bottom, returns the standard screen."""
        current_index = _ALL_WINDOWS.index(self)
        if current_index == 0:
            return _BASE_SCREEN

        return _ALL_WINDOWS[current_index - 1]

    @property
    def xpos(self):
        return self.screen.getbegyx()[1]

    @property
    def ypos(self):
        return self.screen.getbegyx()[0]

    def __str__(self):
        if self.name is None:
            return object.__str__(self)

        return "Window: {}".format(self.name)


def update_all(clear = True, refresh_base = True):
    global _BASE_SCREEN
    global _ALL_WINDOWS

    if clear:
        _BASE_SCREEN.clear()

    if refresh_base:
        _BASE_SCREEN.refresh()

    for window in _ALL_WINDOWS:
        window.refresh()

# class Panel:
#     def __init__(self, window):
#         self.panel = unicurses.new_panel(window.screen)
#         self.window = window
#
#     @classmethod
#     def refresh(cls):
#         unicurses.update_panels()
#         unicurses.doupdate()

class Stopwatch:
    """A Stopwatch to measure time passing"""
    def __init__(self):
        self._start_time = None
        self._time_passed = 0
        self._stored_time = None
        self._timing = False

    def current_time(self):
        """Returns the current system time, as number of seconds since UNIX epoch"""
        return _time.time()

    def _update_time(self):
        if self._stored_time is None:
            return

        new_time = self.current_time()
        self._time_passed += new_time - self._stored_time
        self._stored_time = new_time

    def start(self):
        """Starts (or Resumes) the Stopwatch"""
        if self._timing:
            return

        if self._start_time is None:
            self._start_time = self.current_time()

        self._timing = True
        self._stored_time = self.current_time()
        self._update_time()

    def stop(self):
        """Pauses the Stopwatch"""
        if not self._timing:
            return

        self._timing = False
        self._update_time()
        self._stored_time = None

    def reset(self):
        """Resets the time on the Stopwatch to 0"""
        if self._timing:
            self._start_time = self.current_time()
            self._stored_time = self.current_time()
            self._time_passed = 0
        else:
            self._start_time = None
            self._stored_time = None
            self._time_passed = 0

    @property
    def timeS(self) -> float:
        """The current time on the Stopwatch in Seconds"""
        if self._timing:
            self._update_time()

        return self._time_passed

    @property
    def time(self) -> float:
        """The current time on the Stopwatch in Seconds"""
        return self.timeS

    @property
    def timeMS(self) -> float:
        """The current time on the Stopwatch in Milliseconds"""
        return self.timeS * 1000

    @property
    def timing(self) -> bool:
        return self._timing


class COLOR:
    RED = unicurses.COLOR_RED
    BLUE = unicurses.COLOR_BLUE
    YELLOW = unicurses.COLOR_YELLOW
    GREEN = unicurses.COLOR_GREEN
    BLACK = unicurses.COLOR_BLACK
    WHITE = unicurses.COLOR_WHITE
    MAGENTA = unicurses.COLOR_MAGENTA
    CYAN = unicurses.COLOR_CYAN

    @classmethod
    def create_color(cls, text_color: int, background_color: int) -> int:
        """Creates and returns a Color Combination of text color and background color."""
        global _COLOR_COUNTER
        unicurses.init_pair(_COLOR_COUNTER, text_color, background_color)
        color = unicurses.color_pair(_COLOR_COUNTER)
        _COLOR_COUNTER += 1
        return color

    @classmethod
    def create_color_id(cls, text_color: int, background_color: int) -> int:
        """Creates and returns the id of a Color Combination of text color and background color."""
        global _COLOR_COUNTER
        unicurses.init_pair(_COLOR_COUNTER, text_color, background_color)
        color_id = _COLOR_COUNTER
        _COLOR_COUNTER += 1
        return color_id

    @classmethod
    def create_color_and_id(cls, text_color: int, background_color: int) -> _Tuple[int, int]:
        """Creates and returns the color and id of a Color Combination of text color and background color."""
        global _COLOR_COUNTER
        unicurses.init_pair(_COLOR_COUNTER, text_color, background_color)
        color_id = _COLOR_COUNTER
        color = unicurses.color_pair(color_id)
        _COLOR_COUNTER += 1
        return color, color_id

    @classmethod
    def get_color(cls, id: int) -> int:
        return unicurses.color_pair(id)

    def __init__(self):
        raise Exception("Cannot Initialise this class")

class MODIFIER:
    BOLD = unicurses.A_BOLD
    DIM = unicurses.A_DIM
    BLINK = unicurses.A_BLINK
    INVIS = unicurses.A_INVIS
    COLOR = unicurses.A_COLOR
    NORMAL = unicurses.A_NORMAL
    REVERSE = unicurses.A_REVERSE
    PROTECT = unicurses.A_PROTECT
    STANDOUT = unicurses.A_STANDOUT
    UNDERLINE = unicurses.A_UNDERLINE

    def __init__(self):
        raise Exception("Cannot Initialise this class")

class KEY:
    # Letters (UPPERCASE)
    A = 65
    B = 66
    C = 67
    D = 68
    E = 69
    F = 70
    G = 71
    H = 72
    I = 73
    J = 74
    K = 75
    L = 76
    M = 77
    N = 78
    O = 79
    P = 80
    Q = 81
    R = 82
    S = 83
    T = 84
    U = 85
    V = 86
    W = 87
    X = 88
    Y = 89
    Z = 90

    # Letters (lowercase)
    a = 97
    b = 98
    c = 99
    d = 100
    e = 101
    f = 102
    g = 103
    h = 104
    i = 105
    j = 106
    k = 107
    l = 108
    m = 109
    n = 110
    o = 111
    p = 112
    q = 113
    r = 114
    s = 115
    t = 116
    u = 117
    v = 118
    w = 119
    x = 120
    y = 121
    z = 122

    # NUMBERS
    ZERO = 48
    ONE = 49
    TWO = 50
    THREE = 51
    FOUR = 52
    FIVE = 53
    SIX = 54
    SEVEN = 55
    EIGHT = 56
    NINE = 57

    #  NUMPAD
    NUMPAD_0 = 506
    NUMPAD_1 = 455
    NUMPAD_2 = 456
    NUMPAD_3 = 457
    NUMPAD_4 = 452
    NUMPAD_5 = 253
    NUMPAD_6 = 454
    NUMPAD_7 = 449
    NUMPAD_8 = 450
    NUMPAD_9 = 451
    NUMPAD_MULTIPLY = 463
    NUMPAD_ADD = 465
    NUMPAD_ENTER = 459
    NUMPAD_SUBTRACT = 464
    NUMPAD_DECIMAL = 462
    NUMPAD_DIVIDE = 458

    # FUNCTION KEYS
    F1 = 265
    F2 = 266
    F3 = 267
    F4 = 268
    F5 = 269
    F6 = 270
    F7 = 271
    F8 = 272
    F9 = 273
    F10 = 274
    F11 = 275
    F12 = 276
    F13 = 277
    F14 = 278
    F15 = 279

    # SYMBOLS
    COLON = 58
    SEMICOLON = 59
    EQUALS = 61
    UNDERSCORE = 95
    QUESTION_MARK = 63
    PERIOD = 46
    COMMA = 44
    TILDE = 126
    ACCENT = 96
    OPEN_BRACKET = 40
    CLOSED_BRACKET = 41
    OPEN_SQUARE_BRACKET = 91
    CLOSED_SQUARE_BRACKET = 93
    OPEN_CURLY_BRACKET = 123
    CLOSED_CURLY_BRACKET = 125
    BACKWARD_SLASH = 92
    FORWARD_SLASH = 47
    VERTICAL_PIPE = 124
    SINGLE_QUOTE = 39
    QUOTES = 34
    LESS_THAN = 60
    GREATER_THAN = 62
    EXCLAMATION_MARK = 33
    AT_SIGN = 64
    HASH_SIGN = 35
    DOLLAR_SIGN = 36
    PERCENT_SIGN = 37
    CARET_SIGN = 94
    AMPERSAND_SIGN = 38
    ASTERISK = 42

    # OTHER KEYS
    BACKSPACE = 8
    TAB = 9
    CLEAR = 12
    ENTER = 10
    ESC = 27
    SPACEBAR = 32
    PAGE_UP = 339
    PAGE_DOWN = 338
    END = 358
    HOME = 262
    LEFT_KEY = 260
    UP_KEY = 259
    RIGHT_KEY = 261
    DOWN_KEY = 258
    INSERT = 331
    DELETE = 330

    def __init__(self):
        raise Exception("Cannot Initialise this class")
