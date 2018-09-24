from units import Stopwatch, Unit, Player_Unit, Enemy_Unit
from random import randint
import time

class Game:
	NUM_ENEMIES = 20

	def __init__(self, screen):
		self.watch = Stopwatch()
		self.screen = screen

		self.score = 0
		
		self.screen.nodelay(True)

		self.player = Player_Unit(self.screen_width // 2, self.screen_height // 2, "@", self.screen, self)
		self.enemies = []

		# Set enemies at far edge of screen at a random row
		for u in range(self.NUM_ENEMIES):
			rand_row = randint(0, self.screen_height - 1 - 1) # The second -1 is to avoid spawning an enemy in the last row which would cause an error (and cover the score meter)
			enemy = Enemy_Unit(self.screen_width - 1, rand_row, "X", self.screen, self)
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
			if len(self.enemies) < (self.NUM_ENEMIES + self.score // 50):
				rand_row = randint(0, self.screen_height - 1 - 1) # The second -1 is to avoid spawning an enemy in the last row which would cause an error (and cover the score meter)
				enemy = Enemy_Unit(self.screen_width - 1, rand_row, "X", self.screen, self)
				self.enemies.append(enemy)

			# Update All Units
			self.player.update(delta_time)
			for enemy in self.enemies:
				enemy.update(delta_time)

			# Check if any enemy collides with the player
			for enemy in self.enemies:
				if self.player.collide(enemy):
					alive = False
					
			self.screen.clear() # Clear the screen before drawing

			# Draw all units
			self.player.draw()
			for enemy in self.enemies:
				enemy.draw()

			self.draw_score()

			self.screen.refresh() # Refresh the screen to display the drawings
			time.sleep(0.005) # To ensure the program does not use 100% of CPU

		self.screen.clear()
		self.screen.nodelay(False)
		self.screen.move(self.screen_height // 2 - 1, 0)
		self.screen.addstr("You Lose: Your score was: {}".format(self.score))
		self.screen.refresh()
		time.sleep(1.5)
		self.screen.move(self.screen_height - 1, 0)
		self.screen.addstr("Press any key to continue...")
		self.screen.getch()


	def draw_score(self):
		self.screen.move(self.screen_height - 1, 0)
		self.screen.addstr("Score: {}".format(self.score))

	@property
	def screen_width(self):
		return self.screen.getmaxyx()[1]

	@property
	def screen_height(self):
		return self.screen.getmaxyx()[0]	

