import numpy as np
from pycsphere.green import TruncatedFourierLegendreSeries

n_max=20
n=np.arange(0, n_max + 1).astype(np.float)
fn=0*n; fn[n>0]=(n[n>0]*(n[n>0]+1))**(-1)
fN=TruncatedFourierLegendreSeries(fn)
theta=np.linspace(-np.pi, np.pi, 1024)
plt.plot(theta, fN(np.cos(theta)))
plt.ylabel('$f_N(\\cos\\theta)$')
plt.xlabel('$\\theta\\in[-\\pi,\\pi]$')