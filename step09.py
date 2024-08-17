import numpy as np

from step08 import Square, Exp, Variable

def square(x):
    f = Square()
    return f(x)

def exp(x):
    f = Exp()
    return f(x)

if __name__ == "__main__":
    x = Variable(np.array(0.5))
    y = square(exp(square(x)))
    
    # backward
    y.grad = np.array(1.0)
    y.backward()
    print(x.grad)
