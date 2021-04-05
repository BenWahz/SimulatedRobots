import constants as c
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import time
import numpy
import pyrosim.pyrosim as pyrosim


class SIMULATION:
    def __init__(self, sim_style, solutionID):
        self.directOrGUI = sim_style
        if sim_style == "DIRECT":
            p.connect(p.DIRECT)
        elif sim_style == "GUI":
            self.physicsClient = p.connect(p.GUI)


        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()

        p.setGravity(0, 0, c.Gravity_constant)

        self.robot = ROBOT(solutionID)


    def run(self):

        for i in range(0, c.Steps_constant):

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
            if self.directOrGUI == "GUI":
                time.sleep(1/3000)

    def __del__(self):
        p.disconnect()

    def Get_Fitness(self, solutionID):
        self.robot.Get_Fitness(solutionID)

