import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.conv import Convolve2D
from scipy import signal
sig = np.zeros(shape=(100,100))
sig[sig.shape[0] // 2 - 2:sig.shape[0] // 2 + 3, sig.shape[1] // 2 - 2:sig.shape[1] // 2 + 3] = 1
filter = signal.hann(50)
filter = filter[None,:] * filter[:,None]
ConvOp = Convolve2D(size=sig.size, filter=filter, shape=sig.shape)
filtered = (ConvOp * sig.ravel()).reshape(sig.shape)
correlated = (ConvOp.H * sig.ravel()).reshape(sig.shape)
plt.figure()
plt.subplot(1,3,1)
plt.imshow(sig, cmap='plasma'); plt.title('Signal')
plt.subplot(1,3,2)
plt.imshow(filtered, cmap='plasma'); plt.title('Filtered Signal')
plt.subplot(1,3,3)
plt.imshow(correlated, cmap='plasma'); plt.title('Correlated Signal')
plt.show()