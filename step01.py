class Variable:
    def __init__(self, data) -> None:
        self.data = data


if __name__ == "__main__":
    import numpy as np

    data = np.array(2.0)
    x = Variable(data)
    print(x.data)