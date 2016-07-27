import random

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

from agent import PersonAgent, Ethnicities


class WorldModel(Model):
    def __init__(self, N, width, height):
        self.grid = SingleGrid(height, width, True)

        self.schedule = RandomActivation(self)
        self.num_agents = N
        self.running = True
        
        for i in range(self.num_agents):
            ethnicity = random.choice(Ethnicities)
            a = PersonAgent(unique_id=i,
                            model=self,
                            ethnicity=int(ethnicity)
                            )
            self.schedule.add(a)
            # Add the agent to a random grid cell

            self.grid.position_agent(a)
            
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
