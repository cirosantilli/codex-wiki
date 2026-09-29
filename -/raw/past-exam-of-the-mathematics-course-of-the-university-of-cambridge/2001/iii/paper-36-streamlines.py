"""Magnetic skin-layer bulk-slip illustration; Python 3.14, NumPy/Matplotlib.

Writes only paper-36-streamlines.png in the caller's current directory.
The supplied MPLCONFIGDIR is respected. The pictured bulk solution omits
an asymptotically thin physical no-slip skin layer.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-4, 4, 501)
y = np.linspace(0, 4, 251)
xx, yy = np.meshgrid(x, y)
z = xx + 1j * yy
w = z + 1j
f = 1 / (4 * w**3) - 1j / (8 * w**2)
fp = -3 / (4 * w**4) + 1j / (4 * w**3)
u = f.real + yy * (1j * fp).real
v = -yy * fp.real
fig, ax = plt.subplots(figsize=(8, 5.3), facecolor='white', layout='constrained')
ax.set_facecolor('white')
ax.streamplot(x, y, u, v, color='#2166ac', density=(1.35, 1.1),
              linewidth=1.1, arrowsize=1.05, minlength=0.06)
ax.axhline(0, color='black', lw=2)
for start, end in [(-2.8, -2.25), (-1.5, -0.95), (2.8, 2.25), (1.5, 0.95)]:
    ax.annotate('', xy=(end, 0.08), xytext=(start, 0.08),
                arrowprops=dict(arrowstyle='->', color='#1b7837', lw=2.4))
ax.annotate('Upwelling above wire', xy=(0, 1.0), xytext=(0.9, 2.4),
            arrowprops=dict(arrowstyle='->', color='black'), fontsize=10,
            bbox=dict(facecolor='white', edgecolor='none', alpha=1))
ax.set(xlim=(-4, 4), ylim=(0, 4), xlabel=r'$x/b$', ylabel=r'$y/b$')
ax.set_aspect('equal')
ax.set_title('Bulk Stokes flow driven by magnetic skin-layer slip', fontsize=13)
fig.supxlabel('Effective outer boundary at y = 0; physical no-slip skin layer unresolved', fontsize=10)
fig.savefig('paper-36-streamlines.png', dpi=140, facecolor='white', transparent=False)
plt.close(fig)
