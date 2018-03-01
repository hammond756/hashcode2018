__author__ = 'Aron'

class Car:

    def __init__(self, i):
        self.id = i
        self.row = 0
        self.col = 0
        self.t = 0
        self.schedule = []

    def assign(self, ride):
        self.row, self.col, self.t = ride.endRow, ride.endCol, (self.t + self.travelTime(ride))
        self.schedule.append(ride.id)

    def willEndInTime(self, ride):
        # print("Ride length: {}, Car Position: ({},{}), Ride Position ({},{}), Dest ({},{})".format(len(ride),
        #                                                                                            self.row,
        #                                                                                            self.col,
        #                                                                                            ride.startRow,
        #                                                                                            ride.startCol,
        #                                                                                            ride.endRow,
        #                                                                                            ride.endCol))
        return self.t + self.timeToTravelToRideStart(ride) + len(ride) <= ride.end

    def willEarnBonus(self, ride):
        return self.t + self.timeToTravelToRideStart(ride) < ride.start

    def travelTime(self, ride):
        return max(self.timeToTravelToRideStart(ride), (ride.start - self.t)) + len(ride)

    def timeToTravelToRideStart(self, ride):
        time = abs(self.row - ride.startRow) + abs(self.col - ride.startCol)
        return time

    def wastedTime(self, ride):
        return max(ride.start - self.t, self.timeToTravelToRideStart(ride))