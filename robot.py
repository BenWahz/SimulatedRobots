from sensor import SENSOR
from motor import MOTOR
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import time

class ROBOT:

    def __init__(self, solutionID):

        self.motors = {}
        self.myID = solutionID
        # while not os.path.exists("body.urdf"):
        #     time.sleep(0.01)
        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        # while not os.path.exists("brain" + str(solutionID) + ".nndf"):
        #     time.sleep(0.01)

        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        #os.system("del brain" + str(solutionID) + ".nndf")



    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, timeStep):
       for i in (self.sensors):
           self.sensors[i].Get_Value(timeStep)


    def Prepare_To_Act(self):
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

        #BL_targetAngles = numpy.linspace(-numpy.pi, numpy.pi, c.Steps_constant)
        # for i in range(len(BL_targetAngles)):
        #     BL_targetAngles[i] = c.BL_amplitude * numpy.sin(c.BL_frequency * BL_targetAngles[i] + c.BL_phaseOffset)
        #
        # FL_targetAngles = numpy.linspace(-numpy.pi, numpy.pi, c.Steps_constant)
        # for i in range(len(FL_targetAngles)):
        #     FL_targetAngles[i] = c.FL_amplitude * numpy.sin(c.FL_frequency * FL_targetAngles[i] + c.FL_phaseOffset)
        #

    def Act(self, timeStep):


        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Values(desiredAngle, self.robot)
                #print(jointName + ": " + neuronName + ",   desiredAngle: " + str(desiredAngle))

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self, solutionID):
        stateOfLinkZero = p.getLinkState(self.robot, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        # print("State tuple: ")
        # print(stateOfLinkZero)
        # print("position tuple: ")
        # print(positionOfLinkZero)
        # print("x coord: ")
        print(xCoordinateOfLinkZero)

        f = open("tmp" + str(solutionID) + ".txt", 'w')
        f.write(str(xCoordinateOfLinkZero))
        #os.rename("tmp" + str(solutionID) + ".txt", "fitness" + str(solutionID) + ".txt")
        f.close()
        os.system("rename tmp" + str(solutionID) + ".txt fitness" + str(solutionID) +".txt")
        #exit()