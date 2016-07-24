from RacismBehavior.agent import RacismAgent

from mesa import  Agent

import  random

Ethnicities = [i for i in range(10)]

class PersonAgent(Agent):

    behaviors = [RacismAgent]

    def __init__(self, **kwargs):

        self.ethnicity = kwargs.get('ethnicity')
        self.unique_id = kwargs.get('unique_id')

    def move(self, model):
        possible_steps = model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = random.choice(possible_steps)
        model.grid.move_agent(self, new_position)


    def step(self, model):
        self.move(model)
        for behavior in self.behaviors:
            _behavior = behavior(**self.__dict__)
            _behavior.step(model)
