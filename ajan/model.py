from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from agent import PersonAgent, Ethnicities

import  random

class WorldModel(Model):
    def __init__(self, N, width, height):
        self.grid = MultiGrid(height, width, True)

        self.schedule = RandomActivation(self)
        self.num_agents = N
        self.running = True
        
        
        for i in range(self.num_agents):
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            ethnicity = random.choice(Ethnicities)
            a = PersonAgent(unique_id=i,
                            ethnicity=int(ethnicity))
            self.schedule.add(a)
            # Add the agent to a random grid cell
            self.grid.place_agent(a, (x, y))
            
        self.datacollector = DataCollector(
            agent_reporters={
                "Nationalism": lambda a: a.nationalism,
                "X": lambda a: a.pos[0],
                "Y": lambda a: a.pos[1]
            }
        )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
