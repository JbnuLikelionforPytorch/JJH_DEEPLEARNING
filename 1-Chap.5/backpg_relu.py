class Relu:
    def __init__(self):
        self.mask = None

    def foward(self, x):
        self.mask = (0 >= x)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx

import numpy as np
x = np.array([[1.0, -0.5],[-2.0, 3.0]])
mask = (x <= 0)
print(mask)