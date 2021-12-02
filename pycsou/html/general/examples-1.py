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
Gop = DownSampling(size=x.size, downsampling_factor=3)
Gop.compute_lipschitz_cst()
y = Gop(x)
l22_loss = (1 / 2) * SquaredL2Loss(dim=Gop.shape[0], data=y)
F = l22_loss * Gop
lambda_ = 0.1
H = lambda_ * L1Norm(dim=D.shape[0])
G = 0.01 * L1Norm(dim=Gop.shape[1])
pds = PrimalDualSplitting(dim=Gop.shape[1], F=F, G=G, H=H, K=D, verbose=None)
estimate, converged, diagnostics = pds.iterate()
plt.figure()
plt.stem(x, linefmt='C0-', markerfmt='C0o')
plt.stem(estimate['primal_variable'], linefmt='C1--', markerfmt='C1s')
plt.legend(['Ground truth', 'PDS Estimate'])
plt.show()