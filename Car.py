__author__ = 'Aron'

class Car:

    def __init__(self):
        self.state = (0, 0, 0)
        self.schedule = []

    def assign(self, ride):
        self.state = (ride.endRow, ride.endCol, self.state[3] + self.travelTime(ride))
        self.schelude.append(ride.id)

    def travelTime(self, ride):
        return self.timeToTravelToRideStart(ride) + len(ride)

    def timeToTravelToRideStart(self, ride):
        return abs(self.state[0] - self.state[1]) + abs(ride.startRow - ride.startCol)