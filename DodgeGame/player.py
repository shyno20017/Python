from unit import Unit
from wrapcurses import KEY

class Player_Unit(Unit):
	def __init__(self, x, y, symbol, screen, game, modifier = 0):
		super().__init__(x, y, symbol, screen, game, modifier)

	def update(self, delta_time):
		# Define key handling and stuff here
		c = self.screen.getch()
		if c != -1:
			if c in [KEY.A, KEY.a, KEY.LEFT_KEY, KEY.FOUR, KEY.NUMPAD_4]:
				if self.x > 0:
					self.x -= 1
			elif c in [KEY.D, KEY.d, KEY.RIGHT_KEY, KEY.SIX, KEY.NUMPAD_6]:
				if self.x < self.screen.width - 2:
					self.x += 1
			elif c in [KEY.W, KEY.w, KEY.UP_KEY, KEY.EIGHT, KEY.NUMPAD_8]:
				if self.y > 0:
					self.y -= 1
			elif c in [KEY.S, KEY.s, KEY.DOWN_KEY, KEY.TWO, KEY.NUMPAD_2]:
				if self.y < self.screen.height - 1:
					self.y += 1
			elif c in [KEY.P, KEY.p]:
				self.game.pause()
			elif c == 3:
				raise KeyboardInterrupt()

		super().update(delta_time)
