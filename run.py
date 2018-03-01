__author__ = 'Aron'

from loadRides import loadCsv
from Car import Car
from Scenario import Scenario
import os
from writeOutput import writeOutput


for filename in ['a_example.in', 'b_should_be_easy.in', 'c_no_hurry.in', 'd_metropolis.in', 'e_high_bonus.in']:

    scenario, rides = loadCsv(os.path.join('data', filename))
    cars = [Car(i) for i in range(scenario.cars)]

    print(scenario)

    for ride in rides:
        scores = []

        tranches = {'bonus' : [], 'succeed' : [], 'fail' : []}

        tranches['bonus'] = list(filter(lambda x: x.willEarnBonus(ride), cars))
        tranches['succeed'] = list(filter(lambda x: x.willEndInTime(ride) and not x.willEarnBonus(ride), cars))
        tranches['fail'] = list(filter(lambda x: not x.willEndInTime(ride), cars))

        if len(tranches['bonus']) > 0: car = min(tranches['bonus'], key=lambda x: x.wastedTime(ride))
        elif len(tranches['succeed']) > 0: car = min(tranches['succeed'], key=lambda x: x.wastedTime(ride))
        else:
            continue

        car.assign(ride)


    writeOutput(cars, filename)