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
        cellmates_hated = [cellmate for cellmate in cellmates if cellmate.ethnicity != self.agent.ethnicity and cellmate.is_living]

        if len(cellmates_hated):
            self.agent.nationalism += len(cellmates_hated)
        else:
            self.agent.nationalism = random.randint(1,20)


    def behavior(self):
        self.calculate_hate()

        if self.agent.nationalism > 10000:
            neighbours = self.model.grid.get_neighborhood(
                self.agent.pos,
                moore=True,
                include_center=True,
                radius=BOMB_RADIUS)

            cellmates = self.model.grid.get_cell_list_contents(neighbours)

            for agent in cellmates:
                agent.kill()



