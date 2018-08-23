'''
    Contains the board class
'''

import sys
from os import system
from config import x_fac, y_fac
import numpy as np
import config
import random
from objects import Ground, Brick, Question, Pipe
from colorama import *
import person


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

        self._storage = {
            # config.types[config._bricks]: [],
            config.types[config._enemy]: []
        }

        self.players = []

    '''def init_board(self, reset=False):
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
        # and dividing by two for range of motion'''

    def init_board(self, reset=False):
        if reset:
            self.frame_counter = 0
        w = Ground(self.width / 20, self.height / 20)
        w_height, w_width = w.get_size()
        # creating the rows
        full_row, full_row[:, :] = np.chararray((w_height, self.width)), config._ground
        # assigning top and bottom
        self._b[-w_height:, :] = full_row

        b = Brick(self.width / 20, self.height / 20)
        q = Question(self.width / 20, self.height / 20)
        b_height, b_width = b.get_size()
        q_height, q_width = q.get_size()

        p = Pipe(4,6)
        p_height, p_width = p.get_size()

        noground, noground[:, :] = np.chararray((w_height, w_width)), config._empty
        brick, brick[:, :] = np.chararray((b_height, b_width)), config._bricks
        question, question[:, :] = np.chararray((q_height, q_width)), config._question
        pipe, pipe[:, :] = np.chararray((p_height, p_width)), config._pipe

        self._b[-10:-8, 24:24 + q_width] = question

        self._b[-10:-8, 39:39 + b_width] = brick
        self._b[-10:-8, 42:42 + q_width] = question
        self._b[-10:-8, 45:45 + b_width] = brick
        self._b[-10:-8, 48:48 + q_width] = question
        self._b[-10:-8, 51:51 + b_width] = brick

        self._b[-16:-14, 45:45 + q_width] = question

        self._b[-2-p_height:-2, 63:63+p_width] = pipe

        p = Pipe(6, 6)
        p_height, p_width = p.get_size()
        pipe, pipe[:, :] = np.chararray((p_height, p_width)), config._pipe

        self._b[-2 - p_height:-2, 81:81 + p_width] = pipe

        p = Pipe(8, 6)
        p_height, p_width = p.get_size()
        pipe, pipe[:, :] = np.chararray((p_height, p_width)), config._pipe

        self._b[-2 - p_height:-2, 99:99 + p_width] = pipe
        self._b[-2 - p_height:-2, 117:117 + p_width] = pipe

        self._b[-10:-8, 138:138 + b_width] = brick
        self._b[-2:, 147:147+w_width] = noground
        self._b[-2:, 150:150 + w_width] = noground
        self._b[-2:, 153:153 + w_width] = noground

        self._b[-16:-14, 160:160 + b_width] = brick
        self._b[-16:-14, 163:163 + b_width] = brick
        self._b[-16:-14, 166:166 + b_width] = brick

        self._b[-16:-14, 177:177 + b_width] = brick
        self._b[-16:-14, 180:180 + q_width] = question
        self._b[-16:-14, 183:183 + q_width] = question
        self._b[-16:-14, 186:186 + b_width] = brick

        self._b[-10:-8, 174:174 + b_width] = brick
        self._b[-10:-8, 177:177 + b_width] = brick

        for i in range(5):
            self._b[-2 - b_height:-2, 207 + (3*i):207 + (3*i) + b_width] = brick
        for i in range(4):
            self._b[-4 - b_height:-4, 210 + (3 * i):210 + (3 * i) + b_width] = brick
        for i in range(3):
            self._b[-6 - b_height:-6, 213 + (3 * i):213 + (3 * i) + b_width] = brick
        for i in range(2):
            self._b[-8 - b_height:-8, 216 + (3 * i):216 + (3 * i) + b_width] = brick
        self._b[-10 - b_height:-10, 219:219 + b_width] = brick

        self._b[-2:, 222:222 + w_width] = noground
        self._b[-2:, 225:225 + w_width] = noground
        self._b[-2:, 228:228 + w_width] = noground

        for i in range(5):
            self._b[-2 - b_height:-2, 231 + (3 * i):231 + (3*i) + b_width] = brick
        for i in range(4):
            self._b[-4 - b_height:-4, 231 + (3 * i):231 + (3 * i) + b_width] = brick
        for i in range(3):
            self._b[-6 - b_height:-6, 231 + (3 * i):231 + (3 * i) + b_width] = brick
        for i in range(2):
            self._b[-8 - b_height:-8, 231 + (3 * i):231 + (3 * i) + b_width] = brick
        self._b[-10 - b_height:-10, 231:231 + b_width] = brick

        p = Pipe(6, 6)
        p_height, p_width = p.get_size()
        pipe, pipe[:, :] = np.chararray((p_height, p_width)), config._pipe
        self._b[-2 - p_height:-2, 267:267 + p_width] = pipe

        self._b[-10:-8, 279 + 6:279  + 6 + b_width] = brick
        self._b[-10:-8, 282 + 6:282 + 6 + b_width] = brick
        self._b[-10:-8, 285 + 6:285 + 6 + q_width] = question
        self._b[-10:-8, 288 + 6:288 + 6 + b_width] = brick

        p = Pipe(4, 6)
        p_height, p_width = p.get_size()
        pipe, pipe[:, :] = np.chararray((p_height, p_width)), config._pipe
        self._b[-2 - p_height:-2, 318:318 + p_width] = pipe

        for i in range(6):
            self._b[-2 - b_height:-2, 324 + (3 * i):324 + (3 * i) + b_width] = brick
        for i in range(5):
            self._b[-4 - b_height:-4, 327 + (3 * i):327 + (3 * i) + b_width] = brick
        for i in range(4):
            self._b[-6 - b_height:-6, 330 + (3 * i):330 + (3 * i) + b_width] = brick
        for i in range(3):
            self._b[-8 - b_height:-8, 333 + (3 * i):333 + (3 * i) + b_width] = brick
        for i in range(2):
            self._b[-10 - b_height:-10, 336 + (3 * i):336 + (3 * i) + b_width] = brick
        self._b[-12 - b_height:-12, 339:339 + b_width] = brick
        # DYING A SLOW DEATH
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
        self.init_board(reset)
        self.clear_storage()
        # self.clear_storage()

    def draw_obj(self, obj):
        # draws the object on the board
        if self.path_check(obj):
            height, width = obj.get_size()
            x, y = obj.get_coords()
            self._b[y - 1: y - 1 + height, x - 1: x - 1 + width] = obj.structure
            return True

        return False

    def path_check(self, obj):
        # check if new binding space is occupied else if occupied'''

        height, width = obj.get_size()
        x_pos, y_pos = obj.get_coords()

        emp_comp = np.chararray(obj.get_size())

        emp_comp[:, :] = config._empty

        if obj.get_type() == config.types[config._enemy]:
            for player in self.players:
                x, y = player.get_coords()
                x1, y1 = obj.get_coords()
                x = x + 6
                if x == x1 and y == y1:
                    player.lives -= 1
                    return True
                x = x - 6
                if x == x1 and y == y1:
                    player.lives -= 1
                    return True

        elif obj in self.players:
            for enemy in self._storage[config.types[config._enemy]]:
                x, y = obj.get_coords()
                x1, y1 = enemy.get_coords()
                x = x + 6
                if x==x1 and y==y1:
                    # if obj.get_coords() == enemy.get_coords():
                    obj.lives -= 1
                    return True
                x = x - 6
                if x == x1 and y == y1:
                    obj.lives -= 1
                    return True

        return np.all(self._b[y_pos - 1: y_pos - 1 + height, x_pos - 1: x_pos - 1 + width] == emp_comp)

    def clear_obj(self, obj):
        # clears the object from the board by an object'''
        if obj.get_type() != config.types[config._ground]:
            height, width = obj.get_size()
            x, y = obj.get_coords()
            self._b[y - 1: y - 1 + height, x - 1: x - 1 + width] = config._empty
            return True
        return False

    def spawn(self, obj):
        # method to spawn the main player'''
        if obj.get_type() == config.types[config._mario]:
            height, width = obj.get_size()
            x, y = obj.get_coords()
            print(x)  # 3
            print(y)  # 21
            x, y = x - 1, y - 1  # 2,20
            self._b[y: y + height, x: x + width] = obj.structure
            self.players.append(obj)
            return True
        else:
            print("Can't spawn")
            return False

    #def isGround(self, obj):
     #   if obj.get_type() == config.types[config._mario]:
      #      height, width = obj.get_size()
       #     x, y = obj.get_coords()
        #    y = y + 2
         #   return np.any(self._b[y + 2: y + 4, x: x + 3]) == Ground(0, 0).structure

    def process_input(self, player, key_press):
        res = False
        if key_press in config.DIR:
            x, y = player.get_coords()
            if key_press == config.UP:
                y -= config.y_fac
            elif key_press == config.DOWN:
                y += config.y_fac
            elif key_press == config.LEFT:
                x -= config.x_fac
            elif key_press == config.RIGHT:
                x += config.x_fac
            res = player.update_location(self, x, y)
        return res

    def update_frame(self):
        for _ in self._storage[config.types[config._enemy]]:
            _dir = random.choice(config.DIR)
            self.process_input(_, _dir)

        self.frame_counter += 1

    def add_storage(self, obj):
        try:
            if obj not in self._storage[obj.get_type()]:
                self._storage[obj.get_type()].append(obj)
                return True
            else:
                return None
        except KeyError:
            return False

    def clear_storage(self, obj=None):
        '''# clear the objects on the board at every instance'''
        if obj is None:
            for object_type in self._storage:
                for object_ in self._storage[object_type]:
                    del object_
                self._storage[object_type] = []
            return True
        else:
            typ = obj.get_type()
            try:
                self._storage[typ].remove(obj)
                return True
            except BaseException:
                return False

    '''def render(self, x, y):
        # display board at every frame
        sys.stdout.flush()
        try:
            system('clear')
        except BaseException:
            system('cls')
        # sys.stdout.write("\n")
        temp_board = np.matrix(self._b)
        for row in range(self.height):
            for col in range(x, y):
                try:
                    sys.stdout.write(temp_board[row, col].decode())
                except BaseException:
                    sys.stdout.write(temp_board[row, col])
            sys.stdout.write("\n")
        del temp_board'''

    def gameover(self, player):
        if player.lives == 0:
            raise Exception(Style.BRIGHT + Fore.RED + "\nNO LIVES LEFT, IT'S GAME OVER, AMIGO")
        return True

    def render(self, x, y):
        # display board at every frame
        sys.stdout.flush()
        try:
            system('clear')
        except BaseException:
            system('cls')
        # sys.stdout.write("\n")
        temp_board = np.matrix(self._b)
        for row in range(self.height):
            for col in range(x,y):
                try:
                    if temp_board[row, col].decode() == config._ground:
                        sys.stdout.write(Back.GREEN + " ") # temp_board[row, col].decode())
                    elif temp_board[row, col].decode() == config._bricks or temp_board[row, col].decode() == '\\':
                        sys.stdout.write(Back.BLACK + temp_board[row, col].decode())
                    elif temp_board[row, col].decode() == config._question:
                        sys.stdout.write(Back.YELLOW + temp_board[row, col].decode())
                    elif temp_board[row, col].decode() == config._empty:
                        sys.stdout.write(Back.BLUE + temp_board[row, col].decode())
                    elif temp_board[row, col].decode() == config._pipe:
                        sys.stdout.write(Back.RED + temp_board[row, col].decode())
                    elif temp_board[row, col].decode() == 'M':
                        sys.stdout.write(Back.MAGENTA + temp_board[row, col].decode())
                    elif temp_board[row, col].decode() == 'E':
                        sys.stdout.write(Back.CYAN + temp_board[row, col].decode())
                except BaseException:
                    sys.stdout.write(temp_board[row, col])
            sys.stdout.write("\n")
        print(Style.RESET_ALL)
        del temp_board
