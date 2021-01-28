import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.diff import Integration1D

x = np.array([0,0,0,1,0,0,0,0,0,2,0,0,0,0,-1,0,0,0,0,2,0,0,0,0])
Int = Integration1D(size=x.size)
y = Int * x
plt.figure()
plt.plot(np.arange(x.size), x)
plt.plot(np.arange(x.size), y)
plt.legend(['Signal', 'Integral'])
plt.title('Integration')
plt.show()