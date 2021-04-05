from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")

        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Spawn(self):
        self.children = {}
        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        for i in range(len(self.children)):
            self.children[i].Mutate()
        # print("PARENT AND CHILD: ")
        # print(self.parent.weights)
        # print(self.child.weights)
        # exit()

    def Select(self):
        for i in range(len(self.parents)):
            if self.parents[i].fitness < self.children[i].fitness:
                self.parents[i] = self.children[i]
        # print("FITNESS SCORES")
        # print(self.parent.fitness)
        # print(self.child.fitness)
        # exit()

    def Evolve_For_One_Generation(self):
        # pass
        self.Spawn()
        self.Mutate()
        print("EVALUATING CHILDREN")
        self.Evaluate(self.children)
        # exit()
        self.Print()
        self.Select()

    def Evolve(self):
        print(self.parents)
        self.Evaluate(self.parents)
        print("Should exit now")
        # exit()
        for currentGeneration in range(c.currentGenerations):
            self.Evolve_For_One_Generation()

    def Evaluate(self, solutions):
        print("FLAG FLAG")
        print(solutions)
        for i in range(len(solutions)):
            solutions[i].Start_Simulation("DIRECT")   #CHANGING THIS TO GUI WILL BREAK PARALLELISM, NOT SURE WHY

        for j in range(len(solutions)):
            solutions[j].Wait_For_Simulation_To_End()

    def Show_Best(self):
        minFitness = 1000
        minIndex = -1
        for i in range(len(self.parents)):
            if self.parents[i].fitness < minFitness:
                minIndex = i
                minFitness = self.parents[i].fitness
        print("RUNNING BEST PARENT SIMULATION    INDEX: " + str(minIndex))
        self.parents[minIndex].Start_Simulation("GUI")

    def Print(self):
        print("\n")
        for key in range(len(self.parents)):
            print(str(self.parents[key].fitness) + ", " + str(self.children[key].fitness))
            print("\n")