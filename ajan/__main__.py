from model import WorldModel
import matplotlib.pyplot as plt

if __name__ == '__main__':
    nationalities = []
    model = WorldModel(100)
    for i in range(100):
        model.step()

    for agent in model.schedule.agents:
        nationalities.append(int(agent.nationalism))

plt.hist(nationalities, bins=range(max(nationalities)+1))
plt.show()