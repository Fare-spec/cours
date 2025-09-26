import maze_creator as mc


lab = mc.Labyrinth(10, 10)
lab.set_start_end((0, 0), (100, 100))
lab.generate_maze()
print(lab.__str__())
