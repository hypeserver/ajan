import random

BOMB_RADIUS = 2


class AgentBehaviour(object):

    def __init__(self, agent, model):
        self.agent = agent
        self.model = model

    def behavior(self):
        pass

    def run(self):
        self.behavior()


class Racism(AgentBehaviour):

    def calculate_hate(self):
        cellmates = self.model.grid.get_neighbors(self.agent.pos, moore=True, radius=1)

        len_cellmates_hated = sum(1 for cellmate in cellmates if cellmate.ethnicity != self.agent.ethnicity and cellmate.is_living)

        if len_cellmates_hated:
            self.agent.nationalism += len_cellmates_hated
        else:
            self.agent.nationalism = random.randint(1, 20)

    def behavior(self):
        self.calculate_hate()

        if self.agent.nationalism > 5000 and self.agent.education < 10:
            neighbours = self.model.grid.get_neighborhood(
                self.agent.pos,
                moore=True,
                include_center=True,
                radius=BOMB_RADIUS)

            cellmates = self.model.grid.get_cell_list_contents(neighbours)

            for agent in cellmates:
                agent.kill()


class Education(AgentBehaviour):

    def calculate_education(self):
        cellmates = self.model.grid.get_neighbors(self.agent.pos, moore=True, radius=1)
        cellmates_more_educated = [cellmate for cellmate in cellmates if cellmate.education > self.agent.education and cellmate.is_living]

        if len(cellmates_more_educated) > 4:
            if not self.agent.education >= 20:
                self.agent.education += 1
        else:
            if not self.agent.education <= 0:
                self.agent.nationalism -= 1

    def behavior(self):
        self.calculate_education()

