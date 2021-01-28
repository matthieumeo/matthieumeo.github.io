import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.sampling import MappedDistanceMatrix

t = np.linspace(0, 2, 256)
rng = np.random.default_rng(seed=2)
x,y = np.meshgrid(t,t)
samples1 = np.stack((x.flatten(), y.flatten()), axis=-1)
samples2 = np.stack((2 * rng.random(size=4), 2 * rng.random(size=4)), axis=-1)
alpha = np.ones(samples2.shape[0])
sigma = 1 / 12
func = lambda x: np.exp(-x ** 2 / (2 * sigma ** 2))
MDMOp = MappedDistanceMatrix(samples1=samples1, samples2=samples2, function=func, operator_type='dask')
plt.contourf(x,y,(MDMOp * alpha).reshape(t.size, t.size), 50)
plt.title('Sum of 4 (radial) Gaussians')
plt.colorbar()
plt.xlabel('$x$')
plt.ylabel('$y$')