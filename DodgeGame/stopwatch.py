import time

class Stopwatch:
	def __init__(self):
		self.start_time = None
		self.time_passed = 0
		self.stored_time = None
		self.timing = False

	def current_time(self):
		return time.time()

	def update_time(self):
		if self.stored_time is None:
			return

		new_time = self.current_time()
		self.time_passed += new_time - self.stored_time
		self.stored_time = new_time

	def start(self):
		if self.timing:
			return

		if self.start_time is None:
			self.start_time = self.current_time()

		self.timing = True
		self.stored_time = self.current_time()
		self.update_time()

	def stop(self):
		if not self.timing:
			return

		self.timing = False
		self.update_time()
		self.stored_time = None

	def reset(self):
		if self.timing:
			self.start_time = self.current_time()
			self.stored_time = self.current_time()
			self.time_passed = 0
		else:
			self.start_time = None
			self.stored_time = None
			self.time_passed = 0

	@property
	def timeS(self):
		if self.timing:
			self.update_time()

		return self.time_passed

	@property
	def timeMS(self):
		return self.timeS * 1000
