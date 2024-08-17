import numpy as np

from step08 import Square, Exp, Variable

def square(x):
    f = Square()
    return f(x)

def exp(x):
    f = Exp()
    return f(x)

if __name__ == "__main__":
    # x = Variable(np.array(0.5))
    # y = square(exp(square(x)))
    # y.backward()
    # print(x.grad)

    # x = Variable(np.array(1.0))
    # x = Variable(None)
    # x = Variable(1.0)

    x = np.array([1.0])
    y = x ** 2
    print(type(x), x.ndim)
    print(type(y))

    x = np.array(1.0)
    y = x ** 2
    print(type(x), x.ndim)
    print(type(y))
