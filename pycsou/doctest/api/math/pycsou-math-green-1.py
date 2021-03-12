import matplotlib.pyplot as plt
import numpy as np
from pycsou.math.green import Matern

x=np.linspace(-3,3,1024)
for k in range(4):
   matern=Matern(k)
   plt.plot(x, matern(np.abs(x)))
plt.legend(['k=0', 'k=1', 'k=2', 'k=3'])