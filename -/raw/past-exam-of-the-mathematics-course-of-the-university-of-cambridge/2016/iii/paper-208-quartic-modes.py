"""Quartic target contours. Tested with Python 3.14, NumPy and Matplotlib.
Run from the directory in which the opaque PNG should be written.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

u = np.linspace(-0.7, 5.1, 450)
x, y = np.meshgrid(u, u)
v = x*x*y*y + x*x + y*y - 8*x - 8*y
fig, ax = plt.subplots(figsize=(7.8, 4.4), dpi=100, facecolor='white')
fig.subplots_adjust(left=0.10, right=0.96, bottom=0.14, top=0.86)
cs = ax.contour(x, y, (v+17)/2, levels=[0.1, 0.3, 0.7, 1.1, 1.5, 2.5, 4, 7, 12], cmap='viridis', linewidths=1.1)
ax.clabel(cs, levels=[0.3, 1.1, 2.5, 7], fmt='%g', fontsize=8)
a, b = 2+np.sqrt(3), 2-np.sqrt(3)
ax.scatter([a,b], [b,a], color='#b2182b', s=45, zorder=5, label='Density modes')
r = np.roots([1,0,1,-4]); d = r[np.abs(r.imag)<1e-10].real[0]
ax.scatter([d], [d], marker='x', color='#333333', s=60, zorder=5, label='Saddle')
ax.plot([b,a], [a,b], ls='--', color='#777777', alpha=0.5, linewidth=1)
ax.set(xlim=(-0.7,5.1), ylim=(-0.7,5.1), xlabel=r'$x_1$', ylabel=r'$x_2$', aspect='equal')
ax.set_title(r'Quartic target: contours of $-\log(f/f_{\max})$', fontsize=12, pad=11)
ax.legend(loc='upper right', fontsize=9, framealpha=1)
fig.savefig('paper-208-quartic-modes.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
