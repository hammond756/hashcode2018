__author__ = 'Aron'

from loadRides import loadCsv
from Car import Car
from Scenario import Scenario
import os

scenario, rides = loadCsv(os.path.join('data', 'a_example.in'))
cars = [Car(i) for i in range(scenario.cars)]

i = 0
for ride in rides:
    scores = []

    tranches = {'bonus' : [], 'succeed' : [], 'fail' : []}
    tranches['bonus'] = list(filter(lambda x: x.willEarnBonus(ride), cars))
    tranches['succeed'] = list(filter(lambda x: x.willEndInTime(ride) and not x.willEarnBonus(ride), cars))
    tranches['fail'] = list(filter(lambda x: not x.willEndInTime(ride), cars))

    if len(tranches['bonus']) > 0: car = min(tranches['bonus'], key=lambda x: x.wastedTime(ride))
    elif len(tranches['succeed']) > 0: car = min(tranches['succeed'], key=lambda x: x.wastedTime(ride))
    else: continue

    car.assign(ride)

for car in cars:
    print(car.schedule)