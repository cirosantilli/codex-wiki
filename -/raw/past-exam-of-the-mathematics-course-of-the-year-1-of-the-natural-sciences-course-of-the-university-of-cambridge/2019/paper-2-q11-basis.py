"""Original midpoint-vector diagram. Python 3.14; NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import proj3d

fig = plt.figure(figsize=(7.2, 6.0), facecolor='white')
ax = fig.add_subplot(111, projection='3d')
o = np.zeros(3)
a, b, c = np.eye(3)
e, f, g = (b+c)/2, (a+c)/2, (a+b)/2
for endpoint, label in zip((a, b, c), ('x', 'y', 'z')):
    ax.quiver(*o, *(1.25*endpoint), color='#222222', arrow_length_ratio=.075, linewidth=1.3)
    ax.text(*(1.34*endpoint), label, fontsize=13)
for p, q in ((a, b), (b, c), (c, a)):
    line = np.array([p, q])
    ax.plot(*line.T, ':', color='#888888', linewidth=1.0)
ax.add_collection3d(Poly3DCollection([[e, f, g]], facecolor='#e1eff7', edgecolor='#477389', alpha=.55))
for endpoint, label, color in zip((e, f, g), ('e', 'f', 'g'), ('#b84039', '#246caa', '#347b49')):
    ax.quiver(*o, *endpoint, color=color, arrow_length_ratio=.12, linewidth=2.4)
    ax.text(*(endpoint*.72 + np.array([0, 0, .035])), '$\\mathbf{' + label + '}$', color=color, fontsize=14)
ax.set(xlim=(-.15, 1.45), ylim=(-.15, 1.45), zlim=(-.15, 1.45))
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=24, azim=35)
points = [(o, 'O', (-20, 9)), (a, 'A (1,0,0)', (-10, 12)),
          (b, 'B (0,1,0)', (10, 8)), (c, 'C (0,0,1)', (10, 8)),
          (e, 'E', (9, 6)), (f, 'F', (-15, 6)), (g, 'G', (5, -17))]
for point, label, offset in points:
    ax.scatter(*point, s=25, color='#202020', depthshade=False)
    projected = proj3d.proj_transform(*point, ax.get_proj())
    ax.annotate(label, projected[:2], xytext=offset, textcoords='offset points',
                fontsize=10, annotation_clip=False, zorder=20,
                arrowprops=dict(arrowstyle='-', color='#222222', linewidth=.8) if label == 'O' else None,
                bbox=dict(facecolor='white', edgecolor='none', alpha=.9, pad=.8))
ax.set_axis_off()
fig.suptitle('Midpoint vectors and their plane', fontsize=15, y=.94)
fig.subplots_adjust(left=0, right=1, bottom=0, top=.97)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=155, facecolor='white')
plt.close(fig)
