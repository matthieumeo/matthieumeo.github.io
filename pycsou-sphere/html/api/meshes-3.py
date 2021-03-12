from pycsphere.mesh import RandomPointSet
res = RandomPointSet.angle2res(angular_resolution=10)
rnd = RandomPointSet(res, lonlat=True)
rnd.plot_delaunay_cells()
rnd.plot_tessellation()