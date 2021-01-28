import numpy as np
from pycsou.linop.sampling import NNSampling
import matplotlib.pyplot as plt
rng = np.random.default_rng(seed=0)

rng = np.random.default_rng(seed=0)
x = np.arange(24).reshape(4, 6)
grid = np.stack(np.meshgrid(np.arange(6), np.arange(4)), axis=-1)
samples = np.stack((5 * rng.random(size=12), 3 * rng.random(size=12)), axis=-1)
NNSamplingOp = NNSampling(samples=samples, grid=grid)
grid = grid.reshape(-1, 2)
x = x.reshape(-1)
y = (NNSamplingOp * x.flatten())
x_samp = NNSamplingOp.adjoint(y).reshape(x.shape)
plt.scatter(grid[..., 0].reshape(-1), grid[..., 1].reshape(-1), s=64, c=x.reshape(-1), marker='s', vmin=np.min(x),
     vmax=np.max(x))
plt.scatter(samples[:, 0], samples[:, 1], c='r', s=64)
plt.plot(np.stack((grid[NNSamplingOp.nn_indices, 0], samples[:, 0]), axis=0),
  np.stack((grid[NNSamplingOp.nn_indices, 1], samples[:, 1]), axis=0), '--r')
plt.colorbar()
plt.title('Nearest-neighbours Sampling')
plt.figure()
plt.scatter(grid[..., 0].reshape(-1), grid[..., 1].reshape(-1), s=64, c=x_samp.reshape(-1), marker='s',
     vmin=np.min(x),
     vmax=np.max(x))
plt.scatter(samples[:, 0], samples[:, 1], c='r', s=64)
plt.plot(np.stack((grid[NNSamplingOp.nn_indices, 0], samples[:, 0]), axis=0),
  np.stack((grid[NNSamplingOp.nn_indices, 1], samples[:, 1]), axis=0), '--r')
plt.colorbar()
plt.title('Sampling followed by adjoint')