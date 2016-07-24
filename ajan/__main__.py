from model import WorldModel
import matplotlib.pyplot as plt

import numpy as np

if __name__ == '__main__':
    model = WorldModel(100)
    for i in range(100):
        model.step()

    agent_counts = np.zeros((model.grid.width, model.grid.height))
    for agent in model.schedule.agents:
        x, y = agent.pos
        agent_counts[x][y] = int(agent.nationalism)

    plt.imshow(agent_counts, interpolation='nearest')
    plt.colorbar()
    plt.show()
