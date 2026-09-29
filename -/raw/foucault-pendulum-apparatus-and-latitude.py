"""Original functional schematic and latitude prediction; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; emits this script's basename.png into the current directory.
Sighting method motivated by UNSW's undriven teaching pendulum; no historical dimensions.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, Rectangle

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig = plt.figure(figsize=(11.2, 7.0), layout='constrained')
gs = fig.add_gridspec(2, 2, width_ratios=(1.05, 1))
a = fig.add_subplot(gs[:, 0])
a.set(xlim=(-2.8, 2.8), ylim=(-.7, 6.5), aspect='equal')
a.axis('off')
a.set_title('A. Functional apparatus (schematic)', loc='left', weight='bold')
a.add_patch(Rectangle((-1.6, 5.4), 3.2, .22, color='#454f5b'))
a.plot([0, 0], [5.4, 1], '--', color='.65', lw=1)
a.plot([0, -1.05], [5.4, 1.4], color='#263849', lw=2)
a.add_patch(Circle((-1.05, 1.4), .23, color='#235b91'))
a.scatter([0], [5.4], s=45, color='#a94726', zorder=5)
a.annotate('Rigid support; pivot must allow\nboth horizontal swing directions', (0, 5.4), (0, 6.05), ha='center', arrowprops={'arrowstyle': '->'})
a.text(.3, 3.7, 'Light flexible wire\nlength ℓ', va='center')
a.text(-1.05, .95, 'Compact bob', ha='center')
a.annotate('Gentle release\nwithout sideways push', (-1.2, 1.6), (-2.55, 2.7), arrowprops={'arrowstyle': '->'}, fontsize=10)
a.plot([-2.5, 2.5], [.3, .3], color='.4')
a.text(0, -.15, 'Stationary floor reference', ha='center')
# Top-view readout inset drawn in the otherwise empty lower-right region.
b = fig.add_subplot(gs[0, 1])
b.set_title('B. Readout from above', loc='left', weight='bold')
b.set(xlim=(-1.4, 1.4), ylim=(-1.3, 1.4), aspect='equal')
b.axis('off')
b.add_patch(Circle((0, 0), 1, fill=False, edgecolor='.75'))
b.plot([0, 0], [-1, 1], '--', color='.35', label='Fixed N–S sighting plane')
angle = np.deg2rad(18)
b.plot([-np.sin(angle), np.sin(angle)], [-np.cos(angle), np.cos(angle)], color='#a94726', lw=3, label='Later swing direction')
b.scatter([0], [0], s=20, color='black')
b.text(0, 1.1, 'N: fixed wire + wall line', ha='center', fontsize=10)
b.annotate('', (1.1, 0), (0, 0), arrowprops={'arrowstyle': '->'})
b.text(1.15, 0, 'E', va='center')
b.add_patch(Arc((0, 0), 1.05, 1.05, theta1=72, theta2=90, color='#a94726', lw=2))
b.text(.35, .7, 'Δψ', color='#a94726')
b.text(0, -1.2, 'Clockwise example in northern hemisphere', ha='center', fontsize=10)
c = fig.add_subplot(gs[1, 1])
phi = np.linspace(-90, 90, 361)
omega = 7.292115e-5
rate = -omega * np.sin(np.deg2rad(phi)) * 3600 * 180 / np.pi
c.plot(phi, rate, color='#235b91', lw=2)
c.axhline(0, color='.6', lw=.8)
c.axvline(0, color='.6', lw=.8)
c.set(title='C. Latitude sets the slow rate', xlabel='Latitude φ (degrees; north positive)', ylabel='dψ/dt (degrees/hour)', xticks=[-90, -45, 0, 45, 90], yticks=[-15, 0, 15])
c.text(-82, 4, 'Anticlockwise', fontsize=10, color='#235b91')
c.text(13, -5, 'Clockwise', fontsize=10, color='#235b91')
c.grid(alpha=.2)
fig.suptitle('Foucault pendulum: observe a direction against the building', fontsize=15, weight='bold')
fig.savefig(Path(__file__).stem + '.png', dpi=100, facecolor='white')
