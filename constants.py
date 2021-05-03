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

Gravity_constant = -19.6

Steps_constant = 2500

s = 4 #number of sensors on robot
m = 8 #number of motors on robot

currentGenerations = 10
populationSize = 10

SENSOR_NEURON = "sensor"
MOTOR_NEURON = "motor"
HIDDEN_NEURON = "hidden"


numSensorNeurons = 4
numHiddenNeurons = 2
numMotorNeurons = 8

motorJointRange = 1.25