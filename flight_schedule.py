# Joseph Urbanski
# MPCS 50101 Final Exam

import sys

class FlightSchedule():
    flights = []
    plane_identifiers = []

    def read_data_from_file(self):
        infile = open("flight_data.csv", "r")

        for line in infile:
            currline = line.split(',')

            self.flights.append(currline)

            if currline[1] not in self.plane_identifiers:
                self.plane_identifiers.append(currline[1])

    def determine_longest_flight(self):
        longest_flight = 0
        longest_flight_number = 0

        for i in self.flights:
            if int(i[4]) > longest_flight:
                longest_flight = int(i[4])
                longest_flight_number = int(i[0])

        return longest_flight_number
