import numpy

amplitude = numpy.pi/4
frequency = 12
offset = numpy.pi

FL_amplitude = numpy.pi/4
FL_frequency = 12
FL_phaseOffset = -numpy.pi

BL_amplitude = numpy.pi/4
BL_frequency = 6
BL_phaseOffset = numpy.pi

Gravity_constant = -9.8

Steps_constant = 1000

s = 4 #number of sensors on robot
m = 8 #number of motors on robot

currentGenerations = 10

populationSize = 10

numSensorNeurons = 4
numMotorNeurons = 8

motorJointRange = 0.5