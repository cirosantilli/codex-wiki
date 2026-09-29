"""Free-slip rotating-convection neutral curves; pinned root dependencies.

Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Same-basename PNG beside this generator.
"""
from pathlib import Path
# Honour an explicitly owned MPLCONFIGDIR; otherwise Matplotlib uses its normal cache.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def minimize_t(rhs, m):
    lo, hi = m / 2, max(m, rhs ** (1 / 3) + m)
    while (hi + m) ** 2 * (2 * hi - m) < rhs:
        hi *= 2
    for _ in range(90):
        mid = (lo + hi) / 2
        if (mid + m) ** 2 * (2 * mid - m) < rhs:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

Ta = 1e5
m = np.pi ** 2
k = np.linspace(.9, 15, 2200)
a = k * k + m
Rs = (a ** 3 + Ta * m) / (k * k)
ts = minimize_t(Ta * m, m)
fig, axes = plt.subplots(1, 2, figsize=(12, 5.6), dpi=100, facecolor='white')
for ax, P in zip(axes, [.3, .7]):
    Ro = (2 * (1 + P) * a ** 3 + 2 * P * P * Ta * m / (1 + P)) / (k * k)
    omega2 = P * P * ((1 - P) / (1 + P) * Ta * m / a - a * a)
    to = minimize_t(P * P * Ta * m / (1 + P) ** 2, m)
    ao = to + m
    assert (1 - P) / (1 + P) * Ta * m / ao - ao * ao > 0
    so = (2 * (1 + P) * ao ** 3 + 2 * P * P * Ta * m / (1 + P)) / to
    ss = ((ts + m) ** 3 + Ta * m) / ts
    ax.plot(k, Rs, color='#222222', label='Stationary neutral curve')
    ax.plot(k, np.where(omega2 > 0, Ro, np.nan), color='#2166ac',
            label=r'Oscillatory neutral curve ($\omega^2>0$)')
    ax.scatter([np.sqrt(ts)], [ss], c='#222222', zorder=3, marker='o')
    ax.scatter([np.sqrt(to)], [so], c='#2166ac', zorder=3, marker='o')
    selected = 'oscillatory' if so < ss else 'stationary'
    ax.set(title=rf'$\mathrm{{Pr}}={P}$: {selected} primary onset',
           xlabel='Horizontal wave number $k$', ylabel='Rayleigh number $R$',
           xlim=(.9, 15), ylim=(7000, 3e5), yscale='log')
    ax.grid(alpha=.22)
    ax.legend(loc='upper center', fontsize=9)
fig.suptitle(r'Rotating convection: $\mathrm{Ta}=10^5$, first vertical mode' + '\n'
             + 'Stress-free, impermeable, fixed-temperature plates', fontsize=14)
fig.subplots_adjust(left=.085, right=.975, bottom=.14, top=.78, wspace=.28)
fig.savefig((Path.cwd() / (Path(__file__).stem + '.png')), dpi=100,
            facecolor='white', transparent=False)
plt.close(fig)
