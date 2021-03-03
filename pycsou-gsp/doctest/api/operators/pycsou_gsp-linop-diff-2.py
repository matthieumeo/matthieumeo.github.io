import numpy as np
from pygsp.graphs import Ring
from pycsou_gsp.linop.diff import GeneralisedGraphLaplacian
np.random.seed(1)
G = Ring(N=32, k=4)
G.compute_laplacian(lap_type='normalized')
G.set_coordinates(kind='spring')
x = np.arange(G.N)
signal = np.piecewise(x, [x < G.N//3, (x >= G.N//3) * (x< 2 * G.N//3), x>=2 * G.N//3], [lambda x: -x, lambda x: 3 * x - 4 * G.N//3, lambda x: -0.5 * x + G.N])
Dop = GeneralisedGraphLaplacian(Graph=G, kind='polynomial', coeffs=[1,-1,2])
gen_lap = Dop * signal
plt.figure()
ax=plt.gca()
G.plot_signal(signal, ax=ax, backend='matplotlib')
plt.title('Signal')
plt.axis('equal')
plt.figure()
ax=plt.gca()
G.plot_signal(gen_lap, ax=ax, backend='matplotlib')
plt.title('Generalized Laplacian of signal')
plt.axis('equal')