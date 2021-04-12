import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time

class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1

    # def Evaluate(self, DirectOrGUI):
    #     pass
        # self.Create_World()
        # self.Generate_Body()
        # self.Generate_Brain()
        # os.system("start /B python simulate.py " + DirectOrGUI + " " + str(self.myID))
        #
        # while not os.path.exists("fitness" + str(self.myID) + ".txt"):
        #     time.sleep(0.01)
        #
        # f = open("fitness" + str(self.myID) + ".txt", 'r')
        # self.fitness = float(f.readline())
        # print(self.fitness)

    def Start_Simulation(self, DirectOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()



        # while not os.path.exists("brain" + str(self.myID) + ".nndf"):
        #     time.sleep(0.01)
        # print("FLAG 2 calling start command (solution.py) ID = " + str(self.myID))
        # exit()
        os.system("start /B py simulate.py " + DirectOrGUI + " " + str(self.myID))
        # exit()
        # print("FLAG 3 (solution.py)")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)

        f = open("fitness" + str(self.myID) + ".txt", 'r')
        self.fitness = float(f.readline())
        print("~~~~~~~FITNESS VALUE " + str(self.myID))
        print(self.fitness)
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")
    # def Show_Best(self):

    def Set_ID(self, ID):
        self.myID = ID

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomCol = random.randint(0,1)
        self.weights[randomRow, randomCol] = random.random() * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1
        width = 1
        height = 1
        x = 2
        y = 2
        z = 0.5
        # exit()
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        pyrosim.End()
        # exit()
        while not os.path.exists("world.sdf"):
            time.sleep(0.01)

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="Front_Leg", type="revolute",
                           position="0.5 0 1")
        pyrosim.Send_Cube(name="Front_Leg", pos=[0.5, 0, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="Back_Leg", type="revolute", position="-0.5 0 1")
        pyrosim.Send_Cube(name="Back_Leg", pos=[-0.5, 0, -0.5], size=[length, width, height])
        pyrosim.End()
        while not os.path.exists("body.urdf"):
            time.sleep(0.01)

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Front_Leg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Back_Leg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=-0.25)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=3, weight=-0.75)
        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=-1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=4, weight=-0.75)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=-0.25)
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()
        while not os.path.exists("brain" + str(self.myID) + ".nndf"):
            time.sleep(0.01)
