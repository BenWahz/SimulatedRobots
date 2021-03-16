import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.robot = None
        self.motorValues = None
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.offset
        #self.Prepare_To_Act()


    def Set_Values(self, desiredAngle, bodyIndex):
        pyrosim.Set_Motor_For_Joint(

                bodyIndex=bodyIndex,

                jointName=self.jointName,

                controlMode=p.POSITION_CONTROL,

                targetPosition= desiredAngle,

                maxForce=250)
        #self.motorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Back_Leg")

