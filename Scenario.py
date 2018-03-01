
class Scenario:
	def __init__ (self, line):
		things = line.split()
		self.rows = int(things[0])
		self.cols = int(things[1])
		self.cars = int(things[2])
		self.rides = int(things[3])
		self.bonus = int(things[4])
		self.steps = int(things[5])

	def __str__ (self):
		return "Scenario: field({},{}) with {} cars and {} rides within {} steps with {} bonus.".format(
			self.rows, self.cols, self.cars, self.rides, self.steps, self.bonus)