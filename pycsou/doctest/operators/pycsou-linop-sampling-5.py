import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.sampling import MappedDistanceMatrix

rng = np.random.default_rng(seed=2)
phi = np.linspace(0,2*np.pi, 256)
theta = np.linspace(-np.pi/2,np.pi/2, 256)
phi, theta = np.meshgrid(phi, theta)
x,y,z = np.cos(phi)*np.cos(theta), np.sin(phi)*np.cos(theta), np.sin(theta)
samples1 = np.stack((x.flatten(), y.flatten(), z.flatten()), axis=-1)
phi2 = 2 * np.pi * rng.random(size=4)
theta2 = np.pi * rng.random(size=4) - np.pi/2
x2,y2,z2 = np.cos(phi2)*np.cos(theta2), np.sin(phi2)*np.cos(theta2), np.sin(theta2)
samples2 = np.stack((x2,y2,z2), axis=-1)
alpha = np.ones(samples2.shape[0])
sigma = 1 / 9
func = lambda x: np.exp(-np.abs(1-x) / (sigma ** 2))
MDMOp = MappedDistanceMatrix(samples1=samples1, samples2=samples2, function=func,mode='zonal', operator_type='sparse', max_distance=3*sigma)
plt.contourf(phi, theta, (MDMOp * alpha).reshape(phi.shape), 50)
plt.title('Sum of 4 (zonal) wrapped Gaussians')
plt.colorbar()
plt.xlabel('$\\phi$ (radians)')
plt.ylabel('$\\theta$ (radians)')