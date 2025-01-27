import maze_creator as mc
import random


random.seed(random.randint(-2147483647, 2147483647))
lab = mc.Labyrinth(100,100)
lab.set_start_end((0,0),(100,100))
