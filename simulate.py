import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import constants as c
import random
import matplotlib.pylab as plt
from simulation import SIMULATION

simulation = SIMULATION()
simulation.run()










# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
#
# p.setGravity(0,0,c.Gravity_constant)
# planeId = p.loadURDF("plane.urdf")
# robot = p.loadURDF("body.urdf")
#
#
# # targetAngles = numpy.sin(targetAngles * numpy.pi/4)
# #targetAngles = [0]*1000
# BL_targetAngles = numpy.linspace(-numpy.pi, numpy.pi, c.Steps_constant)
# for i in range(len(BL_targetAngles)):
#     BL_targetAngles[i] = c.BL_amplitude * numpy.sin(c.BL_frequency * BL_targetAngles[i] + c.BL_phaseOffset)
#
# FL_targetAngles = numpy.linspace(-numpy.pi, numpy.pi, c.Steps_constant)
# for i in range(len(FL_targetAngles)):
#     FL_targetAngles[i] = c.FL_amplitude * numpy.sin(c.FL_frequency * FL_targetAngles[i] + c.FL_phaseOffset)
#
# #plt.plot(targetAngles)
# #plt.show()
# #numpy.sin(targetAngles / 4.0)
# #targetAngles * (numpy.pi/4.0)
# # # print("test")
# # # print(numpy.sin(targetAngles*numpy.pi/4.0))
# numpy.save("data/BL_targetAngles.npy", (numpy.sin(BL_targetAngles)))
# numpy.save("data/FL_targetAngles.npy", (numpy.sin(FL_targetAngles)))
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate("body.urdf")
# #make empty array the size of for loop
#
# numpy.save("data/backLegData.npy", backLegSensorValues)
# numpy.save("data/frontLegData.npy", frontLegSensorValues)
# p.disconnect()
# print(backLegSensorValues)
# print()
# print(frontLegSensorValues)