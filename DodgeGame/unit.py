import random

class Unit:
	def __init__(self, x, y, symbol, screen, game, modifier = 0):
		self.screen = screen
		self.x = x
		self.y = y
		self.symbol = symbol
		self.game = game
		self.modifier = modifier

	def draw(self):
		self.screen.addstr(self.symbol, mod = self.modifier, x = self.x, y = self.y)

	def update(self, delta_time):
		pass

	def randint(self, a, b):
		return random.randint(a, b)

	def collide(self, other):
		return self.x == other.x and self.y == other.y

	def __setattr__(self, name, value):
		if name == 'x':
			try:
				if value != int(value):
					raise Exception("Set X position: X position {} is not int".format(value))
			except:
				raise Exception("Set X position: X position {} is not int".format(value))

			value = int(value)
			if value < 0 or value >= self.screen.width:
				raise Exception("Set X position: X position {} is out of bounds".format(value))

			self.__dict__['x'] = value
		elif name == 'y':
			try:
				if value != int(value):
					raise Exception("Set Y position: Y position {} is not int".format(value))
			except:
				raise Exception("Set Y position: Y position {} is not int".format(value))

			value = int(value)
			if value < 0 or value >= self.screen.height:
				raise Exception("Set Y position: Y position {} is out of bounds".format(value))

			self.__dict__['y'] = value
		elif name == 'symbol':
			try:
				value = str(value)
			except:
				raise Exception("Set Symbol: Value {} is not str".format(value))

			if len(value) != 1:
				raise Exception("Set Symbol: Value {} is not str with length 1".format(value))

			self.__dict__['symbol'] = value
		else:
			self.__dict__[name] = value
