import queue
import airplane
import random as rand

airplanes = ["MD-82", "MD-83", "E190", "787", "777", "767", "757", "737 MAX", "737", "A350", "A330", "A321neo",
             "A321", "A320", "A319"]

# These are inaccurate, but based off of the MTOW (max take-off weight) of the 777-300ER (so at least somewhat realistic)
weights = [600000, 600000, 625000, 795000, 775000, 765000, 760000, 755000, 740000, 835000,
           820000, 822500, 822500, 825000, 800000]

maxPass = [140, 140, 99, 285, 310, 209, 188, 172, 160, 342, 291, 284, 181, 150, 128]

airlines = ["American", "Alaska", "Delta", "JetBlue", "United", "Southwest", "Frontier", "Sun Country", "Spirit",
            "Allegiant", "Silver", "Ravn Alaska", "Mesa", "Virgin", "National", "Cape Air", "Horizon", "CommutAir",
            "Island", "Trans States", "ATI", "Xtra", "Vision", "Republic", "ABX", "Comair", "ExpressJet", "FedEx", "UPS"]

designations = ["HEAVY", "SUPER"]


iterations = 2

#Populate the air with planes.
for i in range(iterations):
    flight = queue.Queue()
    grounded = queue.Queue()

    airPop = rand.randint(30, 60)

    # Within that range, construct that many airplanes from the above constructor list values.
    for a in range(airPop):
        # Get a random integer between index 0 and the length of the airplanes list. This integer is used to populate
        # the passenger amount and estimated weight for the airplane.
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

        # UPS and FedEx planes will not have passengers, only packages! Keep the weight, drop the passengers.
        if plane.getAirline() == "FedEx" or plane.getAirline() == "UPS":
            plane.setPassengers(rand.randint(4, 9))
        else:
            plane.setPassengers(passengers)

        plane.setWeight(totalWeight)

        # Check if the plane is either a Boeing 700 series plane (HEAVY designation)
        # or an Airbus plane (SUPER designation), and append to end of name if it is.
        if planeIter >= 3 and planeIter <= 5:
            plane.setName(airplanes[planeIter] + "-" + designations[0])
        elif planeIter > 8 and planeIter < len(airplanes):
            plane.setName(airplanes[planeIter] + "-" + designations[1])
        else:
            plane.setName(airplanes[planeIter])

        flight.enqueue(plane)

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

    slots = 30
    minutes = 86400

    # Simulation with 30 slot airport. All planes in the air grounded once.
    totalAirtime = 0
    totalIdle = 0
    avgAirtime = 0
    avgIdle = 0
    totalPass = 0
    avgPass = 0
    totalWgt = 0
    avgWgt = 0

    # for a in range(minutes):
    #     for a in range(flight.size()):
    #         cPln = flight.dequeue()
    #         if grounded.size() < slots:
    #             grounded.enqueue(cPln)
    #         else:
    #             flight.enqueue(cPln)
    #
    #     # Increment everyone's time spent in air by one second.
    #     for b in range(flight.size()):
    #         pln = flight.dequeue()
    #         pln.setAirtime(pln.getAirtime() + 1)
    #
    #     # Increment everyone's time spent grounded by one second.
    #     for c in range(grounded.size()):
    #         gPln = grounded.dequeue()
    #         gPln.setGroundtime(gPln.getGroundtime() + 1)
    #
    #     # If all planes have waited 15 minutes and the compliment probability is exceeded,
    #     # let one plane take off.
    #     if a % 900 == 0 and (rand.uniform(0, 1) > .38) and grounded.size() != 0:
    #         flight.enqueue(grounded.dequeue())
    #
    #     # If all planes have waited 31 minutes and the compliment probability is exceeded,
    #     # let one plane take off.
    #     if a % 1801 == 0 and (rand.uniform(0, 1) > .07) and grounded.size() != 0:
    #         flight.enqueue(grounded.dequeue())

    for a in range(flight.size()):
        if flight.size() > 0:
            pln = flight.dequeue()

            totalAirtime += pln.getAirtime()
            totalIdle += pln.getGroundtime()
            totalWgt += pln.getWeight()
            totalPass += pln.getPassengers()

            flight.enqueue(pln)

    for a in range(grounded.size()):
        if grounded.size() > 0:
            pln = grounded.dequeue()

            totalAirtime += pln.getAirtime()
            totalIdle += pln.getGroundtime()
            totalWgt += pln.getWeight()
            totalPass += pln.getPassengers()

            grounded.enqueue(pln)

    avgAirtime = round((totalAirtime / (grounded.size() + flight.size() + 1)) / 60, 2)
    avgIdle = round((totalIdle / (grounded.size() + flight.size() + 1)) / 60, 2)
    avgWgt = round(totalWgt / (grounded.size() + flight.size() + 1), 2)
    avgPass = round(totalPass / (grounded.size() + flight.size() + 1), 2)

    print("Iteration " + str(i + 1) + ":\tAvg Airtime: " + str(avgAirtime) + " min\tAvg Idle: " + str(
            avgIdle) + " min\tAvg Weight: " + str(avgWgt) + " lbs\tAvg Passengers: " + str(avgPass))