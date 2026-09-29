"""Original functional comparison, not an instrument reconstruction.

Tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Run from the desired output directory; emits this script's basename.png.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, axs = plt.subplots(2, 1, figsize=(10.8, 7.5))
colors = ['#1976aa', '#b34e11', '#6c4994']
ax = axs[0]
ax.set(xlim=(0, 10), ylim=(-0.05, 3.5))
ax.set_title('A. Early Aston instrument: successive opposite deflections', loc='left', weight='bold', pad=15)
ax.text(.1, 2.88, 'Positive ions from\nlow-pressure discharge', va='top')
ax.annotate('', (1.35, 1.55), (.2, 1.55), arrowprops={'arrowstyle': '->', 'color': '#333333'})
for x in (1.4, 1.75):
    ax.plot([x, x], [1.0, 1.48], color='black', lw=3)
    ax.plot([x, x], [1.62, 2.1], color='black', lw=3)
ax.text(1.57, .62, 'Two slits', ha='center')
ax.add_patch(Rectangle((2.1, 1.13), 1.7, 1.0, fc='#fff6da', ec='none'))
for y in (1.13, 2.13):
    ax.plot([2.1, 3.8], [y, y], color='#a87800', lw=3)
ax.text(2.9, 2.4, 'Electric plates', ha='center')
ax.text(2.9, .66, 'E only: spread', ha='center', color='#8d6600')
ax.add_patch(Rectangle((4.75, .85), 1.25, 1.6, fc='#e5f1f7', ec='#b2cad6'))
ax.text(5.4, 2.75, 'Magnet', ha='center')
ax.text(5.4, .48, 'B only: opposite bend', ha='center', color='#195478')
# Thin-kick illustration. Lever arms: 8.65-2.95=5.70, 8.65-5.40=3.25.
x = np.linspace(1.75, 8.65, 600)
for t, color in zip((.94, 1, 1.06), colors):
    y = 1.55 + (.7 / 5.7) / t**2 * np.maximum(x-2.95, 0) - (1.4/3.25) / t * np.maximum(x-5.4, 0)
    ax.plot(x, y, color=color, lw=1.8)
# Diaphragm only accepts a small fan of rays.
for y1, y2 in ((.96, 1.67), (1.83, 2.36)):
    ax.plot([4.25, 4.25], [y1, y2], color='black', lw=2.3)
ax.text(4.2, 3.02, 'Diaphragm', ha='center')
ax.annotate('', (4.25, 1.89), (4.25, 2.81), arrowprops={'arrowstyle':'-', 'color':'#555555'})
ax.plot([8.65, 8.65], [.54, 1.34], color='black', lw=5)
ax.text(8.65, 1.73, 'Photographic\nreadout', ha='center')
ax.text(7.0, 2.73, 'Same m/q, nearby speeds\nconverge near the readout', ha='center', color='#333333')
ax.text(.1, .08, 'Functional sequence only; paths use a local approximation. Dimensions and plate orientation are omitted.', fontsize=9)
ax.axis('off')
ax = axs[1]
ax.set(xlim=(0, 10), ylim=(-.2, 4.1))
ax.set_title('B. Chosen teaching model: velocity selection, then a semicircle', loc='left', weight='bold', pad=15)
ax.add_patch(Rectangle((1.5, .45), 2.5, 1.1, fc='#eaf5e6', ec='#a4c897'))
ax.text(2.75, 1.92, 'Overlapping Eₛ and Bₛ', ha='center')
ax.text(2.75, .32, 'Pass v₀ = Eₛ / Bₛ', ha='center', color='#326128')
ax.annotate('', (5.5, 1.0), (.2, 1.0), arrowprops={'arrowstyle':'->','lw':1.8,'color':colors[0]})
ax.text(.2, 1.23, 'q > 0')
ax.add_patch(Rectangle((5.5, .68), 2.55, 2.95, fc='#e5f1f7', ec='none'))
ax.text(8.42, 2.84, 'Bₐ into page\nE = 0\n\nSeparate analyzer', ha='center')
theta=np.linspace(0, np.pi, 200)
r=1.14
ax.plot(5.5+r*np.sin(theta), 1+r-r*np.cos(theta), color=colors[0], lw=2)
ax.annotate('', (6.64, 2.25), (6.64, 2.01), arrowprops={'arrowstyle':'->','color':colors[0]})
ax.plot([5.5, 5.5], [2.95, 3.59], color='black', lw=4)
ax.text(4.95, 3.77, 'Detector', ha='center')
ax.annotate('', (5.15, 3.28), (5.15, 1), arrowprops={'arrowstyle':'<->','color':'#444444'})
ax.text(4.94, 2.14, 'D = 2r', rotation=90, ha='center', va='center')
ax.plot([5.5, 6.64], [2.14, 2.14], color='#666666', ls='--')
ax.text(6.04, 2.32, 'r', ha='center')
ax.text(.15, 3.5, 'Straight-through selector:\nq(Eₛ − vBₛ) = 0\n\nCurvature gives m/q = Bₐr/v₀', va='top')
ax.text(.1, -.1, 'Original ideal geometry; this is not Aston’s layout. Selected speed and fixed accelerating voltage are different conditions.', fontsize=9)
ax.axis('off')
fig.subplots_adjust(left=.025, right=.985, top=.93, bottom=.04, hspace=.32)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120, facecolor='white')
plt.close(fig)
