import matplotlib.pyplot as plt
import numpy as np
from pycsou.math.green import SubGaussian

x=np.linspace(-3,3,1024)
lg=[]
for alpha in np.linspace(0,2,6)[1:-1]:
   subgaussian=SubGaussian(alpha)
   plt.plot(x, subgaussian(np.abs(x)))
   lg.append(f'$\\alpha={np.round(alpha,1)}$')
plt.legend(lg)