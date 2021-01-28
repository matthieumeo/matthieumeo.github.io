import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.diff import Gradient
from pycsou.util.misc import peaks

x  = np.linspace(-2.5, 2.5, 25)
X,Y = np.meshgrid(x,x)
Z = peaks(X, Y)
Dop = Gradient(shape=Z.shape)
y = Dop * Z.flatten()

plt.figure()
h = plt.pcolormesh(X,Y,Z, shading='auto')
plt.colorbar(h)
plt.title('Signal')
plt.figure()
h = plt.pcolormesh(X,Y,y[:Z.size].reshape(X.shape), shading='auto')
plt.colorbar(h)
plt.title('Gradient (1st component)')
plt.figure()
h = plt.pcolormesh(X,Y,y[Z.size:].reshape(X.shape), shading='auto')
plt.colorbar(h)
plt.title('Gradient (2nd component)')
plt.show()