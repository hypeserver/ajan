from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from model import WorldModel


def agent_portrayal(agent):
    ethnicity_colors = ["red", "green", "yellow", "purple", "pink", "orange", "brown", "grey", "magenta"]
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 1,
                 "r": 0.9,
                 "text": str(agent.nationalism),
                 "text_color": "black",
                 "Colors": agent.rsorted_known_origin_names,
                 #"Colors": ["red", "green", "blue"],
                 }
    
    if agent.nationalism > 3000:
        portrayal["Layer"] = 0
        portrayal["r"] = 1.5

    if not agent.is_living:
        portrayal["text"] = "X"
        portrayal["text_color"] = "black"
        portrayal["Layer"] = 2
        portrayal["Colors"] = ["black"]

    return portrayal

grid = CanvasGrid(agent_portrayal, 25, 25, 800, 800)

server = ModularServer(WorldModel,
                       [grid],
                       "Canli Bomba",
                       250, 25, 25)
server.port = 8889
server.launch()
