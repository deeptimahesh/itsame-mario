#!/home/deepti/anaconda3/bin/python3.6

import random
import board
import person
from time import sleep
import config
from os import system


def main():
    height, width = (24, 76)
    a = 'r'
    while a == 'r':
        bd = board.Board(height, width)
        player = person.Mario(3, height - 3, 3)
        print("Waking up Mario")
        bd.spawn(player)
        print("Yay, he woke up!")
        sleep(3)
        bd.render()
        while a == 'r':
            p_input = config.get_key(config.get_input())

            if p_input == config.QUIT:
                break
            if p_input == config.UP:
                i = 6
                while i > 3:
                    bd.process_input(player, config.UP)
                    bd.render()
                    inter_input = config.get_key(config.get_input())
                    if inter_input == config.LEFT or inter_input == config.RIGHT:
                        bd.process_input(player, inter_input)

                    #sleep(0.1)
                    i = i - 1

                while i > 0:
                    if i == 2:
                        sleep(0.2)
                    bd.process_input(player, config.DOWN)
                    bd.render()
                    # inter_input = config.get_key(config.get_input())
                    # bd.process_input(player, inter_input)
                    # bd.render()
                    sleep(0.1)
                    i = i - 1

            # cur_round = datetime.datetime.now()
            if p_input == config.LEFT or p_input == config.RIGHT:
                bd.process_input(player, p_input)
            """ if (cur_round - prev_round) >= datetime.timedelta(seconds=1):
                # bd.update_frame()
                # prev_round = cur_round"""

            bd.render()

        a = config._getch()
        system('reset')


if __name__ == '__main__':
    main()
