from mesa import  Agent

import  random

Ethnicities = [i for i in range(10)]

class RacismAgent(Agent):

    languages = []

    def __init__(self, **kwargs):
        for i, v in kwargs.items():
            setattr(self, i, v)

        self.languages.append(self.ethnicity)
        self.nationalism = random.uniform(1,20)


    def increase_hate(self, model):
        cellmates = model.grid.get_cell_list_contents([self.pos])
        cellmates_hated = [cellmate for cellmate in cellmates if cellmate.ethnicity != self.ethnicity]
        self.nationalism += len(cellmates_hated)
        print(self.nationalism)


    def step(self, model):
        if self.nationalism > 50:
            print("hello nationalism")
        else:
            # print("fuck you")
            self.increase_hate(model)
