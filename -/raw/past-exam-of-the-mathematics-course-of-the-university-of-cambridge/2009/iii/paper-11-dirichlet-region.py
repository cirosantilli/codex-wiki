"""Origin-centered Gaussian-integer Dirichlet region.
Tested with Python 3.14 and the root NumPy/Matplotlib dependencies.
Writes paper-11-dirichlet-region.png to the caller's current directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

angle = np.linspace(np.pi, 1.5 * np.pi, 250)
first = 1 + 1j + np.exp(1j * angle)
boundary = np.concatenate([first * (-1j) ** j for j in range(4)])
fig, ax = plt.subplots(figsize=(6.5, 6.1), facecolor='white')
ax.set_facecolor('white')
ax.fill(boundary.real, boundary.imag, color='#dcecf5', label='Dirichlet region', zorder=1)
outer = np.exp(1j * np.linspace(0, 2 * np.pi, 600))
ax.plot(outer.real, outer.imag, color='#777777', lw=1.3)
for j in range(4):
    arc = first * (-1j) ** j
    ax.plot(arc.real, arc.imag, color='#236a99', lw=2.4, zorder=3)
for sx in [-1, 1]:
    for sy in [-1, 1]:
        ax.scatter([sx / 2], [sy / 2], color='#a14c34', s=35, zorder=4)
ax.scatter([], [], color='#a14c34', s=35, label='Neighboring orbit points')
ax.scatter([0], [0], color='#222222', s=30, zorder=4)
ax.text(.045, -.075, '0', fontsize=11)
for x, y, text, dx, dy in [(1, 0, '1', .055, 0), (0, 1, 'i', 0, .065), (-1, 0, '−1', -.09, 0), (0, -1, '−i', 0, -.065)]:
    ax.scatter([x], [y], s=32, facecolors='white', edgecolors='#236a99', zorder=5)
    ax.text(x + dx, y + dy, text, ha='center', va='center', fontsize=12)
ax.set_aspect('equal')
ax.set_xlim(-1.17, 1.17)
ax.set_ylim(-1.18, 1.17)
ax.set_xlabel('Re z')
ax.set_ylabel('Im z')
ax.set_title('An ideal quadrilateral in the hyperbolic disc')
ax.legend(loc='lower center', bbox_to_anchor=(.5, -.19), ncol=2, fontsize=9, frameon=False)
fig.tight_layout()
fig.savefig('paper-11-dirichlet-region.png', dpi=155, facecolor='white', transparent=False)
plt.close(fig)
