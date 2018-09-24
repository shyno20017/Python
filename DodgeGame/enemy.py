import unit

class Enemy_Unit(unit.Unit):
	def __init__(self, x, y, symbol, screen, game):
		super().__init__(x, y, symbol, screen, game)
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
			self.x = self.screen_width - 1
			self.y = self.randint(0, self.screen_height - 1 - 1) # The second -1 is to avoid spawning an enemy in the last row which would cause an error (and cover the score meter)
			self.time_between_moves = int(self.time_between_moves * 0.9)
			if self.time_between_moves < 500 // 15:
				self.time_between_moves = 500 // 15

			self.game.score += 1 # Increase the score after each time an enemy reaches the end

		self.x -= 1
		super().update(delta_time)