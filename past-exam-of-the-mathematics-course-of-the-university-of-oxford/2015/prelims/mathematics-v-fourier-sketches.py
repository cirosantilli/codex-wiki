"""Original Q4 sketches. Run in the mirrored _media directory; writes only to cwd.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7 (root pyproject.toml).
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
u = np.linspace(0, 1, 1601)
g = np.exp(u)
fig, axes = plt.subplots(2, 2, figsize=(9.4, 6.2), layout='constrained', sharex=True)
for ax in axes.flat:
    ax.set(xlim=(-.045, 1.045), ylim=(-.15, 3.1), xlabel='$x/L$', ylabel='value')
    ax.set_xticks([0, .5, 1]); ax.set_yticks([0, 1, 2, np.e], ['$0$', '$1$', '$2$', '$e$'])
    ax.grid(alpha=.2); ax.spines[['top', 'right']].set_visible(False)
axes[0, 0].plot(u, g, color='#236e9d', lw=2.3)
axes[0, 0].scatter([0, 1], [1, np.e], color='#236e9d', zorder=5, s=35)
axes[0, 0].set_title('Cosine series: exact sum')
axes[0, 1].plot(u[1:-1], g[1:-1], color='#236e9d', lw=2.3)
axes[0, 1].scatter([0, 1], [1, np.e], facecolor='white', edgecolor='#236e9d', s=42, zorder=5)
axes[0, 1].scatter([0, 1], [0, 0], color='#236e9d', s=35, zorder=5)
axes[0, 1].set_title('Sine series: sum is zero at the endpoints')
n = np.arange(1, 13)[:, None]
a = 2*((-1.)**n*np.e-1)/(1+(n*np.pi)**2)
b = 2*n*np.pi*(1-(-1.)**n*np.e)/(1+(n*np.pi)**2)
cn = np.e-1 + np.sum(a*np.cos(n*np.pi*u), axis=0)
sn = np.sum(b*np.sin(n*np.pi*u), axis=0)
for ax, approx, name in [(axes[1, 0], cn, 'Cosine'), (axes[1, 1], sn, 'Sine')]:
    ax.plot(u, g, color='#236e9d', lw=1.8, label=r'$e^{x/L}$')
    ax.plot(u, approx, color='#c45330', lw=1.5, label='$N=12$')
    ax.set_title(name+' partial sum')
    ax.legend(loc='upper left', frameon=False)
fig.savefig('mathematics-v-fourier-sketches.png', dpi=135, facecolor='white', transparent=False)
plt.close(fig)
