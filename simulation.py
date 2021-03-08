import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy
import random
import matplotlib.pylab as plt


FL_amplitude = numpy.pi/4
FL_frequency = 12
FL_phaseOffset = -numpy.pi

BL_amplitude = numpy.pi/4
BL_frequency = 6
BL_phaseOffset = numpy.pi

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robot = p.loadURDF("body.urdf")


# targetAngles = numpy.sin(targetAngles * numpy.pi/4)
#targetAngles = [0]*1000
BL_targetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)
for i in range(len(BL_targetAngles)):
    BL_targetAngles[i] = BL_amplitude * numpy.sin(BL_frequency * BL_targetAngles[i] + BL_phaseOffset)

FL_targetAngles = numpy.linspace(-numpy.pi, numpy.pi, 1000)
for i in range(len(FL_targetAngles)):
    FL_targetAngles[i] = FL_amplitude * numpy.sin(FL_frequency * FL_targetAngles[i] + FL_phaseOffset)

#plt.plot(targetAngles)
#plt.show()
#numpy.sin(targetAngles / 4.0)
#targetAngles * (numpy.pi/4.0)
# # print("test")
# # print(numpy.sin(targetAngles*numpy.pi/4.0))
numpy.save("data/BL_targetAngles.npy", (numpy.sin(BL_targetAngles)))
numpy.save("data/FL_targetAngles.npy", (numpy.sin(FL_targetAngles)))
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
#make empty array the size of for loop
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Front_Leg")
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robot,

        jointName="Torso_Front_Leg",

        controlMode=p.POSITION_CONTROL,

        targetPosition=FL_targetAngles[i],

        maxForce=250)

    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robot,

        jointName="Torso_Back_Leg",

        controlMode=p.POSITION_CONTROL,

        targetPosition=BL_targetAngles[i],

        maxForce=250)

    #print(backLegSensorValues[i])
    time.sleep(1/240)
numpy.save("data/backLegData.npy", backLegSensorValues)
numpy.save("data/frontLegData.npy", frontLegSensorValues)
p.disconnect()
print(backLegSensorValues)
print()
print(frontLegSensorValues)