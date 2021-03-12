from pycsphere.green import ZonalGreenSobolev

for exp in [2,2.5,3,3.5,4]:
    zonal_green=ZonalGreenSobolev(alpha=1., exponent=exp)
    zonal_green.plot(angles=True, fhandle=1)
plt.legend([f'$\\beta={np.round(val, 1)}$' for val in [2,2.5,3,3.5,4]])
plt.title('$\\alpha=1$')

for exp in [2,2.5,3,3.5,4]:
    zonal_green=ZonalGreenSobolev(alpha=5., exponent=exp)
    zonal_green.plot(angles=True, fhandle=2)
plt.legend([f'$\\beta={np.round(val, 1)}$' for val in [2,2.5,3,3.5,4]])
plt.title('$\\alpha=5$')