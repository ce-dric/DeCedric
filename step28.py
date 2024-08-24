
import numpy as np
from decedric import Variable
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm

def rosenbrock(x0, x1):
    y = 100 * (x1 - x0**2) **2 + (1-x0)**2
    return y

x0 = np.linspace(-2.0, 2.0, num=500)
x1 = np.linspace(-1.0, 3.0, num=500)

X0, X1 = np.meshgrid(x0, x1)
Y = rosenbrock(X0, X1)

# log10(y)の最小値を取得
y_log10_min = np.floor(np.log10(Y.min()) - 1)

# log10(y)の最大値を取得
y_log10_max = np.ceil(np.log10(Y.max()) + 1)

lev_log10 = np.linspace(y_log10_min, y_log10_max, num=45)[25:35]
levs = np.power(10, lev_log10)

x0 = Variable(np.array(0.0))
x1 = Variable(np.array(2.0))

lr = 0.001
iters = 1000

# 更新値の記録用のリストを初期化
x0_list = [x0.data.item()]
x1_list = [x1.data.item()]

for i in range(iters):
    y = rosenbrock(x0, x1)

    x0.cleargrad()
    x1.cleargrad()
    y.backward()

    x0.data -= lr * x0.grad
    x1.data -= lr * x1.grad

    x0_list.append(x0.data.item())
    x1_list.append(x1.data.item())

# トレースプロットを作成
plt.figure("rosenbrock function trace plot")
plt.contour(X0, X1, Y, norm=LogNorm(), levels=levs, zorder=0)
plt.scatter(1.0, 1.0, marker='*', s=500, c='blue')
plt.plot(x0_list, x1_list, c='orange', marker='o', mfc='red', mec='red')
plt.xlabel("x0")
plt.ylabel("x1")
plt.show()