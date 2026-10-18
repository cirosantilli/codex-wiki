"""Original geometry diagrams. Write the matching PNG to the working directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), layout='constrained')
ax = axes[0]
t = np.linspace(0, np.pi, 700)
ax.plot(t*np.cos(t), t*np.sin(t), color='#1769aa', lw=2)
ax.scatter([0], [0], facecolor='white', edgecolor='#1769aa', zorder=4)
ax.scatter([-np.pi, 0], [0, np.pi/2], color='#1769aa', zorder=4)
ax.annotate(r'$\theta=\pi,\ r=\pi$', (-np.pi, 0), xytext=(-3.35, .32))
ax.annotate(r'$\theta=\pi/2,\ r=\pi/2$', (0, np.pi/2), xytext=(-.7, 2.05))
ax.annotate('origin excluded', (0, 0), xytext=(.35, -.5), arrowprops={'arrowstyle':'->'})
ax.set(xlim=(-3.6, 1.3), ylim=(-.7, 2.5), title=r'Principal argument: $0<\theta\leq\pi$', xlabel=r'$\mathrm{Re}\,z$', ylabel=r'$\mathrm{Im}\,z$')
ax = axes[1]
t = np.linspace(0, 2*np.pi, 700)
e6 = np.array([np.sqrt(3), 1])/2
e2 = np.array([-1, np.sqrt(3)])/2
p = np.sqrt(2/3)*e6[:, None]*np.cos(t) + np.sqrt(2)*e2[:, None]*np.sin(t)
ax.plot(*p, lw=2, color='#1769aa')
for e, r, label, color in [(e6, np.sqrt(2/3), r'$\sqrt{2/3}$ at $30^\circ$', '#c04d25'), (e2, np.sqrt(2), r'$\sqrt{2}$ at $120^\circ$', '#168347')]:
    ax.plot(*np.column_stack((-r*e, r*e)), '--', color=color, lw=1.6)
    ax.annotate(label, r*e, xytext=(.1 if e[0]>0 else -1.7, .3 if e[0]>0 else 1.52), color=color)
ax.set(xlim=(-1.8, 1.8), ylim=(-1.6, 1.9), title=r'Ellipse: $6u^2+2v^2=4$', xlabel=r'$x_1$', ylabel=r'$x_2$')
for ax in axes:
    ax.axhline(0, color='.6', lw=.6)
    ax.axvline(0, color='.6', lw=.6)
    ax.set_aspect('equal')
    ax.grid(alpha=.18)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
