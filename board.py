'''
    Contains the board class
'''

import sys
from os import system
from config import x_fac, y_fac
import numpy as np
import config
from objects import Ground


class Board:
    def __init__(self, l, w):
        # preferred size = (34,76)
        self.width = w
        self.height = l
        self.dimen = (l, w)
        self._b = np.chararray((l, w))
        self._b[:, :] = config._empty
        self.init_points = []
        self.score = 0
        self.frame_counter = 0

        self.init_board()

        '''self._storage = {
            config.types[config._bomb]: [],
            config.types[config._bricks]: [],
            config.types[config._enemy]: []
        }'''

    def init_board(self, reset=False):
        if reset:
            self.frame_counter = 0
        w = Ground(self.width / 20, self.height / 20)
        w_height, w_width = w.get_size()
        # creating the rows
        full_row, full_row[:, :] = np.chararray((w_height, self.width)), config._ground
        # emp_row, emp_row[:, :] = np.chararray((w_height, self.width)), config._empty
        # emp_row[:, :w_width] = emp_row[:, -w_width:] = w.structure

        # alt_row, alt_row[:, :] = np.chararray((w_height, self.width)), config._empty
        # for c in range(1, int(self.width / w_width) + 1):
        # if c % 2:
        # alt_row[:, (c - 1) * w_width: (c * w_width)] = w.structure

        # assigning top and bottom
        self._b[-w_height:, :] = full_row

        # assigning other rows
        """for r in range(2, int(self.height / w_height)):
            # alt row
            if r % 2:
                cur_row = alt_row
            else:
                cur_row = emp_row

            self._b[(r - 1) * w_height: (r * w_height), :] = cur_row"""

        # create the inital points for spawning objects
        # subtracting two edge blocks for each top bottom
        # and dividing by two for range of motion
        fp = (5, 3)
        # each object is 4 px wide
        total_block_x = int((self.width / config.x_fac - 2) / 2 + 1)
        # each object is 2px tall
        total_block_y = int((self.height / config.y_fac - 2) / 2 + 1)
        for r in range(total_block_x):
            for c in range(total_block_y):
                self.init_points.append((fp[0] + r * (2 * config.x_fac), fp[-1] + c * (2 * config.y_fac)))

        self.init_points = list(set(self.init_points))

    def reset_board(self):
        reset = True
        self.init_board(self, reset)
        # self.clear_storage()

    def spawn(self, obj):
        '''# method to spawn the main player'''
        if obj.get_type() == config.types[config._mario]:
            height, width = obj.get_size()
            x, y = obj.get_coords()
            x, y = x - 1, y - 1
            self._b[y: y + height, x: x + width] = obj.structure
            return True
        else:
            print("Can't spawn")
            return False

    def render(self):
        # display board at every frame
        sys.stdout.flush()
        try:
            system('clear')
        except BaseException:
            system('cls')
        # sys.stdout.write("\n")
        temp_board = np.matrix(self._b)
        for row in range(self.height):
            for col in range(self.width):
                try:
                    sys.stdout.write(temp_board[row, col].decode())
                except BaseException:
                    sys.stdout.write(temp_board[row, col])
            sys.stdout.write("\n")
        del temp_board
