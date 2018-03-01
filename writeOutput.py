from Car import Car

def writeOutput(cars, input_file):

	output_file = "data/" + input_file.split(".")[0] + "_answers.out"
	f = open(output_file, 'w')
	for car in cars:
		f.write("{}".format(len(car.schedule)))
		for ride in car.schedule:
			f.write(" {}".format(ride))
		f.write("\n")