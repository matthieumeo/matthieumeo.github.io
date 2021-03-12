from pycsphere.green import ZonalGreenIteratedLaplaceBeltrami

for exp in [1,2,3,4,5]:
    zonal_green=ZonalGreenIteratedLaplaceBeltrami(exponent=exp)
    zonal_green.plot(angles=True, fhandle=1)
plt.legend([f'$k={np.round(val, 1)}$' for val in [1,2,3,4,5]])