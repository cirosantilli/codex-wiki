"""Requested initial-profile sketches; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the intended output directory. Writes only the PNG basename to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 7), dpi=120, facecolor='white')
L = 8.0
z = np.linspace(0, L, 501)
w = np.cosh(L-z)/np.cosh(L)-1
rate = np.sinh(L-z)/np.cosh(L)
axes[0, 0].plot(z, w, label='Exact initial profile')
axes[0, 0].plot(z, np.exp(-z)-1, '--', label='Tall-column limit')
axes[0, 0].set(title='Tall column: downward velocity', xlabel=r'$Z=z/\widehat z$', ylabel=r'$W=w/\widehat w$')
axes[0, 1].plot(z, rate, label='Exact initial profile')
axes[0, 1].plot(z, np.exp(-z), '--', label='Tall-column limit')
axes[0, 1].set(title='Tall column: basal thickening', xlabel=r'$Z=z/\widehat z$', ylabel=r'$\phi_T/\phi_0$')
L = 0.15
s = np.linspace(0, 1, 501)
z = L*s
axes[1, 0].plot(s, (np.cosh(L-z)/np.cosh(L)-1)/L**2, label='Exact initial profile')
axes[1, 0].plot(s, s**2/2-s, '--', label='Short-column limit')
axes[1, 0].set(title='Short column: extensional fall', xlabel=r'$s=Z/\Lambda_0$', ylabel=r'$W/\Lambda_0^2$')
axes[1, 1].plot(s, np.sinh(L-z)/np.cosh(L)/L, label='Exact initial profile')
axes[1, 1].plot(s, 1-s, '--', label='Short-column limit')
axes[1, 1].set(title='Short column: distributed thickening', xlabel=r'$s=Z/\Lambda_0$', ylabel=r'$\phi_T/(\phi_0\Lambda_0)$')
for ax in axes.flat:
    ax.set_facecolor('white')
    ax.grid(alpha=0.25)
    ax.legend(fontsize=8)
    ax.axhline(0, color='black', linewidth=0.6)
fig.suptitle('Initial column profiles: annular drag versus extensional stress', fontsize=14)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig('paper-73-column-limits.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
