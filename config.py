'''
    contains symbols and constants
'''

_ground = "X"
_bricks = "/"
_mario = "M"
_empty = " "
_question = "?"
_pipe = '|'

types = {
    _empty: "Unassigned",

    _ground: "Ground",
    _bricks: "Bricks",
    _question: "Question",
    _pipe: "Pipe",

    _mario: "Mario"
}

x_fac, y_fac = (4, 2)

UP, DOWN, LEFT, RIGHT, BOMB, QUIT = range(6)
DIR = [UP, DOWN, LEFT, RIGHT]
INVALID = -1

_allowed_inputs = {
    UP: ['w', '\x1b[A'],
    DOWN: ['s', '\x1b[B'],
    LEFT: ['a', '\x1b[D'],
    RIGHT: ['d', '\x1b[C'],
    BOMB: ['b'],
    QUIT: ['q']
}


def get_key(key):
    for x in _allowed_inputs:
        if key in _allowed_inputs[x]:
            return x
    return INVALID


# Gets a single character from standard input.  Does not echo to the screen.
class _Getch:

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:

    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys
        import tty
        import termios
        fedvar = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fedvar)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:

    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


_getch = _Getch()


class AlarmException(Exception):
    pass


def alarmHandler(signum, frame):
    raise AlarmException


def get_input(timeout=1):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = _getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

def getcc(ch):
    try:
        if ch == _empty:
            return Back.BLUE
        elif ch == _ground:
            return Back.GREEN
        elif ch == _bricks:
            return Back.BLACK
        elif ch == _question:
            return Back.YELLOW
        else:
            return None

    except KeyError:
        return ch