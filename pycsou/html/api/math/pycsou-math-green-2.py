import matplotlib.pyplot as plt
import numpy as np
from pycsou.math.green import Wendland

x=np.linspace(-1,1,1024)
for k in range(4):
   wendland=Wendland(k)
   plt.plot(x, wendland(np.abs(x)))
plt.legend(['k=0', 'k=1', 'k=2', 'k=3'])