import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.diff import FirstDirectionalDerivative, DirectionalGradient
from pycsou.util.misc import peaks

x  = np.linspace(-2.5, 2.5, 25)
X,Y = np.meshgrid(x,x)
Z = peaks(X, Y)
directions1 = np.zeros(shape=(2,Z.size))
directions1[0, :Z.size//2] = 1
directions1[1, Z.size//2:] = 1
directions2 = np.zeros(shape=(2,Z.size))
directions2[1, :Z.size//2] = -1
directions2[0, Z.size//2:] = -1
Dop1 = FirstDirectionalDerivative(shape=Z.shape, directions=directions1)
Dop2 = FirstDirectionalDerivative(shape=Z.shape, directions=directions2)
Dop = DirectionalGradient([Dop1, Dop2])
y = Dop * Z.flatten()

plt.figure()
h = plt.pcolormesh(X,Y,Z, shading='auto')
plt.quiver(x, x, directions1[1].reshape(X.shape), directions1[0].reshape(X.shape))
plt.quiver(x, x, directions2[1].reshape(X.shape), directions2[0].reshape(X.shape), color='red')
plt.colorbar(h)
plt.title('Signal and directions of derivatives')
plt.figure()
h = plt.pcolormesh(X,Y,y[:Z.size].reshape(X.shape), shading='auto')
plt.colorbar(h)
plt.title('Directional derivatives in 1st direction')
plt.figure()
h = plt.pcolormesh(X,Y,y[Z.size:].reshape(X.shape), shading='auto')
plt.colorbar(h)
plt.title('Directional derivatives in 2nd direction')
plt.show()