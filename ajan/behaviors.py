

def calculate_hate(agent, model):
    cellmates = model.grid.get_cell_list_contents([agent.pos])
    cellmates_hated = [cellmate for cellmate in cellmates if cellmate.ethnicity != agent.ethnicity]
    
    if len(cellmates_hated):
        agent.nationalism += len(cellmates_hated)
    else:
        agent.nationalism -= 1



def racism(agent, model):

    calculate_hate(agent, model)

    if agent.nationalism > 40:
        cellmates = model.grid.get_cell_list_contents([agent.pos])
        map(model.schedule.remove, cellmates)
        model.schedule.remove(agent)
        #model.grid._remove_agent(agent.pos,agent)

        for i in cellmates:
            model.grid._remove_agent(i.pos, i)

