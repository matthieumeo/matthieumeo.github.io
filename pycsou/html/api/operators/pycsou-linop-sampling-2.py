import numpy as np
from pycsou.linop.sampling import Pooling
import matplotlib.pyplot as plt
import scipy.misc
img = scipy.misc.face(gray=True).astype(float)
PoolingOp = Pooling(shape=img.shape, block_size=(10,20))
pooled_img = (PoolingOp * img.flatten()).reshape(PoolingOp.output_shape)
adjoint_img = PoolingOp.adjoint(pooled_img.flatten()).reshape(img.shape)
plt.figure()
plt.imshow(img)
plt.colorbar()
plt.title('Original')
plt.figure()
plt.imshow(pooled_img)
plt.colorbar()
plt.title('Mean Pooling')
plt.figure()
plt.imshow(adjoint_img)
plt.colorbar()
plt.title('Mean Pooling followed by Unpooling')