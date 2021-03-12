import matplotlib.pyplot as plt
import numpy as np
from pycsou.math.green import CausalGreenIteratedDerivative

x=np.linspace(-1,1,1024)
for k in range(1,5):
   green=CausalGreenIteratedDerivative(k)
   plt.plot(x, green(x))
plt.legend(['k=1', 'k=2', 'k=3', 'k=4'])