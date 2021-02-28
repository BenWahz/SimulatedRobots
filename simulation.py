import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
body = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate("body.urdf")
#make empty array the size of for loop
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Front_Leg")
    #print(backLegSensorValues[i])
    time.sleep(1/60)
numpy.save("data/backLegData.npy", backLegSensorValues)
numpy.save("data/frontLegData.npy", frontLegSensorValues)
p.disconnect()
print(backLegSensorValues)
print()
print(frontLegSensorValues)