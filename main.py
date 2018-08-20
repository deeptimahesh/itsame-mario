#!/home/deepti/anaconda3/bin/python3.6

import random
import board


def main():
    height, width = (24,76)
    bd = board.Board(height, width)
    bd.render()


if __name__ == '__main__':
    main()


