import healpy as hp
import numpy as np
from pycsphere.linop import FLT
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 4096)
bn = np.ones(21)
flt = FLT(n_max=20, t=t)
b = flt.adjoint(bn)
plt.figure()
plt.stem(np.arange(flt.n_max + 1), bn)
plt.xlabel('$n$')
plt.title('Fourier-Legendre coefficients')
plt.figure()
plt.plot(t, b)
plt.xlabel('$t$')
plt.title('Fourier-Legendre Expansion')