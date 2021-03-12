import healpy as hp
import numpy as np
from pycsphere.linop import SHT, FLT, ZonalSphericalConvolution
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

n_max = 30
nside = SHT.nmax2nside(n_max)
rng = np.random.default_rng(0)
map_in = 100 * rng.binomial(n=1, p=0.01, size=int(hp.nside2npix(nside=nside)))
n=np.arange(2000)
spectral_window=1/(100+n*(n+1))**2
flt=FLT(n_max=1999, t=np.linspace(-1,1,2048))
zonal_filter=flt.adjoint(spectral_window)
zonal_filter_interp=interp1d(flt.t, zonal_filter, assume_sorted=True)
convOp = ZonalSphericalConvolution(size=map_in.size, spectral_window=spectral_window)
map_smoothed = convOp(map_in)
map_bismoothed = convOp.adjoint(map_smoothed)
hp.mollview(map=map_in, title='Input Map', cmap='viridis')
plt.figure()
theta=np.linspace(-np.pi, np.pi, 1024)
plt.plot(theta, zonal_filter_interp(np.cos(theta)))
plt.title('Angular section of Zonal Filter')
hp.mollview(map=map_smoothed, title='Smoothed Map', cmap='viridis')
hp.mollview(map=map_bismoothed, title='Backprojected Smoothed Map', cmap='viridis')