import numpy
import matplotlib.pyplot

#backLegSensorValues = numpy.load('data/backLegData.npy')
#frontLegSensorValues = numpy.load('data/frontLegData.npy')
BL_targetAngles = numpy.load("data/BL_targetAngles.npy")
FL_targetAngles = numpy.load("data/FL_targetAngles.npy")
#print(backLegSensorValues)
#matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 3)
#matplotlib.pyplot.plot(frontLegSensorValues, label="FrontLeg", linewidth = 1)
matplotlib.pyplot.plot(FL_targetAngles, label="Front Leg")
matplotlib.pyplot.plot(BL_targetAngles, label="Back Leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()