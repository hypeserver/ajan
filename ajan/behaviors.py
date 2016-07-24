

def calculate_hate(agent, model):
    cellmates = model.grid.get_cell_list_contents([agent.pos])
    cellmates_hated = [cellmate for cellmate in cellmates if cellmate.ethnicity != agent.ethnicity]
    
    if len(cellmates_hated):
        agent.nationalism += len(cellmates_hated)
    else:
        agent.nationalism -= 1



def racism(agent, model):
    calculate_hate(agent, model)


