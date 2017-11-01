class Airplane:
    def __init__(self):
        self.airline = ""
        self.name = ""
        self.designate = ""
        self.weight = 0
        self.passengers = 0
        self.airTime = 0
        self.groundTime = 0
        self.isGrounded = False

    def setAirline(self, air):
        self.airline = air

    def getAirline(self):
        return self.airline

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setWeight(self, wgt):
        self.weight = wgt

    def getWeight(self):
        return self.weight

    def setPassengers(self, num):
        self.passengers = num

    def getPassengers(self):
        return self.passengers

    def setAirtime(self, time):
        self.airTime = time

    def getAirtime(self):
        return self.airTime

    def setGroundtime(self, time):
        self.groundTime = time

    def getGroundtime(self):
        return self.groundTime

    def setIsGrounded(self, x):
        self.isGrounded = x

    def getIsGrounded(self):
        return self.isGrounded