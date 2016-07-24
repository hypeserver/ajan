from mesa import  Agent

import  random

Ethnicities = [i for i in range(10)]

class PersonAgent(Agent):

    behaviours = []

    languages = []

    def __init__(self, unique_id, ethnicty=random.choice(Ethnicities)):
        self.unique_id = unique_id
        self.ethnicity = ethnicty
        self.languages.append(self.ethnicity)
        self.nationalism = random.uniform(1,20)


    def move(self, model):
        possible_steps = model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = random.choice(possible_steps)
        model.grid.move_agent(self, new_position)


    def increase_hate(self, model):
        cellmates = model.grid.get_cell_list_contents([self.pos])
        cellmates_hated = [cellmate for cellmate in cellmates if cellmate.ethnicity != self.ethnicity]
        self.nationalism += len(cellmates_hated)
        # other = random.choice(cellmates)
        # other.wealth += 1
        # self.wealth -= 1


    def step(self, model):
        self.move(model)
        if self.nationalism > 50:
            print("hello nationalism")
        else:
            self.increase_hate(model)
