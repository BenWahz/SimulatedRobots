import os
from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import hillclimber
# for i in range(5):
# #     os.system("python generate.py")
# #     os.system("python simulate.py")


phc = PARALLEL_HILL_CLIMBER()
# print("Flag 1")
phc.Evolve()
phc.Show_Best()