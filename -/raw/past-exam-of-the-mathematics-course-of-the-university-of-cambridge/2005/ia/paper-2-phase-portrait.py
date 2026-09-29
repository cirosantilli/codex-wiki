"""Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7; output to caller CWD.
Respects caller MPLCONFIGDIR; exact forward trajectories, opaque white PNG.
"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 6.3), layout='constrained')
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
theta = np.linspace(0, 2*np.pi, 500)
ax.plot(np.cos(theta), np.sin(theta), color='#222222', lw=2.5, label='Attracting periodic orbit: r = 1')
for r0, color in [(0.2, '#2878b5'), (1.85, '#c65d20')]:
    for theta0 in np.linspace(0, 2*np.pi, 4, endpoint=False):
        t = np.linspace(0, 7, 700)
        r = 1/np.sqrt(1+(r0**-2-1)*np.exp(-2*t))
        x, y = r*np.cos(theta0+t), r*np.sin(theta0+t)
        ax.plot(x, y, color=color, lw=1.5, alpha=.85)
        for j in [50, 170]:
            ax.annotate('', xy=(x[j+12], y[j+12]), xytext=(x[j], y[j]),
                        arrowprops={'arrowstyle': '->', 'color': color, 'lw': 1.6})
for a in [.4, 2.0, 3.6, 5.2]:
    ax.annotate('', xy=(np.cos(a+.16), np.sin(a+.16)), xytext=(np.cos(a), np.sin(a)),
                arrowprops={'arrowstyle': '->', 'color': '#222222', 'lw': 2})
ax.scatter([0], [0], c='#b52240', s=42, zorder=8, label='Unstable focus: origin')
ax.axhline(0, lw=.6, color='#bbbbbb', zorder=0)
ax.axvline(0, lw=.6, color='#bbbbbb', zorder=0)
ax.set(xlim=(-2.05, 2.05), ylim=(-2.05, 2.05), xlabel='x', ylabel='y',
       title='Counterclockwise flow toward a stable unit circle')
ax.set_aspect('equal')
ax.legend(loc='lower center', framealpha=1, fontsize=9)
fig.savefig('paper-2-phase-portrait.png', dpi=150, facecolor='white', transparent=False)
plt.close(fig)
