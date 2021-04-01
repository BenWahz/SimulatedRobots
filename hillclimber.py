from solution import SOLUTION
import constants as c
import copy


class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        # print("PARENT AND CHILD: ")
        # print(self.parent.weights)
        # print(self.child.weights)
        # exit()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
        # print("FITNESS SCORES")
        # print(self.parent.fitness)
        # print(self.child.fitness)
        # exit()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Evolve(self):
        self.parent.Evaluate("GUI")

        for currentGeneration in range(c.currentGenerations):
            self.Evolve_For_One_Generation()

    def Show_Best(self):
        self.parent.Evaluate("GUI")


    def Print(self):
        print(str(self.parent.fitness) + ", " + str(self.child.fitness))