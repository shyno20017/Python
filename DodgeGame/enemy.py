from unit import Unit

class Enemy_Unit(Unit):
	def __init__(self, x, y, symbol, screen, game, modifier = 0):
		super().__init__(x, y, symbol, screen, game, modifier)
		self.time_between_moves = self.randint(100, 150)
		self.time_since_last_move = 0

	def update(self, delta_time):
		# Do AI here
		self.time_since_last_move += delta_time
		if self.time_since_last_move < self.time_between_moves:
			# Not enough time has passed yet
			return

		# Enough time has passed to update
		self.time_since_last_move -= self.time_between_moves
		if self.x < 1:
			self.x = self.screen.width - 2
			self.y = self.randint(0, self.screen.height - 1)
			self.time_between_moves = int(self.time_between_moves * 0.9)
			if self.time_between_moves < 500 // 15:
				self.time_between_moves = 500 // 15

			self.game.score += 1 # Increase the score after each time an enemy reaches the end

		self.x -= 1
		super().update(delta_time)
