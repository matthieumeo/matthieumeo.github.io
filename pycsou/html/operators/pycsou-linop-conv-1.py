import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.conv import Convolve1D
from scipy import signal
sig = np.repeat([0., 1., 0.], 100)
filter = signal.hann(50); filter[filter.size//2:] = 0
ConvOp = Convolve1D(size=sig.size, filter=filter)
filtered = ConvOp * sig
correlated = ConvOp.H * sig
backprojected = ConvOp.DomainGram * sig
plt.figure()
plt.subplot(2,2,1)
plt.plot(sig); plt.plot(np.linspace(0, 50, filter.size), filter); plt.legend(['Signal', 'Filter'])
plt.subplot(2,2,2)
plt.plot(filtered); plt.title('Filtered Signal')
plt.subplot(2,2,3)
plt.plot(correlated); plt.title('Correlated Signal')
plt.subplot(2,2,4)
plt.plot(backprojected); plt.title('Backprojected Signal')
plt.show()