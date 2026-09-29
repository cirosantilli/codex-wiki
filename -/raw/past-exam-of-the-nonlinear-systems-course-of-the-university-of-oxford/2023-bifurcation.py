"""Original fixed-point diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run in the desired output directory; writes 2023-bifurcation.png there.
Dependencies are already listed in the wiki's root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(9, 4.5), layout='constrained', facecolor='white')
for left, right in [(-1.65, -1), (0, 1.75)]:
    ax.plot([left, right], [0, 0], color='#b14826', ls='--', lw=2)
ax.plot([-1, 0], [0, 0], color='#12659b', lw=3, label='Attracting fixed points')
for left, right in [(-1.65, 0), (1, 1.75)]:
    mu = np.linspace(left, right, 650)
    y = np.sqrt(mu * (mu - 1))
    for sign in [-1, 1]:
        ax.plot(mu, sign * y, color='#b14826', ls='--', lw=1.8)
ax.plot([], [], color='#b14826', ls='--', lw=1.8, label='Unstable fixed points')
ax.scatter([-1, 0, 1], [0, 0, 0], s=65, facecolor='white', edgecolor='black', zorder=6)
for x, text, xytext in [(-1, '1:4 resonance\n$\\lambda=\\pm i$', (-1.03, .85)),
                         (0, 'Subcritical pitchfork\n$\\lambda=0,1$', (0, -1.45)),
                         (1, 'Double $+1$\nnonsemisimple', (.92, 1.48))]:
    ax.annotate(text, (x, 0), xytext=xytext, ha='center', fontsize=10,
                arrowprops={'arrowstyle': '-', 'color': '#444444'})
ax.text(-1.49, 1.53, 'Saddles', fontsize=10, color='#b14826')
ax.text(1.51, -.90, 'Saddles', fontsize=10, color='#b14826')
ax.axvline(0, color='#aaaaaa', lw=.6, zorder=0)
ax.set(xlim=(-1.65, 1.75), ylim=(-2.2, 2.2), xlabel=r'Parameter $\mu$', ylabel=r'Fixed-point coordinate $y$',
       title=r'Fixed points: $y=0$ and $y=\pm\sqrt{\mu(\mu-1)}$, with $x=\mu y$')
ax.set_xticks([-1, 0, 1])
ax.grid(alpha=.14)
ax.legend(loc='lower right', fontsize=9, framealpha=1)
fig.savefig(Path.cwd() / '2023-bifurcation.png', dpi=120, facecolor='white')
plt.close(fig)
