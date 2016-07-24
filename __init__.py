from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

import random

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
        print(len(cellmates), len(cellmates_hated))
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


class WorldModel(Model):
    def __init__(self, N):
        self.grid = MultiGrid(50, 50, True)
        self.schedule = RandomActivation(self)
        self.num_agents = N
        for i in range(self.num_agents):
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            ethnicity = (((x+1) * (y+1)) / self.grid.width * self.grid.height) * len(Ethnicities)
            a = PersonAgent(i, ethnicty=int(ethnicity))
            self.schedule.add(a)
            # Add the agent to a random grid cell
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()


model = WorldModel(10000)
for i in range(100):
    model.step()