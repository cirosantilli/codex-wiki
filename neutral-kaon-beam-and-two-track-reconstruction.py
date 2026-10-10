"""Original functional kaon schematic; Python 3.14, matplotlib 3.10, NumPy 2.3.

Run from _media. Apparatus functions: Christenson et al., PRL 13 (1964),
p.138; Fitch's 1980 Nobel lecture, pp.598-600. Geometry is not to scale.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig = plt.figure(figsize=(11, 7.5), dpi=100, facecolor='white')
ax = fig.add_axes((.035, .40, .93, .51))
ax.set(xlim=(0, 12), ylim=(-3.0, 3.0)); ax.axis('off')
fig.suptitle('Neutral kaon decay: beam preparation and event reconstruction', y=.975, fontsize=17)
fig.text(.5, .925, 'Functional schematic • geometry and trajectories are illustrative', ha='center', color='#555555')

def arrow(a, b, color='#314b61', style='-|>', lw=1.8):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=12, color=color, lw=lw))

def box(x, y, w, h, label, color='#edf3f7', size=10):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.06', facecolor=color, edgecolor='#607486'))
    ax.text(x+w/2, y+h/2, label, ha='center', va='center', fontsize=size)

box(.05, -.42, 1.25, .84, 'Target\nBe + protons')
arrow((1.35, 0), (1.95, 0))
box(2.0, -.42, 1.35, .84, 'Neutral beam\ncollimation')
arrow((3.4, 0), (4.05, 0))
box(4.1, -.75, 2.1, 1.5, '', '#eff7ed', 11)
ax.text(4.25, .50, 'Helium decay', ha='left', va='center', fontsize=11)
ax.text(4.25, .16, 'volume', ha='left', va='center', fontsize=11)
ax.plot(5.65, 0, 'o', color='#253b4d', ms=5)
ax.text(4.25, -1.2, 'Decay vertex', fontsize=10)
ax.plot([5.05, 5.62], [-.98, -.06], color='#607486', lw=.8)
for sign, color, particle in [(1, '#b84433', r'$\pi^+$'), (-1, '#2268a1', r'$\pi^-$')]:
    points = np.array([[5.65, 0], [7.05, sign*.9], [8.3, sign*1.65], [9.05, sign*1.84], [10.2, sign*2.03]])
    ax.plot(points[:, 0], points[:, 1], color=color, lw=2.4)
    ax.text(6.55, sign*.95, particle, color=color, fontsize=14)
    for x, y in [(7.05, sign*.9), (9.05, sign*1.84)]:
        ax.add_patch(Rectangle((x-.06, y-.35), .12, .7, facecolor='#a7c0cf', edgecolor='#607486'))
    box(7.7, sign*1.6-.32, .82, .64, 'Magnet', '#f7e7ce', 9)
    box(10.25, sign*2.02-.38, 1.6, .76, 'Counters', '#e7eef8', 10)
ax.text(7.0, 2.65, 'Two spectrometer arms', ha='center', fontsize=12, fontweight='bold')
ax.text(7.0, 2.20, 'Spark chambers before / after each magnet', fontsize=9, ha='center')
ax.text(10.8, 0, 'Coincident\ntrigger', ha='center', va='center', fontsize=10)
ax.text(.1, -2.35, 'Calibration / control: insert a tungsten regenerator in the beam', color='#526340', fontsize=11)
ax.text(.1, -2.85, 'Free-decay run: avoid mistaking material regeneration for a long-lived decay', color='#555555', fontsize=10)

left = fig.add_axes((.065, .075, .33, .27))
left.set(xlim=(-2.2, 2.2), ylim=(-.35, 3.65), aspect='equal'); left.axis('off')
left.text(0, 3.5, 'Synthetic momenta before deflection', ha='center', fontsize=11)
for dx, c, label in [(np.sqrt(3), '#b84433', r'$\mathbf{p}_+$'), (-np.sqrt(3), '#2268a1', r'$\mathbf{p}_-$')]:
    left.annotate('', (dx, 3), (0, 0), arrowprops={'arrowstyle':'->', 'color':c, 'lw':2})
    left.text(dx*.75, 2.0, label, color=c, fontsize=14)
left.plot([0, 0], [0, 3.1], '--', color='#555555', lw=1)
left.text(.09, .9, r'$\alpha=60^\circ$', fontsize=12)
left.text(0, -.25, r'Beam along $+z$; transverse momenta cancel', ha='center', fontsize=10)
fig.text(.43, .305, 'Two independent tests', fontsize=13, fontweight='bold')
fig.text(.43, .255, r'$m_\pi=1,\quad \mathbf{p}_\pm=(\pm\sqrt{3},0,3),\quad E_\pm=\sqrt{13}$', fontsize=14)
fig.text(.43, .200, r'$M_{\pi\pi}^2=(2\sqrt{13})^2-6^2=16\quad\Rightarrow\quad M_{\pi\pi}=4$', fontsize=14)
fig.text(.43, .145, r'$\mathbf{P}=(0,0,6)\quad\Rightarrow\quad\theta=0$', fontsize=14)
fig.text(.43, .09, 'Correct mass + parent pointing along the beam', fontsize=11)
fig.savefig(Path(__file__).stem+'.png', facecolor='white', dpi=100)
plt.close(fig)
