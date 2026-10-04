"""Original six tree diagrams. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.
Write only the PNG basename to the caller's CWD; respect caller MPLCONFIGDIR.
"""
from itertools import permutations
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(12, 6.4), facecolor='white')
for ax, order in zip(axes.flat, permutations((1, 2, 3))):
    ax.set_facecolor('white')
    ax.set_xlim(-0.12, 1.12)
    ax.set_ylim(0.06, 1.08)
    ax.axis('off')
    y = 0.30
    ax.plot([0, 1], [y, y], color='black', lw=1.5)
    for x in (0.12, 0.38, 0.62, 0.90):
        ax.annotate('', xy=(x + 0.04, y), xytext=(x - 0.04, y),
                    arrowprops=dict(arrowstyle='-|>', color='black', lw=1.3))
    for x, k in zip((0.25, 0.50, 0.75), order):
        t = np.linspace(0, 1, 250)
        ax.plot(x + 0.012 * np.sin(10 * np.pi * t), y + 0.48 * t,
                color='#155a91', lw=1.5)
        ax.plot(x, y, 'o', color='black', ms=3)
        ax.text(x, 0.84, rf'$\gamma(q_{k})$', ha='center', fontsize=12)
    ax.text(0.00, 0.18, r'$e^-(p)$', ha='center', fontsize=12)
    ax.text(1.00, 0.18, r'$e^+(p^{\prime})$', ha='center', fontsize=12)
    ax.text(0.375, 0.38, rf'$p-q_{order[0]}$', ha='center', fontsize=10)
    ax.text(0.625, 0.38, rf'$q_{order[2]}-p^{{\prime}}$', ha='center', fontsize=10)
    ax.set_title('Photon order ' + ', '.join(map(str, order)), fontsize=13)
fig.suptitle('Electron–positron annihilation into three photons', fontsize=17, y=0.98)
fig.text(0.5, 0.02, 'Straight arrows: fermion flow. All three photons are outgoing.',
         ha='center', fontsize=12)
fig.subplots_adjust(top=0.86, bottom=0.10, wspace=0.19, hspace=0.40)
fig.savefig('paper-62-three-photon-diagrams.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
