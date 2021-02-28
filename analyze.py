import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('data/backLegData.npy')
frontLegSensorValues = numpy.load('data/frontLegData.npy')
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, label = "Back Leg", linewidth = 3)
matplotlib.pyplot.plot(frontLegSensorValues, label="FrontLeg", linewidth = 1)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()