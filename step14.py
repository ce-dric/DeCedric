import numpy as np

from step13 import Variable, add

x = Variable(np.array(3.0))
y = add(x, x)
print('y', y.data)

y.backward()
print('x.grad : ', x.grad)