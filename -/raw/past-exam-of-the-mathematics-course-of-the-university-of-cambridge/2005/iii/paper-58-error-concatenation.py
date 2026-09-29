"""Plot ideal five-qubit concatenation; write the PNG basename to caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def failure(p):
    return p * p * (10 + p * (-20 + p * (15 - 4 * p)))


lo, hi = 0.0, 0.5
for _ in range(70):
    mid = (lo + hi) / 2
    if 4 * mid**3 - 11 * mid**2 + 9 * mid - 1 < 0:
        lo = mid
    else:
        hi = mid
threshold = (lo + hi) / 2
fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.7), facecolor='white')
for ax, p in zip(axes, [np.linspace(0, 0.23, 700), np.geomspace(0.001, 0.1, 700)]):
    ax.set_facecolor('white')
    ax.plot(p, p, ':', color='#333333', lw=1.9, label='Unencoded: p')
    ax.plot(p, failure(p), color='#1767a6', lw=2, label='One level: f(p)')
    ax.plot(p, failure(failure(p)), color='#993c83', lw=2, label='Two levels: f(f(p))')
    ax.set_xlabel('Physical error probability p')
    ax.set_ylabel('Logical error probability')
    ax.grid(True, color='#dddddd', lw=0.6)
axes[0].axvline(threshold, ls='--', color='#b26600', lw=1.4,
               label=f'Threshold: {threshold:.5f}')
axes[0].set_xlim(0, 0.23)
axes[0].set_ylim(0, 0.52)
axes[0].set_title('Below threshold, each level helps', fontsize=11)
axes[0].legend(loc='upper left', frameon=False, fontsize=8.5)
axes[1].set_xscale('log')
axes[1].set_yscale('log')
axes[1].set_title('Quadratic and quartic suppression', fontsize=11)
axes[1].text(0.0016, 0.018, 'f(p) ≈ 10p²\nf(f(p)) ≈ 1000p⁴', fontsize=10)
fig.tight_layout()
fig.savefig(Path.cwd() / 'paper-58-error-concatenation.png', dpi=140,
            facecolor='white', transparent=False)
plt.close(fig)
