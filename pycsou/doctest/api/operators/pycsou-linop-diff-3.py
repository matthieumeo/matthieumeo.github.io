import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.diff import GeneralisedDerivative

x  = np.linspace(-2.5, 2.5, 500)
z = np.exp(-x ** 2)
Dop_it = GeneralisedDerivative(size=x.size, kind_op='iterated', order=4)
Dop_sob = GeneralisedDerivative(size=x.size, kind_op='sobolev', order=2, constant=1e-2)
Dop_exp = GeneralisedDerivative(size=x.size, kind_op='exponential', order=4, constant=-1e-2)
Dop_pol = GeneralisedDerivative(size=x.size, kind_op='polynomial',
                                coeffs= 1/2 * np.array([1e-8, 0, -2 * 1e-4, 0, 1]))
y_it = Dop_it * z
y_sob = Dop_sob * z
y_exp = Dop_exp * z
y_pol = Dop_pol * z
plt.figure()
plt.plot(x, z)
plt.title('Signal')
plt.show()
plt.figure()
plt.plot(x, y_it)
plt.plot(x, y_sob)
plt.plot(x, y_exp)
plt.plot(x, y_pol)
plt.legend(['Iterated', 'Sobolev', 'Exponential', 'Polynomial'])
plt.title('Generalised derivatives')
plt.show()