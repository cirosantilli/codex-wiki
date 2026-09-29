"""One-mode magnetoconvection neutral curves; Python 3.14/root pinned dependencies.

Write paper-43-onsets.png in caller CWD, preserving caller MPLCONFIGDIR.
"""
from pathlib import Path
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'codex-wiki-paper-43-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

sigma, zeta = 1.0, 0.25
qstar = zeta * (sigma + 1) / (sigma * (1 - zeta))
q = np.linspace(0, 6, 501)
steady = 1 + q
hopf = (sigma + zeta) * (1 + zeta) / sigma + zeta * (sigma + zeta) * q / (sigma + 1)
fig, ax = plt.subplots(figsize=(10.7, 6.2), dpi=110)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.fill_between(q, 0, np.minimum(steady, hopf), color='#e1f0e7', label='Stable conductive state')
ax.plot(q, steady, color='#256c49', lw=2.5, label='Stationary neutral curve: r = 1 + q')
real = q >= qstar
ax.plot(q[real], hopf[real], color='#b43d36', lw=2.5, label='Hopf neutral curve: positive frequency')
# Formal continuation has no nonzero imaginary eigenvalue below the merger.
formal = np.linspace(0, qstar, 50)
ax.plot(formal, (sigma + zeta) * (1 + zeta) / sigma + zeta * (sigma + zeta) * formal / (sigma + 1),
        color='#b43d36', ls=':', lw=2, label='Formal continuation only (frequency² ≤ 0)')
ax.plot([qstar], [1 + qstar], 'o', color='#222222', ms=6)
ax.annotate('Double-zero merger\nq = 2/3, r = 5/3', xy=(qstar, 1 + qstar),
            xytext=(1.3, 3.1), arrowprops={'arrowstyle': '->', 'color': '#444444'}, fontsize=11)
ax.text(0.06, 0.56, 'Stationary first', fontsize=10.5)
ax.text(3.2, 1.1, 'Oscillatory first', fontsize=11)
ax.set(xlim=(0, 6), ylim=(0, 7.5), xlabel='Scaled magnetic strength q', ylabel='Scaled Rayleigh number r',
       title='Magnetoconvection onset for a fixed roll mode\nσ = 1, ζ = 1/4')
ax.grid(alpha=0.2)
ax.legend(loc='upper left', fontsize=9.5)
fig.tight_layout()
fig.savefig(Path.cwd() / 'paper-43-onsets.png', facecolor='white', transparent=False)
plt.close(fig)
