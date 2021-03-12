import healpy as hp
import numpy as np
from pycsphere.linop import SHT
import matplotlib.pyplot as plt

n_max = 20
nside = SHT.nmax2nside(n_max)
rng = np.random.default_rng(0)
map_in = 100 * rng.binomial(n=1, p=0.01, size=int(hp.nside2npix(nside=nside)))
map_in = hp.smoothing(map_in, beam_window=np.ones(shape=(3*n_max//4,)))
sht = SHT(n_max=n_max)
anm = sht(map_in)
synth_map = sht.adjoint(anm)
hp.mollview(map=map_in, title='Input Map', cmap='viridis')
sht.plot_anm(anm)
hp.mollview(map=synth_map, title='Synthesised Map', cmap='viridis')