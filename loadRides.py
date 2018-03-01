import csv
from Ride import Ride
from Scenario import Scenario

def loadCsv (file):
	rides = []

	with open(file, 'rb') as f:
		lines = f.readlines()

	scenario = Scenario(lines[0])

	# skip first line in file
	i = 0
	iterlines = iter(lines)
	next(iterlines)
	for line in iterlines:
		ride = Ride(line, i)
		rides.append(ride)
		i += 1

	return scenario,rides


# example
# loadCsv('data/a_example.in')
# print(scenario)
# print(len(rides))
# for ride in rides:
# 	print(ride)