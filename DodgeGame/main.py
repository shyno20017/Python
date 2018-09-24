from unicurses import *
from game import Game


def main():
	stdscr = initscr()
	game = Game(stdscr)
	game.run()
	endwin()

if __name__ == "__main__":
	main()