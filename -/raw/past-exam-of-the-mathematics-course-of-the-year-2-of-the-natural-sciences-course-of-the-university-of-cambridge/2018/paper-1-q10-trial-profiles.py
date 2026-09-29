"""Plot the optimized radial trial profile and central temperature; output to cwd.

Tested with Python 3.14; dependencies are in the repository pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(8, 3.4), layout='constrained')
r = np.linspace(0, 1, 500)
t = np.linspace(0, 1, 500)
axes[0].plot(r, 1-r**np.sqrt(2), color='#2465a6', linewidth=2.2)
axes[1].plot(t, np.exp(-(3+2*np.sqrt(2))*t), color='#b85522', linewidth=2.2)
axes[0].set(xlabel='$r$', ylabel=r'$T_{\mathrm{trial}}(r,0)$', title=r'Initial profile: $1-r^{\sqrt{2}}$')
axes[1].set(xlabel='$t$', ylabel=r'$T_{\mathrm{trial}}(0,t)$', title=r'Central decay: $e^{-(3+2\sqrt{2})t}$')
for ax in axes:
 ax.set(xlim=(0, 1), ylim=(0, 1.05))
 ax.spines[['top', 'right']].set_visible(False)
 ax.grid(alpha=.2)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=170, facecolor='white')
