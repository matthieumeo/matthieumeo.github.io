import healpy as hp
import numpy as np
from pycsphere.linop import SphericalPooling

nside = 16
rng = np.random.default_rng(0)
map_in = rng.binomial(n=1, p=0.2, size=hp.nside2npix(nside=nside))
map_in = hp.smoothing(map_in, sigma=10 * np.pi / 180)
pool = SphericalPooling(nside_in=nside, nside_out=8, pooling_func='sum')
pooled_map = pool(map_in)
backprojected_map = pool.adjoint(pooled_map)
hp.mollview(map=map_in, title='Input Map', cmap='viridis')
hp.mollview(map=pooled_map, title='Pooled Map', cmap='viridis')
hp.mollview(map=backprojected_map, title='Backprojected Map', cmap='viridis')