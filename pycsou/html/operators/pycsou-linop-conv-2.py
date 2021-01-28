import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.conv import Convolve1D
from scipy import signal
sig = np.zeros(shape=(100,100))
sig[sig.shape[0] // 2 - 2:sig.shape[0] // 2 + 3, sig.shape[1] // 2 - 2:sig.shape[1] // 2 + 3] = 1
filter = signal.hann(50)
ConvOp = Convolve1D(size=sig.size, filter=filter, reshape_dims=sig.shape, axis=0)
filtered = (ConvOp * sig.reshape(-1)).reshape(sig.shape)
plt.figure()
plt.subplot(1,2,1)
plt.imshow(sig, cmap='plasma'); plt.title('Signal')
plt.subplot(1,2,2)
plt.imshow(filtered, cmap='plasma'); plt.title('Filtered Signal')
plt.show()