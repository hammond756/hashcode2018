
class Ride :
	def __init__ (self, line, id):
		self.id = id
		things = line.split()
		self.startRow = int(things[0])
		self.startCol = int(things[1])
		self.endRow = int(things[2])
		self.endCol = int(things[3])
		self.start = int(things[4])
		self.end = int(things[5])

	def __len__ (self):
		return abs(self.startRow - self.endRow) + abs(self.startCol - self.endRow)

	def __str__ (self):
		return "ride #{}: from ({},{}) to ({},{}) between {} and {}".format(
			self.id, self.startRow, self.startCol, self.endRow, self.endCol, self.start, self.end)