
from mesa import  Agent
import  random
from behaviors import racism

Ethnicities = [i for i in range(10)]
class PersonAgent(Agent):

    behaviors = [racism]

    def __init__(self, **kwargs):
        self.nationalism = random.randint(1,20)
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
        if self.nationalism > 50:
            self.move(model)

        for behaviour in self.behaviors:
            behaviour(self, model)

