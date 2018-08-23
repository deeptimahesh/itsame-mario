#!/home/deepti/anaconda3/bin/python3.6

import random
import board
import person
from time import sleep
import config
from os import system
import datetime


def main():
    height, width = (24, 76)
    a = 'r'
    while a == 'r':
        bd = board.Board(24, 400)
        player = person.Mario(3, height - 3, 3)
        print("Waking up Mario")
        bd.spawn(player)
        print("Yay, he woke up!")
        sleep(3)
        bd.render(0,76)
        x = 0
        p_input = -1
        st_time = datetime.datetime.now()
        prev_round = datetime.datetime.now()
        # while (datetime.datetime.now() - st_time) <= datetime.timedelta(seconds=100):
        while a=='r':
            p_input = config.get_key(config.get_input())

            if p_input == config.QUIT:
                break
            cur_round = datetime.datetime.now()
            if (cur_round - prev_round) >= datetime.timedelta(seconds=1):
                prev_round = cur_round

            if p_input == config.UP:
                i = 3
                while i > 0:
                    bd.process_input(player, config.UP)
                    bd.render(x, x + 76)
                    inter_input = config.get_key(config.get_input())
                    if inter_input == config.LEFT or inter_input == config.RIGHT or inter_input == config.UP :
                        bd.process_input(player, inter_input)

                    #sleep(0.1)
                    i = i - 1

                '''while i > 0:
                    if i == 2:
                        sleep(0.2)
                    bd.process_input(player, config.DOWN)
                    bd.render()
                    # inter_input = config.get_key(config.get_input())
                    # bd.process_input(player, inter_input)
                    # bd.render()
                    sleep(0.1)
                    i = i - 1'''
                '''while player.get_ycoords()+2 != 23:
                    # print(player.get_ycoords())
                    bd.process_input(player, config.DOWN)
                    bd.render()
                    sleep(0.1)
                '''

            # cur_round = datetime.datetime.now()
            if p_input == config.LEFT or p_input == config.RIGHT:
                bd.process_input(player, p_input)

            while player.get_ycoords() + 2 != 23:
                # print(player.get_ycoords())
                res = bd.process_input(player, config.DOWN)
                if res == False:
                    break
                bd.render(x, x + 76)
                sleep(0.1)

                # sleep(0.1)
                # bd.render()
            """ if (cur_round - prev_round) >= datetime.timedelta(seconds=1):
                # bd.update_frame()
                # prev_round = cur_round"""
            bd.render(x, x + 76)
            if player.get_xcoords() > (x + 38):
                x = x + 6
                bd.render(x, x + 76)

        a = config._getch()
        system('reset')


if __name__ == '__main__':
    main()
