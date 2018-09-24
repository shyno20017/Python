import unit

class Player_Unit(unit.Unit):
	def __init__(self, x, y, symbol, screen, game):
		super().__init__(x, y, symbol, screen, game)

	def update(self, delta_time):
		# Define key handling and stuff here
		c = self.screen.getch()
		if c != -1:
			if c == ord('a'):
				self.x -= 1
			elif c == ord('d'):
				self.x += 1
			elif c == ord('w'):
				self.y -= 1
			elif c == ord('s'):
				self.y += 1
			elif c == 3:
				raise KeyboardInterrupt()

		super().update(delta_time)

	