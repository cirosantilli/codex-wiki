"""Original final-size sketch; Python 3.14, NumPy and Matplotlib root dependencies.
Run with the desired media directory as CWD. Honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib.pyplot as plt
lam = np.linspace(0.004, 0.9999, 700)
sigma = []
for value in lam:
    lo, hi = -np.log(value), 1.0 / value
    for _ in range(70):
        mid = (lo + hi) / 2
        if np.exp(-mid) + value * mid - 1 > 0:
            hi = mid
        else:
            lo = mid
    sigma.append(np.exp(-(lo + hi) / 2))
fig, ax = plt.subplots(figsize=(7.5, 4.2), layout='constrained')
fig.set_facecolor('white')
ax.plot(np.r_[0, lam, 1], np.r_[0, sigma, 1], lw=2.4, label='Nontrivial epidemic branch')
ax.plot([0, 1], [1, 1], '--', color='0.4', label='No epidemic: sigma = 1')
ax.plot([0, 1], [0, 1], ':', color='0.65', label='sigma = lambda')
ax.set(xlabel=r'$\lambda=a/(rS_0)$', ylabel=r'Surviving fraction $\sigma$', xlim=(0, 1), ylim=(0, 1.06), title=r'Final size: $\sigma-\lambda\log\sigma=1$')
ax.grid(alpha=.2)
ax.legend(loc='upper left', fontsize=9)
fig.savefig('paper-3-epidemic-final-size.png', dpi=130, facecolor='white', transparent=False)
