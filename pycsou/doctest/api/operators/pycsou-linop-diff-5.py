import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.diff import FirstDirectionalDerivative, SecondDirectionalDerivative
from pycsou.util.misc import peaks

x  = np.linspace(-2.5, 2.5, 25)
X,Y = np.meshgrid(x,x)
Z = peaks(X, Y)
directions = np.zeros(shape=(2,Z.size))
directions[0, :Z.size//2] = 1
directions[1, Z.size//2:] = 1
Dop = FirstDirectionalDerivative(shape=Z.shape, directions=directions)
Dop2 = SecondDirectionalDerivative(shape=Z.shape, directions=directions)
y = Dop * Z.flatten()
y2 = Dop2 * Z.flatten()

plt.figure()
h = plt.pcolormesh(X,Y,Z, shading='auto')
plt.quiver(x, x, directions[1].reshape(X.shape), directions[0].reshape(X.shape))
plt.colorbar(h)
plt.title('Signal and directions of derivatives')
plt.figure()
h = plt.pcolormesh(X,Y,y.reshape(X.shape), shading='auto')
plt.quiver(x, x, directions[1].reshape(X.shape), directions[0].reshape(X.shape))
plt.colorbar(h)
plt.title('First Directional derivatives')
plt.figure()
h = plt.pcolormesh(X,Y,y2.reshape(X.shape), shading='auto')
plt.colorbar(h)
plt.title('Second Directional derivatives')
plt.show()