'''
    Contains living beings :3
'''
import config
import numpy as np


class Person(object):
    def __init__(self, x, y, ch=config._empty):
        self._x = x
        self._y = y
        # self.type = type
        self.structure = np.chararray((2, 4))
        self.structure[:, :] = config._empty
        self._ch = ch
        self._type = config.types[self._ch]
        self.is_killable = True

    '''def setPosition(self, x, y):
        self.x = x
        self.y = y'''

    def get_type(self):
        # returns whether player/enemy etc
        return self._type

    def get_size(self):
        # returns (height, width)
        return self.structure.shape

    def get_coords(self):
        # returns (x, y)
        return self._x, self._y

    def get_ycoords(self):
        return self._y

    def update_location(self, board, new_x, new_y, init=False):
        # update the location of the person
        if board.draw_obj(type(self)(new_x, new_y)):
            # if initial update, will not clear original
            if not init:
                board.clear_obj(self)
            self._x, self._y = new_x, new_y
            return True
        return False


class Mario(Person):
    def __init__(self, x, y, lives=3):
        super(Mario, self).__init__(x, y, config._mario)
        temp_skel = np.matrix([['/', config._mario, config._mario, '\\'],
                               [config._empty, '|', '|', config._empty]])
        self.structure[:, :] = temp_skel
        self.lives = lives
        self.score = 0


