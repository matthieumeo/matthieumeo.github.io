from pycsphere.green import Radial2Zonal
from pycsou.math import Matern

radial_green=Matern(k=0, epsilon=1)
zonal_green=Radial2Zonal(radial_green=radial_green, order=3 / 2)
plt.plot(np.linspace(0,10,1024), radial_green(np.linspace(0,10,1024)))
plt.xlabel('$x$')
plt.ylabel('$\\phi(x)$')
plt.title('Radial Function')
zonal_green.plot()
zonal_green.spectrum(n_max=20)