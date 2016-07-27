import random

from mesa import Agent

from behaviors import racism

Ethnicities = [i for i in range(4)]


class PersonAgent(Agent):
    behaviors = [racism]

    def __init__(self, **kwargs):
        self.nationalism = random.randint(1,20)
        self.ethnicity = kwargs.get('ethnicity')
        self.is_living = True
        super().__init__(kwargs.get('unique_id'), kwargs.get('model'))

    def move(self):
        self.model.grid.move_to_empty(self)

    def move_to_nearby_empty(self):
        neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, radius=1)
        nearby_empty_cells = [nearby_cell for nearby_cell in neighborhood if self.model.grid.is_cell_empty(nearby_cell)]

        if nearby_empty_cells:
            self.model.grid.move_agent(self, random.choice(nearby_empty_cells))

    def step(self):
        if self.is_living:
            if self.nationalism > 20:
                self.move_to_nearby_empty()

            for behaviour in self.behaviors:
                behaviour(self, self.model)

    def kill(self):
        self.is_living = False
