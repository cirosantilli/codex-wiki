"""Hamiltonian limit of three-to-one forcing.
Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Output only the PNG basename in cwd; honor caller's MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

fig, ax = plt.subplots(figsize=(7.5, 5), dpi=120, facecolor='white')
x = np.linspace(-1.1, 1.1, 251)
y = np.linspace(-0.78, 1.28, 251)
X, Y = np.meshgrid(x, y)
U = Y + X*X - Y*Y
V = -X - 2*X*Y
H = X*X + Y*Y + 2*X*X*Y - 2*Y**3/3
ax.streamplot(x, y, U, V, color='#a7afb3', density=0.9,
              linewidth=0.65, arrowsize=0.95)
inside = (Y > -0.5) & (np.abs(X) < (1-Y)/np.sqrt(3))
levels = [0.025, 0.08, 0.16, 0.24, 0.315]
contours = ax.contour(X, Y, np.ma.masked_where(~inside, H),
                     levels=levels, colors='#0072b2', linewidths=1.35)
ax.clabel(contours, inline=True, fontsize=8, fmt=lambda value: f'{value:g}')
vertices = np.array([[0, 1], [np.sqrt(3)/2, -0.5], [-np.sqrt(3)/2, -0.5], [0, 1]])
ax.plot(vertices[:, 0], vertices[:, 1], color='#b2182b', linewidth=2,
        linestyle='--')
ax.scatter(vertices[:3, 0], vertices[:3, 1], marker='s', color='#b2182b',
           s=40, zorder=6)
ax.scatter([0], [0], color='black', s=35, zorder=6)
ax.annotate('Centre: H = 0', xy=(0, 0), xytext=(0.15, -0.16), fontsize=9,
            arrowprops={'arrowstyle': '->', 'color': 'black'})
ax.text(0.04, 1.055, 'Saddle', fontsize=9)
ax.text(-1.06, -0.64, 'Saddle', fontsize=9)
ax.text(0.69, -0.64, 'Saddle', fontsize=9)
ax.set(xlabel='Real part x', ylabel='Imaginary part y',
       title='Periodic orbits and a triangular heteroclinic cycle',
       xlim=(-1.1, 1.1), ylim=(-0.78, 1.28), aspect='equal')
ax.set_facecolor('white')
ax.legend(handles=[Line2D([0], [0], color='#0072b2', label='Closed levels 0 < H < 1/3'),
                   Line2D([0], [0], color='#b2182b', linestyle='--', label='Separatrix H = 1/3')],
          loc='upper left', fontsize=8, framealpha=1)
ax.grid(alpha=0.16)
fig.subplots_adjust(left=0.13, right=0.97, bottom=0.12, top=0.9)
fig.savefig('paper-76-hamiltonian-orbits.png', dpi=120, facecolor='white', transparent=False)
plt.close(fig)
