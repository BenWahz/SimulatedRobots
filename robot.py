from sensor import SENSOR
from motor import MOTOR
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:



    def __init__(self):

        self.motors = {}

        self.robot = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

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
        self.nn.Print()