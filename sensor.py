import pyrosim.pyrosim as pyrosim
import numpy
import constants as c


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.Steps_constant)

    def Get_Value(self, timeStep):
        self.values[timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if timeStep == (c.Steps_constant - 1):
            pass
            # print("Sensor Values for ... " + self.linkName)
            # print(self.values)

    def saveValues(self):
        numpy.save("data/" + self.linkName + "SensorValues.npy", self.values)