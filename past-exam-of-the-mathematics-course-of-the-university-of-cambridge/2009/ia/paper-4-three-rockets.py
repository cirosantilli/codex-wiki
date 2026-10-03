"""Draw a representative voyage; output basename PNG to caller CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

u, vp, wpp = .5, .4, .9  # velocities in units of c
v = (u + vp) / (1 + u * vp)
w = (v - wpp) / (1 - v * wpp)
x = [0, 1, 2, 0]
ct = [0, 1 / u, 1 / u + 1 / v, 1 / u + 1 / v - 2 / w]
fig, ax = plt.subplots(figsize=(6.1, 6.0), layout='constrained')
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.plot([0, 0], [0, ct[-1] + .3], color='#59636c', lw=1.5, label='Skaro')
colors = ['#276d9e', '#238b6b', '#bb583e']
for i, color in enumerate(colors):
 ax.plot(x[i:i+2], ct[i:i+2], lw=2.4, color=color)
 midx = (x[i] + x[i+1]) / 2
 midy = (ct[i] + ct[i+1]) / 2
 ax.annotate('', xy=(midx + .12 * (x[i+1] - x[i]), midy + .12 * (ct[i+1] - ct[i])), xytext=(midx, midy), arrowprops={'arrowstyle': '->', 'color':color, 'lw':2})
labels = ['O: first rocket', 'A: second rocket', 'B: third rocket', 'C: return']
offsets = [(10, -5), (12, -12), (12, 0), (12, 0)]
for xx, yy, label, offset in zip(x, ct, labels, offsets):
 ax.plot(xx, yy, 'o', ms=5, color='#222222')
 ax.annotate(label, (xx, yy), xytext=offset, textcoords='offset points', fontsize=10)
ax.text(.32, .9, 'u', color=colors[0], fontsize=12)
ax.text(1.43, 2.45, 'v', color=colors[1], fontsize=12)
ax.text(.9, 5.9, 'w < 0', color=colors[2], fontsize=12)
ax.set(xlabel='x / L', ylabel='ct / L', xlim=(-.4, 3.2), ylim=(-.3, ct[-1] + .7), title="Three rocket legs in Skaro's inertial frame")
ax.set_xticks([0, 1, 2])
ax.grid(alpha=.18)
ax.text(.98, .02, "Example: u = 0.5c, v = 0.75c, w = -0.462c", transform=ax.transAxes, ha='right', fontsize=9)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', transparent=False)
plt.close(fig)
