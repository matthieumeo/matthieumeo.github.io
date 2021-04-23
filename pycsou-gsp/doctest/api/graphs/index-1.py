import numpy as np
from pycgsp.graph import cvxhull_graph
from pygsp.plotting import plot_graph
theta, phi = np.linspace(0,np.pi,6, endpoint=False)[1:], np.linspace(0,2*np.pi,9, endpoint=False)
theta, phi = np.meshgrid(theta, phi)
x,y,z = np.cos(phi)*np.sin(theta), np.sin(phi)*np.sin(theta), np.cos(theta)
R = np.stack((x.flatten(), y.flatten(), z.flatten()), axis=-1)
G, _ = cvxhull_graph(R)
plot_graph(G)