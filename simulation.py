import constants as c
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import numpy
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()




        p.setGravity(0, 0, c.Gravity_constant)



    def run(self):

        for i in range(0, c.Steps_constant):

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            time.sleep(1/30)

    def __del__(self):
        p.disconnect()