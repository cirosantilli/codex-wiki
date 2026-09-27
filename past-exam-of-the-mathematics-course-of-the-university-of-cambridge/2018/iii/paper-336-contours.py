"""Generate the square-root saddle contour and pole-crossing geometry."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 5), dpi=100, facecolor='white')
x = np.linspace(-3.4, 3.4, 600)
ax.plot(x, 1-x*x/4, color='#235d91', linewidth=2.2, label='Steepest descent: Im z = 1 − (Re z)²/4')
delta = 0.17
ax.plot([-3.4, -delta], [0, 0], color='#b65c21', linewidth=1.8, label='Original contour C')
ax.plot([delta, 3.4], [0, 0], color='#b65c21', linewidth=1.8)
theta = np.linspace(np.pi, 0, 100)
ax.plot(delta*np.cos(theta), delta*np.sin(theta), color='#b65c21', linewidth=1.8)
ax.plot([0, 0], [-2.3, 0], color='#5b5b5b', linestyle='--', linewidth=1.7, label='Square-root branch cut')
theta = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(theta), np.sin(theta), color='#b0b0b0', linewidth=1, linestyle=':')
ax.scatter([0], [1], color='#235d91', zorder=5)
ax.annotate('Saddle z = i', (0, 1), (0.3, 1.1))
ax.scatter([0.55], [0.42], color='#8e2b39', zorder=5)
ax.annotate('Crossed upper pole', (0.55, 0.42), (1.08, 0.35), arrowprops={'arrowstyle':'-', 'color':'#8e2b39'})
ax.scatter([-0.55], [-0.45], color='#376a45', zorder=5)
ax.annotate('Uncrossed lower pole', (-0.55, -0.45), (-2.8, -0.75), arrowprops={'arrowstyle':'-', 'color':'#376a45'})
for a, b in [((-2.25, -0.265625), (-1.95, 0.049375)), ((1.95, 0.049375), (2.25, -0.265625)), ((-2.7, 0), (-2.3, 0)), ((2.3, 0), (2.7, 0))]:
    ax.annotate('', xy=b, xytext=a, arrowprops={'arrowstyle':'->','color':'#235d91' if a[1] else '#b65c21'})
ax.set(xlim=(-3.4,3.4), ylim=(-2.1,1.5), xlabel='Re z', ylabel='Im z')
ax.set_aspect('equal', adjustable='box')
ax.legend(loc='lower center', fontsize=9, framealpha=1)
ax.grid(alpha=0.18)
fig.tight_layout()
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
