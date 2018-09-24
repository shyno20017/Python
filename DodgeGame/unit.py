import random

class Unit:
	def __init__(self, x, y, symbol, screen, game):
		self.screen = screen
		self.x = x
		self.y = y
		self.symbol = symbol
		self.game = game
	
	def draw(self):
		self.screen.move(self.y, self.x)
		self.screen.addstr(self.symbol)

	def undraw(self):
		pass

	def update(self, delta_time):
		pass

	@property
	def screen_width(self):
		return self.screen.getmaxyx()[1]

	@property
	def screen_height(self):
		return self.screen.getmaxyx()[0]

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
			if value < 0 or value > 1000:  # screen.getmaxyx[1] - 1:
				raise Exception("Set X position: X position {} is out of bounds".format(value))

			self.undraw()
			self.__dict__['x'] = value
		elif name == 'y':
			try:
				if value != int(value):
					raise Exception("Set Y position: Y position {} is not int".format(value))
			except:
				raise Exception("Set Y position: Y position {} is not int".format(value))

			value = int(value)
			if value < 0 or value > 1000:   # screen.getmaxyx[0] - 1:
				raise Exception("Set Y position: Y position {} is out of bounds".format(value))

			self.undraw()
			self.__dict__['y'] = value
		elif name == 'symbol':
			try:
				str(value)
			except:
				raise Exception("Set Symbol: Value {} is not str".format(value))

			value = str(value)
			if len(value) != 1:
				raise Exception("Set Symbol: Value {} is not str with length 1".format(value))

			self.undraw()
			self.__dict__['symbol'] = value
		else:
			self.__dict__[name] = value

	def __repr__(self):
		return self.__class__.__name__ + "({}, {}, {}, {})".format(self.x, self.y, self.symbol, self.screen)

