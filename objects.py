'''
    Contains structure of each object
'''

import config
from config import x_fac, y_fac
import numpy as np


class Object:

    def __init__(self, x, y, ch=config._empty):
        self._x = x
        self._y = y
        self.width = 3
        self.height = 2
        self.is_killable = False
        self._ch = ch
        self.structure = np.chararray((self.height, self.width))
        self.structure[:, :] = self._ch
        self._type = config.types[self._ch]

    def get_type(self):
        """# returns whether "Bomber", "Enemy", etc"""
        return self._type

    def get_size(self):
        """# returns (height, width)"""
        return self.structure.shape

    def get_coords(self):
        """# returns (x, y)"""
        return (self._x, self._y)


class Ground(Object):

    def __init__(self, n, m):
        super(Ground, self).__init__(n, m, config._ground)
        self.height = int(m)
        self.width = int(n)

    def __repr__(self):
        """ repr """
        for r in range(self.height):
            print("\n")
            for c in range(self.width):
                try:
                    print(self.structure[r, c].decode(), end="")
                except UnicodeDecodeError:
                    print(self.structure[r, c], end="")
            return ""


class Brick(Object):
    def __init__(self, n, m):
        super(Brick, self).__init__(n, m, config._bricks)
        self.height = int(m)
        self.width = int(n)

    def __repr__(self):
        """ repr """
        for r in range(self.height):
            print("\n")
            for c in range(self.width):
                try:
                    print(self.structure[r, c].decode(), end="")
                except UnicodeDecodeError:
                    print(self.structure[r, c], end="")
            return ""


class Question(Object):
    def __init__(self, n, m):
        super(Question, self).__init__(n, m, config._question)
        self.height = int(m)
        self.width = int(n)

    def __repr__(self):
        """ repr """
        for r in range(self.height):
            print("\n")
            for c in range(self.width):
                try:
                    print(self.structure[r, c].decode(), end="")
                except UnicodeDecodeError:
                    print(self.structure[r, c], end="")
            return ""


class Pipe:
    def __init__(self, x, y, ch = config._pipe):
        self.height = x
        self.width = y
        self._ch = ch
        self.structure = np.chararray((self.height, self.width))
        self.structure[:, :] = self._ch
        self._type =  config.types[self._ch]

    def get_size(self):
        """# returns (height, width)"""
        return self.structure.shape

class Coin:
    def __init__(self, x, y, ch = config._coin):
        self._x = x
        self._y = y
        self._ch = ch
        self.structure = 'O'
        self._type = config.types[self._ch]

    def update_lacation(self, x, y):
        self._x = x
        self._y = y

