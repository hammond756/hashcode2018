from Car import Car

def writeOutput(cars, input_file):

	output_file = input_file.split(".")[0] + "_answers.in"
	f = open(output_file, 'w')
	for car in cars:
		f.write("{}".format(len(car)))
		for ride in car:
			f.write(" {}".format(ride))
		f.write("\n")