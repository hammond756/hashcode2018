__author__ = 'Aron'

class Car:

    def __init__(self, i):
        self.id = i
        self.row = 0
        self.col = 0
        self.t = 0
        self.schedule = []

    def assign(self, ride):
        if not self.willEndInTime(ride):
            return False

        self.row, self.col, self.t = ride.endRow, ride.endCol, (self.t + self.travelTime(ride))
        self.schedule.append(ride.id)

    def willEndInTime(self, ride):
        return self.t + self.timeToTravelToRideStart(ride) + len(ride) <= ride.start

    def willEarnBonus(self, ride):
        return self.t + self.timeToTravelToRideStart(ride) < ride.start

    def travelTime(self, ride):
        return max(self.timeToTravelToRideStart(ride), (ride.start - self.t)) + len(ride)

    def timeToTravelToRideStart(self, ride):
        time = abs(self.row - ride.startRow) + abs(self.col - ride.startCol)
        return time

    def wastedTime(self, ride):
        return max(ride.start - self.t, self.timeToTravelToRideStart(ride))