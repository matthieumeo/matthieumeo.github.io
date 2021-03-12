from pycsphere.green import ZonalGreenFractionalLaplaceBeltrami

for exp in [2,2.5,3,3.5,4]:
    zonal_green=ZonalGreenFractionalLaplaceBeltrami(exponent=exp)
    zonal_green.plot(angles=True, fhandle=1)
plt.legend([f'$\\beta={np.round(val, 1)}$' for val in [2,2.5,3,3.5,4]])