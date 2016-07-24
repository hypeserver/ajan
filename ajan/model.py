from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

from agent import PersonAgent, Ethnicities

import  random

class WorldModel(Model):
    def __init__(self, N):
        self.grid = MultiGrid(100, 100, True)
        self.schedule = RandomActivation(self)
        self.num_agents = N
        for i in range(self.num_agents):
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            ethnicity = random.choice(Ethnicities)
            a = PersonAgent(unique_id=i,
                            ethnicity=int(ethnicity))
            self.schedule.add(a)
            # Add the agent to a random grid cell
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()
