import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x=0
y=0
z=0.5
for j in range(6):
    for k in range(6):
        length = 1
        width = 1
        height = 1
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[j, k, i+0.5], size=[length, width, height])
            length = length*0.9
            width = width*0.9
            height = height*0.9
#pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
#pyrosim.Send_Cube(name="Box2", pos=[(x+width),y,z+height], size=[length,width,height])
pyrosim.End()