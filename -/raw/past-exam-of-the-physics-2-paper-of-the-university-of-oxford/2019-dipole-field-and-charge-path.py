"""Original electrostatic field and orbit diagrams; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 12})
fig, (field, orbit) = plt.subplots(1, 2, figsize=(10, 4.8), layout='constrained', facecolor='white')
x = np.linspace(-2.5, 2.5, 181)
y = np.linspace(-2.5, 2.5, 181)
xx, yy = np.meshgrid(x, y)
ex = np.zeros_like(xx)
ey = np.zeros_like(xx)
mask = np.zeros_like(xx, dtype=bool)
for q, yq in [(1, 0.45), (-1, -0.45)]:
    rr2 = xx**2 + (yy-yq)**2
    mask |= rr2 < 0.13**2
    rr2 = np.maximum(rr2, 0.05**2)
    ex += q*xx/rr2**1.5
    ey += q*(yy-yq)/rr2**1.5
norm = np.maximum(np.hypot(ex, ey), 1e-9)
field.streamplot(x, y, np.ma.array(ex/norm, mask=mask), np.ma.array(ey/norm, mask=mask), density=1.1, color='#416f91', linewidth=0.9, arrowsize=1)
for q, yq, color in [(1, 0.45, '#cf4338'), (-1, -0.45, '#2874bb')]:
    field.scatter([0], [yq], s=180, color=color, zorder=4)
    field.text(0, yq, '+' if q > 0 else '−', color='white', ha='center', va='center', zorder=5)
field.set(aspect='equal', xlim=(-2.4, 2.4), ylim=(-2.4, 2.4), xlabel='x', ylabel='y', title='Field lines of the finite dipole')
t = np.linspace(0, np.pi, 401)
orbit.plot(-np.cos(t), -np.sin(t), color='#226d3c', linewidth=2.5)
orbit.plot([-1, 1], [0, 0], ':', color='#888888')
orbit.scatter([-1, 1, 0], [0, 0, -1], color='#226d3c', zorder=3)
for pos, vec in [((-1, 0), (0, -0.45)), ((1, 0), (0, -0.45)), ((0, -1), (0, 0.55))]:
    orbit.annotate('', xy=np.array(pos)+np.array(vec), xytext=pos, arrowprops={'arrowstyle':'->', 'color':'#b53131', 'lw':2})
orbit.annotate('', xy=(0.65, -0.76), xytext=(0.4, -0.91), arrowprops={'arrowstyle':'->', 'color':'#226d3c', 'lw':2})
orbit.annotate('', xy=(0.08, 0.7), xytext=(0.08, 0.25), arrowprops={'arrowstyle':'->', 'color':'#303030', 'lw':2})
orbit.text(0.17, 0.48, r'$\mathbf{p}$')
orbit.text(-1, 0.1, 'Release', ha='center')
orbit.text(1, 0.1, 'Turn back', ha='center')
orbit.text(0, -1.25, r'$r=d$; red arrows show force', ha='center')
orbit.text(0, -1.5, 'Ideal point dipole; release from rest', ha='center', fontsize=11)
orbit.scatter([0], [0], s=28, color='#333333')
orbit.set(aspect='equal', xlim=(-1.5, 1.5), ylim=(-1.7, 1.1), xlabel=r'$x/d$', ylabel=r'$y/d$', title='Particle path, distinct from a field line')
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', transparent=False)
