

def increase_hate(agent, model):
    cellmates = model.grid.get_cell_list_contents([agent.pos])
    for i in cellmates:
        print(i.ethnicity, agent.ethnicity)
    cellmates_hated = [cellmate for cellmate in cellmates if cellmate.ethnicity != agent.ethnicity]
    agent.nationalism += len(cellmates_hated)


def racism(agent, model):
    if agent.nationalism > 20:
        print("hello racism")
    else:
        increase_hate(agent, model)


