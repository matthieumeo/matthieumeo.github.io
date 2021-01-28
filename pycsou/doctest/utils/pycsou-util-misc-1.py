import numpy as np
import matplotlib.pyplot as plt
from pycsou.util.misc import peaks

x = np.linspace(-3,3, 1000)
X,Y = np.meshgrid(x,x)
Z = peaks(X,Y)
plt.figure()
plt.imshow(Z)