from pycsphere.green import ZonalWendland, ZonalGreenExponentiated

zonal_green=ZonalWendland(k=0)
iterated_zonal_green=ZonalGreenExponentiated(zonal_green, exponent=2)
zonal_green.plot(angles=True, fhandle=1)
iterated_zonal_green.plot(angles=True, fhandle=1)
plt.legend(['Original Green kernel', 'Iterated Green kernel'])
zonal_green.spectrum(n_max=20, fhandle=2, color_index=0)
iterated_zonal_green.spectrum(n_max=20, fhandle=2, color_index=1)
plt.legend(['Original Green kernel', 'Iterated Green kernel'])