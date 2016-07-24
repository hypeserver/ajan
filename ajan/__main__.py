from model import WorldModel
import matplotlib.pyplot as plt

import numpy as np

if __name__ == '__main__':
    model = WorldModel(10000)
    for i in range(100):
        model.step()
