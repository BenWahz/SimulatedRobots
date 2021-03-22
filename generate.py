import pyrosim.pyrosim as pyrosim
#pyrosim.Start_SDF("world.sdf")
import random


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    length = 1
    width = 1
    height = 1
    x = 2
    y = 2
    z = 0.5
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="Front_Leg", type="revolute", position="0.5 0 1")
    pyrosim.Send_Cube(name="Front_Leg", pos=[0.5, 0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="Back_Leg", type="revolute", position="-0.5 0 1")
    pyrosim.Send_Cube(name="Back_Leg", pos=[-0.5, 0, -0.5], size=[length, width, height])
    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
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
    for i in range(3):
        for j in range(3,5):
            pyrosim.Send_Synapse(sourceNeuronName= i, targetNeuronName= j, weight= random.uniform(-1.0,1.0))
    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()

# < synapse
# sourceNeuronName = "0"
# targetNeuronName = "3"
# weight = "0.8449776935080169" / >
# < synapse
# sourceNeuronName = "0"
# targetNeuronName = "4"
# weight = "0.11088676104484896" / >
# < synapse
# sourceNeuronName = "1"
# targetNeuronName = "3"
# weight = "0.16678167595099103" / >
# < synapse
# sourceNeuronName = "1"
# targetNeuronName = "4"
# weight = "-0.5993838704797643" / >
# < synapse
# sourceNeuronName = "2"
# targetNeuronName = "3"
# weight = "-0.5645928821073778" / >
# < synapse
# sourceNeuronName = "2"
# targetNeuronName = "4"
# weight = "0.2332464281693174" / >