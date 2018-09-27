from stopwatch import Stopwatch
from unit import Unit
from player import Player_Unit
from enemy import Enemy_Unit
from wrapcurses import KEY, COLOR, MODIFIER

from random import randint
import time

class Game:
	NUM_ENEMIES = 20

	def __init__(self, screen):
		self.watch = Stopwatch()
		self.screen = screen

		self.game_window = screen.create_window(0, 0, self.screen.width, self.screen.height - 1) # This -1 leaves the last line blank for the score

		self.player_color = self.screen.create_color(COLOR.CYAN, COLOR.BLACK) + MODIFIER.BOLD
		self.enemy_color = self.screen.create_color(COLOR.RED, COLOR.BLACK) + MODIFIER.BOLD
		self.score_color = self.screen.create_color(COLOR.YELLOW, COLOR.BLACK) + MODIFIER.BOLD

		self.score = 0

		self.screen.nodelay(True)
		self.screen.noecho()
		self.screen.cursor_set(False)
		self.screen.keypad(True)

		self.game_window.nodelay(True)
		self.game_window.noecho()
		self.game_window.cursor_set(False)
		self.game_window.keypad(True)

		self.player = Player_Unit(self.screen.width // 2, self.screen.height // 2, "@", self.game_window, self, self.player_color)
		self.enemies = []

		# Set enemies at far edge of screen at a random row
		for u in range(self.NUM_ENEMIES):
			rand_row = randint(0, self.game_window.height - 1)
			enemy = Enemy_Unit(self.game_window.width - 2, rand_row, "X", self.game_window, self, self.enemy_color)
			self.enemies.append(enemy)

	def run(self):
		self.watch.start()
		time_at_last_frame = self.watch.timeMS
		alive = True
		while alive:
			delta_time = self.watch.timeMS - time_at_last_frame
			time_at_last_frame = self.watch.timeMS

			# Every 50 points, add an enemy
			# This is done by checking the number of enemies
			# If it is less than it is supposed to be,
			# Then add an Enemy_Unit
			if len(self.enemies) < (self.NUM_ENEMIES + self.score // 1):
				rand_row = randint(0, self.game_window.height - 1)
				enemy = Enemy_Unit(self.game_window.width - 2, rand_row, "X", self.game_window, self, self.enemy_color)
				self.enemies.append(enemy)

			# Update All Units
			self.player.update(delta_time)
			for enemy in self.enemies:
				enemy.update(delta_time)

			# Check if any enemy collides with the player
			for enemy in self.enemies:
				if self.player.collide(enemy):
					alive = False

			# Clear the screen before drawing
			self.screen.clear()
			self.game_window.clear()

			# Draw all units
			self.player.draw()
			for enemy in self.enemies:
				enemy.draw()

			# Draw the score on the bottom row (where there are no enemies)
			self.draw_score()

			# Refresh the screen to display the drawings
			self.screen.refresh()
			self.game_window.refresh()
			time.sleep(0.005) # To ensure the program does not use 100% of CPU

		self.screen.clear()
		self.screen.nodelay(False)
		self.screen.addstr("You Lose: Your score was: {}".format(self.score), x = 0, y = self.screen.height // 2 - 1)
		print("You Lose: Your score was: {}".format(self.score))
		self.screen.refresh()
		time.sleep(1.5)
		self.screen.addstr("Press any key to continue...", x = 0, y = self.screen.height - 1)
		self.screen.getch()

	def pause(self):
		self.watch.stop()
		self.screen.clear()
		self.screen.nodelay(False)
		self.screen.addstr("Game is paused. Press (P) to resume...", x = 0, y = self.screen.height // 2 - 1)
		self.screen.refresh()
		key = self.screen.getch()
		while key not in [KEY.P, KEY.p]:
			key = self.screen.getch()

		self.screen.nodelay(True)
		self.screen.clear()
		self.watch.start()

	def draw_score(self):
		self.screen.addstr("Score: {}".format(self.score), mod = self.score_color, x = 0, y = self.screen.height - 1)
