from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from model import WorldModel


def agent_portrayal(agent):
    ethnicity_colors = ["red", "green", "yellow", "purple", "pink", "orange", "brown", "grey", "magenta"]
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 1,
                 "r": 0.5,
                 "Color": ethnicity_colors[agent.ethnicity]
                 }
    
    if agent.nationalism > 25:
        portrayal["Layer"] = 0
        portrayal["r"] = 1.5

    if not agent.is_living:
        portrayal["text"] = "X"
        portrayal["text_color"] = "black"
        portrayal["Layer"] = 2
        portrayal["Color"] = "black"

    return portrayal

grid = CanvasGrid(agent_portrayal, 50, 50, 1000, 1000)

server = ModularServer(WorldModel,
                       [grid],
                       "Canli Bomba",
                       400, 50, 50)
server.port = 8889
server.launch()
