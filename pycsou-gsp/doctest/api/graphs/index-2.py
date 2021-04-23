from pycgsp.graph import healpix_nngraph
from pygsp.plotting import plot_graph
G, _ = healpix_nngraph(nside=2)
plot_graph(G)