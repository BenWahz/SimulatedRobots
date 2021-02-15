import pyrosim.pyrosim as pyrosim
#pyrosim.Start_SDF("world.sdf")



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

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_Front_Leg", parent="Torso", child="Front_Leg", type="revolute", position="0.5 0 1")
    pyrosim.Send_Cube(name="Front_Leg", pos=[0.5, 0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_Back_Leg", parent="Torso", child="Back_Leg", type="revolute", position="-0.5 0 1")
    pyrosim.Send_Cube(name="Back_Leg", pos=[-0.5, 0, -0.5], size=[length, width, height])
    pyrosim.End()

Create_World()
Create_Robot()