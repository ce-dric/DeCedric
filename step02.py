import numpy as np

from step01 import Variable

class Function:
    def __call__(self, input):
        x = input.data
        y = x ** 2
        output = Variable(y)
        return output

x = Variable(np.array(10))
f = Function()
y = f(x)

print(type(y))
print(y.data)