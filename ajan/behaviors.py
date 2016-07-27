import random

BOMB_RADIUS = 2

def calculate_hate(agent, model):
    cellmates = model.grid.get_neighbors(agent.pos, moore=True, radius=1)
    cellmates_hated = [cellmate for cellmate in cellmates if cellmate.ethnicity != agent.ethnicity and cellmate.is_living]
    
    if len(cellmates_hated):
        agent.nationalism += len(cellmates_hated)
    else:
        agent.nationalism = random.randint(1,20)


def racism(agent, model):
    calculate_hate(agent, model)

    if agent.nationalism > 10000:
        neighbours = model.grid.get_neighborhood(
            agent.pos,
            moore=True,
            include_center=True,
            radius=BOMB_RADIUS)

        cellmates = model.grid.get_cell_list_contents(neighbours)

        for agent in cellmates:
            agent.kill()
