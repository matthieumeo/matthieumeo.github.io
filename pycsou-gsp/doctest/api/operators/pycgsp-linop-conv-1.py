import numpy as np
from pygsp.graphs import Ring
from pycgsp.linop.conv import GraphConvolution
np.random.seed(0)
G = Ring(N=32, k=2)
G.compute_laplacian(lap_type='normalized')
G.set_coordinates(kind='spring')
signal = np.random.binomial(n=1,p=0.2,size=G.N)
coefficients = np.ones(3)
ConvOp = GraphConvolution(Graph=G, coefficients=coefficients)
e1 = np.zeros(shape=G.N)
e1[0] = 1
filter = ConvOp * e1
filtered = ConvOp * signal
plt.figure()
ax=plt.gca()
G.plot_signal(signal, ax=ax, backend='matplotlib')
plt.title('Signal')
plt.axis('equal')
plt.figure()
ax=plt.gca()
G.plot_signal(filter, ax=ax, backend='matplotlib')
plt.title('Filter')
plt.axis('equal')
plt.figure()
ax=plt.gca()
G.plot_signal(filtered, ax=ax, backend='matplotlib')
plt.title('Filtered Signal')
plt.axis('equal')