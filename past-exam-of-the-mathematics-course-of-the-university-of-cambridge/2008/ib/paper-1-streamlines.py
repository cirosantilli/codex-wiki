"""Draw the exponential hyperbolic flow. Tested with Python 3.14.

Uses the root project's NumPy and Matplotlib dependencies; writes to caller CWD.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(6.2, 5.2), layout='constrained', facecolor='white')
x = np.linspace(0.012, 3.2, 1600)
colors = ['#2469a0', '#138575', '#b65a27']
for magnitude, color in zip([0.25, 1.0, 4.0], colors):
    y = np.log(magnitude) - np.log(np.sinh(x))
    for side in [-1, 1]:
        ax.plot(side*x, y, color=color, linewidth=1.7)
        for arrow_y in [-1.0, 1.0]:
            xa = np.arcsinh(magnitude*np.exp(-arrow_y))
            xb = np.arcsinh(magnitude*np.exp(-(arrow_y-0.20)))
            if xb < 3.1:
                ax.annotate('', xy=(side*xb, arrow_y-0.20),
                            xytext=(side*xa, arrow_y),
                            arrowprops={'arrowstyle': '-|>', 'color': color, 'lw': 1.6})
ax.plot([0, 0], [-3, 3], color='#30343a', linewidth=1.7)
for ya in [-1.6, 0.0, 1.6]:
    ax.annotate('', xy=(0, ya-0.3), xytext=(0, ya),
                arrowprops={'arrowstyle': '-|>', 'color': '#30343a', 'lw': 1.7})
ax.set(xlim=(-3.1, 3.1), ylim=(-3, 3), xlabel='$x$', ylabel='$y$',
       title=r'Streamlines: $e^y\sinh x=K$')
ax.set_aspect('equal')
ax.grid(alpha=0.18)
ax.text(-1.8, 2.65, '$K<0$', ha='center')
ax.text(1.8, 2.65, '$K>0$', ha='center')
ax.text(0.12, 2.4, '$K=0$', color='#30343a')
ax.text(0.02, 0.02, r'$|K|=0.25,\ 1,\ 4$; arrows show flow',
        transform=ax.transAxes, fontsize=9,
        bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': 1})
fig.savefig('paper-1-streamlines.png', dpi=145, facecolor='white', transparent=False)
plt.close(fig)
