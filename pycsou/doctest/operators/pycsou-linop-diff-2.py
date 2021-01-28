import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.diff import SecondDerivative

x = np.linspace(-2.5, 2.5, 200)
z = np.piecewise(x, [x < -1, (x >= - 1) * (x<0), x>=0], [lambda x: -x, lambda x: 3 * x + 4, lambda x: -0.5 * x + 4])
Dop = SecondDerivative(size=x.size)
y = Dop * z
plt.figure()
plt.plot(np.arange(x.size), z)
plt.title('Signal')
plt.show()
plt.figure()
plt.plot(np.arange(x.size), y)
plt.title('Second Derivative')
plt.show()