import pybullet as p
import pybullet_data


class WORLD:
    def __init__(self):
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")
