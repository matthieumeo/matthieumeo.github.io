import healpy as hp
import numpy as np
from pycsphere.linop import FLT
import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 4096)
b = (np.arccos(t) <= np.pi / 4)
flt = FLT(n_max=40, t=t)
bn = flt(b)
trunc_fl_series = flt.adjoint(bn)
plt.figure()
plt.plot(t, b)
plt.xlabel('$t$')
plt.title('Original Signal')
plt.figure()
plt.stem(np.arange(flt.n_max + 1), bn)
plt.xlabel('$n$')
plt.title('Fourier-Legendre coefficients')
plt.figure()
plt.plot(t, trunc_fl_series)
plt.xlabel('$t$')
plt.title('Truncated Fourier-Legendre Expansion')