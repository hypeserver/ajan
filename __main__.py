from model import WorldModel

if __name__ == '__main__':
    model = WorldModel(10000)
    for i in range(100):
        model.step()
