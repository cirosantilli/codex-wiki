"""Original cyclotron-path sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Outputs paper-4-cyclotron-paths.png to caller CWD; honors MPLCONFIGDIR.
Nondimensional example: initial velocity 1 along x, signed cyclotron rate 1.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(7.8, 4.1), facecolor='white')
for ax, damping, title in zip(axes, [0, .09], ['No drag: a circle', 'Weak drag: a logarithmic spiral']):
    t = np.linspace(0, 2*np.pi if damping == 0 else 60, 3500)
    centre = 1/(damping+1j)
    z = centre*(1-np.exp(-(damping+1j)*t))
    ax.plot(z.real, z.imag, color='#1864ab', lw=1.6)
    ax.scatter([0], [0], color='#d95f02', s=30, zorder=5)
    ax.scatter([centre.real], [centre.imag], color='#2b8a3e', s=45, marker='x', zorder=5)
    ax.annotate('Start', xy=(0, 0), xytext=(-.55, .12), fontsize=9,
                color='#d95f02', arrowprops=dict(arrowstyle='->', color='#d95f02'))
    ax.text(centre.real+.08, centre.imag+.08, 'Centre' if damping==0 else 'Limiting point',
            fontsize=9, color='#2b8a3e')
    j = 500 if damping == 0 else 100
    ax.annotate('', xy=(z[j+35].real,z[j+35].imag),
                xytext=(z[j].real,z[j].imag),
                arrowprops=dict(arrowstyle='->', color='#1864ab', lw=1.7))
    ax.set(xlim=(-1.15, 1.2), ylim=(-2.15, .35), aspect='equal', xlabel='$x$', ylabel='$y$', title=title)
    ax.spines[['top', 'right']].set_visible(False)
fig.suptitle('Charged-particle paths for positive $qB$', fontsize=12)
fig.tight_layout()
fig.savefig('paper-4-cyclotron-paths.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
