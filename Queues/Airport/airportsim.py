import queue
import airplane
import random as rand

airplanes = ["MD-82", "MD-83", "E190", "787", "777", "767", "757", "737 MAX", "737", "A350", "A330", "A321neo",
             "A321", "A320", "A319"]

# These are inaccurate, but based off of the MTOW (max take-off weight) of the 777-300ER
# (so at least somewhat realistic).
weights = [600000, 600000, 625000, 795000, 775000, 765000, 760000, 755000, 740000, 835000,
           820000, 822500, 822500, 825000, 800000]

maxPass = [140, 140, 99, 285, 310, 209, 188, 172, 160, 342, 291, 284, 181, 150, 128]

airlines = ["American", "Alaska", "Delta", "JetBlue", "United", "Southwest", "Frontier", "Sun Country", "Spirit",
            "Allegiant", "Silver", "Ravn Alaska", "Mesa", "Virgin", "National", "Cape Air", "Horizon", "CommutAir",
            "Island", "Trans States", "ATI", "Xtra", "Vision", "Republic", "ABX", "Comair", "ExpressJet", "FedEx", "UPS"]

designations = ["HEAVY", "SUPER"]


iterations = 2


def main():
    # Populate the air with planes.
    for i in range(iterations):

        # Information pulled from the Bureau of Transportation Statistics
        #
        # Average Time Spent Landing to Gate: 6.9 minutes
        #
        # Probability of time spent at gate:
        # .720 ~15 minutes
        # .930 ~30 minutes
        #
        # Average Time Spent Gate to Takeoff: 16.7 minutes
        #

        flights = queue.Queue()

        slots = 30
        minutes = 86400

        inRangeTime = rand.randint(900, 2100)
        landTime = rand.randint(300, 600)
        idleTime = 0

        if rand.uniform(0, 1) < .720:
            idleTime = rand.randint(450, 1349)
        elif rand.uniform(0, 1) < .930:
            idleTime = rand.randint(1350, 2249)
        else:
            idleTime = rand.randint(2250, 3600)

        # Simulation with 30 slot airport. All planes in the air grounded once.
        totalAirtime = 0
        totalIdle = 0
        totalPass = 0
        totalWgt = 0

        for a in range(minutes):
            if a % inRangeTime == 0:
                # Get a random integer between index 0 and the length of the airplanes list.
                # This integer is used to populate the passenger amount and estimated weight
                # for the airplane.
                planeIter = rand.randint(0, len(airplanes) - 1)
                passVal = maxPass[planeIter]
                passengers = rand.randint(int(passVal / 2), passVal)

                # Calculations to determine overall weight of the plane.
                avgPassWgt = rand.randint(100, 300)
                avgPassLugWgt = rand.randint(20, 60)
                weight = weights[planeIter]
                totalWeight = weight + (passengers * avgPassWgt) + (passengers * avgPassLugWgt)

                # Instantiate the plane and populate it with values.
                plane = airplane.Airplane()
                plane.setAirline(rand.choice(airlines))

                # UPS and FedEx planes will not have passengers, only packages!
                # Keep the weight, drop the passengers.
                if plane.getAirline() == "FedEx" or plane.getAirline() == "UPS":
                    plane.setPassengers(rand.randint(4, 9))
                else:
                    plane.setPassengers(passengers)

                plane.setWeight(totalWeight)

                # Check if the plane is either a Boeing 700 series plane (HEAVY designation)
                # or an Airbus plane (SUPER designation), and append to end of name if it is.
                if 3 < planeIter <= 5:
                    plane.setName(airplanes[planeIter] + "-" + designations[0])
                elif 8 < planeIter < len(airplanes):
                    plane.setName(airplanes[planeIter] + "-" + designations[1])
                else:
                    plane.setName(airplanes[planeIter])

                flights.enqueue(plane)


            # if a % landTime == 0:
            #     curPlane = flights.dequeue()
            #     print(str.expandtabs(curPlane.getAirline() + " " + curPlane.getName() + " landing."))
            #     curPlane.setIsGrounded(True)
            #     flights.enqueue(curPlane)
            #
            # if a % idleTime == 0:
            #     for x in range(flights.size()):
            #         curPlane = flights.dequeue()
            #         if curPlane.getIsGrounded():
            #             print(str.expandtabs(curPlane.getAirline() + " " + curPlane.getName() + " taking off."))
            #             curPlane.setIsGrounded(False)
            #         else:
            #             flights.enqueue(curPlane)
            #
            # for y in range(flights.size()):
            #     curPlane = flights.dequeue()
            #     if curPlane.getIsGrounded():
            #         curPlane.setGroundtime(curPlane.getGroundtime() + 1)
            #     else:
            #         curPlane.setAirtime(curPlane.getAirtime() + 1)
            #
            # for a in range(flights.size()):
            #     if flights.size() > 0:
            #         pln = flights.dequeue()
            #
            #         totalAirtime += pln.getAirtime()
            #         totalIdle += pln.getGroundtime()
            #         totalWgt += pln.getWeight()
            #         totalPass += pln.getPassengers()
            #
            #         flights.enqueue(pln)
            #
            # avgAirtime = round(div(totalAirtime, flights.size()) / 60, 2)
            # avgIdle = round(div(totalIdle, flights.size()) / 60, 2)
            # avgWgt = round(div(totalWgt, flights.size()), 2)
            # avgPass = round(div(totalPass, flights.size()), 2)
            #
            # print("Iteration " + str(i + 1) + ":\tAvg Airtime: " + str(avgAirtime) + " min\tAvg Idle: " + str(
            #         avgIdle) + " min\tAvg Weight: " + str(avgWgt) + " lbs\tAvg Passengers: " + str(avgPass))

    for a in range(flights.size()):
        pln = flights.dequeue()
        print(str.expandtabs("Name: " + pln.getAirline() + " " + pln.getName() + "\tTotal Weight: " + str(pln.getWeight()) + " lbs.\tTotal Passengers: " + str(pln.getPassengers()), 35))

def div(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return 0

if __name__ == '__main__':
    main()