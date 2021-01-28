import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.conv import MovingAverage2D
from scipy import signal
sig = np.zeros(shape=(100,100))
sig[sig.shape[0] // 2 - 2:sig.shape[0] // 2 + 3, sig.shape[1] // 2 - 2:sig.shape[1] // 2 + 3] = 1
MAOp = MovingAverage2D(window_shape=(50,25), shape=sig.shape)
moving_average = (MAOp * sig.ravel()).reshape(sig.shape)
plt.figure()
plt.subplot(1,2,1)
plt.imshow(sig, cmap='plasma'); plt.title('Signal')
plt.subplot(1,2,2)
plt.imshow(moving_average, cmap='plasma'); plt.title('Moving Average')
plt.show()