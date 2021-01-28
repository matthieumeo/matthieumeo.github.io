import numpy as np
import matplotlib.pyplot as plt
from pycsou.linop.diff import FirstDerivative
from pycsou.func.loss import SquaredL2Loss
from pycsou.func.penalty import L1Norm, NonNegativeOrthant
from pycsou.linop.sampling import DownSampling
from pycsou.opt.proxalgs import PrimalDualSplitting

x = np.repeat([0, 2, 1, 3, 0, 2, 0], 10)
D = FirstDerivative(size=x.size, kind='forward')
D.compute_lipschitz_cst(tol=1e-3)
rng = np.random.default_rng(0)
G = DownSampling(size=x.size, downsampling_factor=3)
G.compute_lipschitz_cst()
y = G(x)
l22_loss = (1 / 2) * SquaredL2Loss(dim=G.shape[0], data=y)
F = l22_loss * G
lambda_ = 0.1
H = lambda_ * L1Norm(dim=D.shape[0])
G = 0.01 * L1Norm(dim=G.shape[1])
pds = PrimalDualSplitting(dim=G.shape[1], F=F, G=G, H=H, K=D, verbose=None)
estimate, converged, diagnostics = pds.iterate()
plt.figure()
plt.stem(x, linefmt='C0-', markerfmt='C0o')
plt.stem(estimate['primal_variable'], linefmt='C1--', markerfmt='C1s')
plt.legend(['Ground truth', 'PDS Estimate'])
plt.show()