import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.diff import Laplacian
from pycsou.util.misc import peaks

x  = np.linspace(-2.5, 2.5, 25)
X,Y = np.meshgrid(x,x)
Z = peaks(X, Y)
Dop = Laplacian(shape=Z.shape)
y = Dop * Z.flatten()

plt.figure()
h = plt.pcolormesh(X,Y,Z, shading='auto')
plt.colorbar(h)
plt.title('Signal')
plt.figure()
h = plt.pcolormesh(X,Y,y.reshape(X.shape), shading='auto')
plt.colorbar(h)
plt.title('Laplacian')
plt.show()