#!/home/deepti/anaconda3/bin/python3.6

import random
import board
import person
from time import sleep
import config
from os import system
import datetime
from objects import Coin
from colorama import *
import sys


def main():
    height, width = (24, 76)
    quit = False
    won = False
    print("Waking up Mario ...")
    sleep(2)
    print("Yay, he woke up!")
    print("Now, waking up your enemies ...")
    a = 'r'
    while a == 'r':
        bd = board.Board(24, 400)
        player = person.Mario(3, height - 3, 3)
        # while (player.lives > 0):
        bd.spawn(player)


        ls = spawn(config._enemy, bd)
        # ck = spawn_coins(config._coin, bd)

        if ls == False: # or ck == False:
            print("Object Spawn Error")
            return False

        print("Objects spawned, your enemies have been born\n")
        print("Rendering Board ...")

        sleep(3)
        bd.render(0, 76)
        x = 0
        p_input = -1

        st_time = datetime.datetime.now()
        prev_round = datetime.datetime.now()
        while (datetime.datetime.now() - st_time) <= datetime.timedelta(seconds=100):
            # while a=='r':
            sys.stdout.write(Fore.BLUE + "'q' : quit || Lives " + Fore.RED + '%s' % (player.lives * '♥ '))
            sys.stdout.write(' || ' + Fore.BLUE + "Time : %d" % (100 - (datetime.datetime.now() - st_time).seconds))

            try:
                bd.gameover(player)
            except Exception as exc:
                print(exc.args[0])
                break
            print(Style.RESET_ALL)
            p_input = config.get_key(config.get_input())

            if p_input == config.QUIT:
                print(Fore.BLUE + "Quitting game because you're a sore loser ...")
                print("Resetting your clock ...")
                print(Style.RESET_ALL)
                quit = True
                break
            cur_round = datetime.datetime.now()
            if (cur_round - prev_round) >= datetime.timedelta(seconds=1):
                bd.update_frame()
                prev_round = cur_round

            if p_input == config.UP:
                i = 3
                while i > 0:
                    bd.process_input(player, config.UP)
                    bd.render(x, x + 76)
                    inter_input = config.get_key(config.get_input())
                    if inter_input == config.LEFT or inter_input == config.RIGHT or inter_input == config.UP:
                        bd.process_input(player, inter_input)

                    # sleep(0.1)
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

            try:
                bd.gameover(player)
            except Exception as exc:
                sys.stdout.write(exc.args[0])
                break

            for _ in bd._storage[config.types[config._enemy]]:
                while _.get_ycoords() + 2 != 23:
                    res = bd.process_input(_, config.DOWN)
                    if res == False:
                        break

            while player.get_ycoords() != 23:
                # print(player.get_ycoords())
                res = bd.process_input(player, config.DOWN)
                if res == False:
                    break
                bd.render(x, x + 76)
                res = bd.process_input(player, config.DOWN)
                sleep(0.1)

            if player.get_ycoords() == 23:
                player.lives -= 1
            try:
                bd.gameover(player)
            except Exception as exc:
                sys.stdout.write(exc.args[0])
                break


            if player.get_xcoords() >= 360:
                won = True
                sys.stdout.write(Fore.RED + Style.BRIGHT + Back.BLACK + "YOU BEAT THE GAME")
                print(Style.RESET_ALL)
                break

                # sleep(0.1)
                # bd.render()
            """ if (cur_round - prev_round) >= datetime.timedelta(seconds=1):
                # bd.update_frame()
                # prev_round = cur_round"""
            bd.render(x, x + 76)
            if player.get_xcoords() > (x + 38):
                x = x + 6
                bd.render(x, x + 76)

        if player.lives > 0 and won == False:
            sys.stdout.write(Fore.BLUE + "TIME'S UP\n")
        sleep(2)
        bd.clear_storage()

        player.score = (100 - (datetime.datetime.now() - st_time).total_seconds()) * 384

        for player in bd.players:
            if quit:
                sys.stdout.write(Fore.RED + "PLAYER SCORE: 0")
            else:
                sys.stdout.write(Fore.RED + "PLAYER SCORE: %d" % player.score)
        print(Style.RESET_ALL)

        print("Press 'r' to RESTART")
        a = config._getch()
        system('reset')


def spawn(typ, board):
    for _ in range(5):
        x, y = (4, board.height -3)
        if typ == config._enemy:
            e = person.Enemies(x, y)
        else:
            return False
        run_count = 0
        while True:
            new_x, new_y = random.choice(board.init_points)
            if e.update_location(board, new_x, new_y, True):
                break
            run_count += 1
        board.add_storage(e)

    return True

'''def spawn_coins(typ, board):
    for _ in range(10):
        x, y = (1,1)
        if typ == config._coin:
            e = Coin(x, y)
        else:
            return False
        while True:
            new_x, new_y = random.choice(board.init_points)
            board[new_x,new_y] = config._coin
            break
        board.add_storage(e)
'''


if __name__ == '__main__':
    main()
