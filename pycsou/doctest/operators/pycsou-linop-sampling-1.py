import numpy as np
from pycsou.linop.sampling import DownSampling
import matplotlib.pyplot as plt
import scipy.misc
img = scipy.misc.face(gray=True).astype(float)
DownSampOp = DownSampling(size=img.size, shape=img.shape, downsampling_factor=(3,6))
down_sampled_img = (DownSampOp * img.flatten()).reshape(DownSampOp.output_shape)
up_sampled_img = DownSampOp.adjoint(down_sampled_img.flatten()).reshape(img.shape)
plt.figure()
plt.imshow(img)
plt.colorbar()
plt.title('Original')
plt.figure()
plt.imshow(down_sampled_img)
plt.colorbar()
plt.title('Downsampling')
plt.figure()
plt.imshow(up_sampled_img)
plt.colorbar()
plt.title('Downsampling followed by Upsampling')