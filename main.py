#!/home/deepti/anaconda3/bin/python3.6

import random
import board
import person
from time import sleep
import config
from os import system

def main():
    height, width = (24,76)
    a='r'
    while a=='r':
        bd = board.Board(height, width)
        player = person.Mario(3, height-3, 3)
        print("Waking up Mario")
        bd.spawn(player)
        print("Yay, he woke up!")
        sleep(1)
        bd.render()

        a = config._getch()
        system('reset')


if __name__ == '__main__':
    main()


