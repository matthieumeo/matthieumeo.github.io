import healpy as hp
import numpy as np
from pycsphere.mesh import HEALPixPointSet
from pycsphere.linop import DiscreteSphericalLaplacian

nside = 16
rng = np.random.default_rng(0)
map_in = rng.binomial(n=1, p=0.005, size=hp.nside2npix(nside=nside))
map_in = hp.smoothing(map_in, sigma=10 * np.pi / 180)
laplacian = DiscreteSphericalLaplacian(point_set=HEALPixPointSet(nside=nside))
map_d2 = laplacian(map_in)
hp.mollview(map=map_in, title='Input Map', cmap='viridis')
hp.mollview(map=np.abs(map_d2), title='Magnitude of Laplacian Map', cmap='viridis')