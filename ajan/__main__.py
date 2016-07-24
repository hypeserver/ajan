from model import WorldModel
import matplotlib.pyplot as plt

if __name__ == '__main__':
    nationalities = []
    model = WorldModel(100)
    for i in range(100):
        model.step()