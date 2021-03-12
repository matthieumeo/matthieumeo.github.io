from pycsphere.mesh import HEALPixPointSet
nside = HEALPixPointSet.angle2nside(angular_resolution=10)
healpix = HEALPixPointSet(nside, lonlat=True)
healpix.plot_delaunay_cells()
healpix.plot_voronoi_cells()
healpix.plot_tessellation()