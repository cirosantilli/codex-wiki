import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.6), dpi=100, layout='constrained')
y = np.linspace(0.025, 3, 900)
for ax, coupling in zip(axes, [1.5, 4.0]):
    line = 2*y/coupling
    low, high = np.tanh(y), 1/np.tanh(y)
    allowed = (line >= low) & (line <= high)
    ax.plot(y, low, label=r'$\tanh y$', color='#1765a4')
    ax.plot(y, high, label=r'$\coth y$', color='#b33a32')
    ax.plot(y, line, label=r'$2y/(\lambda a)$', color='#222222')
    ax.fill_between(y, 0, 3, where=allowed, color='#80c49a', alpha=0.25, label='allowed y')
    ax.set(xlim=(0, 3), ylim=(0, 3), xlabel=r'$y=\kappa a/2$', title=rf'$\lambda a={coupling:g}$')
    ax.spines[['top', 'right']].set_visible(False)
axes[0].set_ylabel('Boundary functions')
axes[1].legend(fontsize=8, loc='upper right')
fig.suptitle('One negative-energy band; its upper energy reaches zero for lambda a ≤ 2', fontsize=10)
fig.savefig('paper-3-delta-comb-bands.png', facecolor='white', transparent=False)
plt.close(fig)
