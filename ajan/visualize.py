from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


from model import WorldModel

def agent_portrayal(agent):
    ethnicity_colors = ["black", "blue", "red", "green", "yellow", "purple", "pink", "orange", "brown", "grey", "magenta"]
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 1,
                 "r": 0.5}
    
    if agent.nationalism > 50:
        portrayal["Layer"] = 1
        portrayal["r"] = 1.5

    portrayal['Color'] = ethnicity_colors[agent.ethnicity]


    return portrayal

grid = CanvasGrid(agent_portrayal, 50, 50, 1000, 1000)

server = ModularServer(WorldModel,
                       [grid],
                       "World Model",
                       800, 50, 50)
server.port = 8889
server.launch()
