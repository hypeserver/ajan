from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

from agent import PersonAgent, Ethnicities

import  random

class WorldModel(Model):
    def __init__(self, N):
        self.grid = MultiGrid(50, 50, True)
        self.schedule = RandomActivation(self)
        self.num_agents = N
        for i in range(self.num_agents):
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
<<<<<<< HEAD
            ethnicity = (((x+1) * (y+1)) / self.grid.width * self.grid.height) * len(Ethnicities)
            a = PersonAgent(unique_id=i,
                            ethnicity=int(ethnicity))
=======
            ethnicity = ((x+1) * (y+1)) / float(self.grid.width * self.grid.height) * len(Ethnicities)
            a = PersonAgent(i, ethnicty=int(ethnicity))
>>>>>>> fd86103c5cb207fcbd098a464fd69981c3c1168e
            self.schedule.add(a)
            # Add the agent to a random grid cell
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()
