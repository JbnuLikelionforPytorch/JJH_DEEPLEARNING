import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=np.int)


x = np.array([-5.0, 5.0, 0.1])
y = step_function(x)
plt.plot(x, y)
# y축 지정
plt.ylim(-0.1, 1, 1)
plt.show()
