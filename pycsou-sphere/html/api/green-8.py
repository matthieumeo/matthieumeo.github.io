from pycsphere.green import ZonalGreenIteratedBeltrami

for k in [1,2,3,4,5]:
    zonal_green=ZonalGreenIteratedBeltrami(k=k)
    zonal_green.plot(angles=True, fhandle=1)
plt.legend([f'$k={np.round(val, 1)}$' for val in [1,2,3,4,5]])