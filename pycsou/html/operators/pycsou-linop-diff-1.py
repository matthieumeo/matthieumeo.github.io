import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.diff import FirstDerivative

x = np.repeat([0,2,1,3,0,2,0], 10)
Dop_bwd = FirstDerivative(size=x.size, kind='backward')
Dop_fwd = FirstDerivative(size=x.size, kind='forward')
Dop_cent = FirstDerivative(size=x.size, kind='centered')
y_bwd = Dop_bwd * x
y_cent = Dop_cent * x
y_fwd = Dop_fwd * x
plt.figure()
plt.plot(np.arange(x.size), x)
plt.plot(np.arange(x.size), y_bwd)
plt.plot(np.arange(x.size), y_cent)
plt.plot(np.arange(x.size), y_fwd)
plt.legend(['Signal', 'Backward', 'Centered', 'Forward'])
plt.title('First derivative')
plt.show()