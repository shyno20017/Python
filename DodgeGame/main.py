from wrapcurses import Screen, COLOR, KEY, MODIFIER
from game import Game
import time

def main():
	stdscr = Screen()
	game = Game(stdscr)
	game.run()
	stdscr.end()

if __name__ == "__main__":
	main()
