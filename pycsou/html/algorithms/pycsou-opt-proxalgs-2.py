import numpy as np
import matplotlib.pyplot as plt
from pycsou.func.loss import SquaredL2Loss
from pycsou.func.penalty import L1Norm
from pycsou.linop.base import DenseLinearOperator
from pycsou.opt.proxalgs import APGD

rng = np.random.default_rng(0)
G = DenseLinearOperator(rng.standard_normal(15).reshape(3,5))
G.compute_lipschitz_cst()
x = np.zeros(G.shape[1])
x[1] = 1
x[-2] = -1
y = G(x)
l22_loss = (1/2) * SquaredL2Loss(dim=G.shape[0], data=y)
F = l22_loss * G
lambda_ = 0.9 * np.max(np.abs(F.gradient(0 * x)))
G = lambda_ * L1Norm(dim=G.shape[1])
apgd = APGD(dim=G.shape[1], F=F, G=None, acceleration='CD', verbose=None)
estimate, converged, diagnostics = apgd.iterate()
plt.figure()
plt.stem(x, linefmt='C0-', markerfmt='C0o')
plt.stem(estimate['iterand'], linefmt='C1--', markerfmt='C1s')
plt.legend(['Ground truth', 'LASSO Estimate'])
plt.show()