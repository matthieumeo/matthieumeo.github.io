from pycsphere.green import ZonalMatern

for k in [0, 1,2,3]:
    zonal_green=ZonalMatern(k=k)
    zonal_green.plot(angles=True, fhandle=1)
plt.legend([f'$k={np.round(val, 1)}$' for val in [0, 1,2,3]])

for k in [0, 1,2,3]:
    zonal_green=ZonalMatern(k=k)
    zonal_green.spectrum(n_max=10, fhandle=2, color_index=k)
plt.legend([f'$k={np.round(val, 1)}$' for val in [0, 1,2,3]])