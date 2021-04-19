import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
    def __init__(self, myID):
        self.myID = myID
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons)
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
        #Select a random row and col from a array that is numSensors x numMotors in size
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomCol = random.randint(0,c.numMotorNeurons-1)
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

    def Generate_Body(self): #Create Dog Body
        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1

        #torso
        pyrosim.Send_Cube(name="Torso", pos=[1, 0, 1], size=[length*3, width, height])
        # pyrosim.Send_Cube(name="Front_Torso", pos=[1, 0, 1], size=[length, width, height])
        # pyrosim.Send_Cube(name="Back_Torso", pos=[-0.5, 0, 0], size=[length, width, height])
        # pyrosim.Send_Joint(name="Torso_Joint", parent="Front_Torso", child= "Back_Torso", type= "revolute", position= "0.5 0 1", jointAxis= "0 1 0")




        #front right leg
        pyrosim.Send_Joint(name="Torso_To_Front_Right", parent="Torso", child="Front_Right_Leg", type="revolute",
                           position="0.125 0.5 1", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Front_Right_Leg", pos=[0, 0.125, -0.5], size=[0.25, 0.25, 1])

        pyrosim.Send_Joint(name="Front_Right_To_Lower", parent="Front_Right_Leg", child="Front_Right_Leg_Lower", type="revolute",
                           position="0 0.125 -1", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Front_Right_Leg_Lower", pos=[-0.5, 0, 0], size=[1, 0.25, .25])
        #
        # # front left leg
        pyrosim.Send_Joint(name="Torso_To_Front_Left", parent="Torso", child="Front_Left_Leg", type="revolute",
                           position="0.125 -0.5 1", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Front_Left_Leg", pos=[0, -0.125, -0.5], size=[0.25, 0.25, 1])

        pyrosim.Send_Joint(name="Front_Left_To_Lower", parent="Front_Left_Leg", child="Front_Left_Leg_Lower", type="revolute",
                           position="0 -0.125 -1", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Front_Left_Leg_Lower", pos=[-0.5, 0, 0], size=[1, 0.25, 0.25])

        # back right leg
        pyrosim.Send_Joint(name="Torso_To_Back_Right", parent="Torso", child="Back_Right_Leg", type="revolute",
                           position="2.25 0.5 1", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Back_Right_Leg", pos=[0, 0.125, -0.5], size=[0.25, 0.25, 1])

        pyrosim.Send_Joint(name="Back_Right_To_Lower", parent="Back_Right_Leg", child="Back_Right_Leg_Lower",
                           type="revolute",
                           position="0 0.125 -1", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Back_Right_Leg_Lower", pos=[-0.5, 0, 0], size=[1, 0.25, .25])
        #
        # # back left leg
        pyrosim.Send_Joint(name="Torso_To_Back_Left", parent="Torso", child="Back_Left_Leg", type="revolute",
                           position="2.25 -0.5 1", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Back_Left_Leg", pos=[0, -0.125, -0.5], size=[0.25, 0.25, 1])

        pyrosim.Send_Joint(name="Back_Left_To_Lower", parent="Back_Left_Leg", child="Back_Left_Leg_Lower",
                           type="revolute",
                           position="0 -0.125 -1", jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Back_Left_Leg_Lower", pos=[-0.5, 0, 0], size=[1, 0.25, 0.25])



        #back upper leg
        # pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="Back_Leg", type="revolute", position="0 -0.5 1", jointAxis= "1 0 0")
        # pyrosim.Send_Cube(name="Back_Leg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
        # # back lower leg
        # pyrosim.Send_Joint(name="BackLeg_Lower", parent="Back_Leg", child="Back_Leg_Lower", type="revolute",
        #                    position="0 -1 0", jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="Back_Leg_Lower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        #
        #
        # #right upper leg
        # pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="Right_Leg", type="revolute", position="-0.5 0 1",
        #                    jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="Right_Leg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        # # right lower leg
        # pyrosim.Send_Joint(name="RightLeg_Lower", parent="Right_Leg", child="Right_Leg_Lower", type="revolute",
        #                    position="-1 0 0", jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="Right_Leg_Lower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        #
        #
        # #left upper leg
        # pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="Left_Leg", type="revolute",
        #                    position="0.5 0 1", jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="Left_Leg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        # pyrosim.Send_Joint(name="LeftLeg_Lower", parent="Left_Leg", child="Left_Leg_Lower", type="revolute",
        #                    position="1 0 0", jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="Left_Leg_Lower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])




        pyrosim.End()


        while not os.path.exists("body.urdf"):
            time.sleep(0.01)
        # exit()

    def Generate_Brain(self):
        #send sensor neurons
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        #commented out sensors to try only having sensors on lower legs

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Front_Right_Leg_Lower")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="Front_Left_Leg_Lower")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Back_Right_Leg_Lower")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="Back_Left_Leg_Lower")

        # pyrosim.Send_Motor_Neuron(name=2, jointName="Torso_Joint")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_To_Front_Right")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Front_Right_To_Lower")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_To_Front_Left")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Front_Left_To_Lower")

        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_To_Back_Right")
        pyrosim.Send_Motor_Neuron(name=9, jointName="Back_Right_To_Lower")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_To_Back_Left")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Back_Left_To_Lower")
        #

        # # pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        # # pyrosim.Send_Sensor_Neuron(name=1, linkName="Front_Leg")
        # pyrosim.Send_Sensor_Neuron(name=0, linkName="Front_Leg_Lower")
        # # pyrosim.Send_Sensor_Neuron(name=3, linkName="Back_Leg")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName="Back_Leg_Lower")
        # # pyrosim.Send_Sensor_Neuron(name=5, linkName="Right_Leg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName="Right_Leg_Lower")
        # # pyrosim.Send_Sensor_Neuron(name=7, linkName="Left_Leg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName="Left_Leg_Lower")
        #
        # #send motor neurons
        # pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Joint")
        #
        # # pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron(name=5, jointName="BackLeg_Lower")
        #
        # pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron(name=7, jointName="FrontLeg_Lower")
        #
        # pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron(name=9, jointName="RightLeg_Lower")
        #
        # pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron(name=12, jointName="LeftLeg_Lower")
        #



        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])
        pyrosim.End()
        while not os.path.exists("brain" + str(self.myID) + ".nndf"):
            time.sleep(0.01)
        # exit()
