from pycsphere.mesh import FibonacciPointSet
N = FibonacciPointSet.angle2N(angular_resolution=10)
fib = FibonacciPointSet(N, lonlat=True)
fib.plot_delaunay_cells()
fib.plot_tessellation()