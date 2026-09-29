"""Original functional detector schematic; Python 3.14, matplotlib 3.10.7.

Run from _media; output is deliberately not a scale reconstruction or data plot.
Apparatus: Fukuda et al. PRL 81 (1998); Ahmad et al. PRL 87 (2001), 89 (2002).
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
import numpy as np

BLUE = '#176c9c'
ORANGE = '#bd5426'
GREEN = '#247b55'
plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(1, 2, figsize=(12, 7), dpi=110, facecolor='white')
fig.subplots_adjust(left=.025, right=.975, bottom=.06, top=.88, wspace=.09)
fig.suptitle('Water Cherenkov readout: geometry determines the observable', fontsize=17, y=.97)
fig.text(.5, .92, 'Functional diagrams only • no scale or measured light intensities', ha='center', color='#555555')
for ax in axes:
    ax.set(xlim=(0, 10), ylim=(0, 10), aspect='equal')
    ax.axis('off')

def arrow(ax, start, end, color=BLUE, style='->', lw=1.8):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=13, color=color, lw=lw))

ax = axes[0]
ax.text(5, 9.7, 'Super-Kamiokande: track direction and ring type', ha='center', weight='bold', fontsize=12)
ax.add_patch(Rectangle((1.4, 4.4), 7.2, 4.65, facecolor='#eaf6fb', edgecolor='#59626c', lw=2))
ax.add_patch(Rectangle((1.85, 4.85), 6.3, 3.75, fill=False, edgecolor=BLUE, lw=1.3))
for x in np.linspace(2.05, 7.95, 13):
    ax.plot([x, x], [4.85, 8.6], 'o', ms=3, color=BLUE)
for y in np.linspace(5.1, 8.35, 8):
    ax.plot([1.85, 8.15], [y, y], 'o', ms=3, color=BLUE)
ax.text(5, 8.92, 'Outer veto / exiting-track readout', ha='center', fontsize=10)
ax.text(5, 5.12, 'Ordinary water • inner light sensors', ha='center', fontsize=10)
arrow(ax, (.1, 7), (3.7, 7), '#333333')
ax.text(.1, 7.24, r'$\nu$', fontsize=16)
ax.plot(3.7, 7, 'o', color='#333333', ms=5)
arrow(ax, (3.7, 7), (6.45, 7), ORANGE, lw=3)
ax.text(4.6, 7.25, 'charged lepton', color=ORANGE, fontsize=10)
for start in [(3.9, 7), (4.6, 7), (5.3, 7)]:
    arrow(ax, start, (start[0]+1.7, 8.6), BLUE, lw=.9)
    arrow(ax, start, (start[0]+1.7, 4.85), BLUE, lw=.9)
ax.text(5, 4.0, 'Pulse times + charges → vertex, direction, ring', ha='center', fontsize=11)
for center, width, label in [(2.8, .065, 'Muon: sharper edge'), (7.3, .28, 'Electron shower: blurred edge')]:
    for dr in np.linspace(-width, width, 11):
        ax.add_patch(Circle((center, 2.55), .68+dr, fill=False, color=BLUE, alpha=.12, lw=1.5))
    ax.text(center, 1.3, label, ha='center', fontsize=10)
ax.text(5, .35, 'Classifies charged products; the neutrino leaves no ring.', ha='center', fontsize=10)

ax = axes[1]
ax.text(5, 9.7, 'SNO: distinct reactions in nested spherical volumes', ha='center', weight='bold', fontsize=12)
center=(5, 6.9)
for radius, fill, edge in [(2.15, '#eaf6fb', '#59626c'), (1.7, 'none', BLUE), (1.12, '#cdebf1', GREEN)]:
    ax.add_patch(Circle(center, radius, facecolor=fill, edgecolor=edge, lw=1.7))
for phi in np.linspace(0, 2*np.pi, 28, endpoint=False):
    ax.plot(5+1.7*np.cos(phi), 6.9+1.7*np.sin(phi), 'o', color=BLUE, ms=3)
ax.text(5, 7.1, r'$\mathrm{D_2O}$', ha='center', fontsize=17, color=GREEN)
ax.text(5, 6.65, 'acrylic vessel', ha='center', fontsize=9)
ax.text(7.4, 8.7, 'Light-water shield', ha='center', fontsize=10)
ax.text(7.8, 5.1, 'Sensor shell', ha='center', fontsize=10)
arrow(ax, (7.4, 5.4), (6.25, 5.75), '#555555', lw=1)
arrow(ax, (.7, 7), (3.95, 7), '#333333')
ax.text(.65, 7.25, r'$\nu$', fontsize=16)
ax.text(5, 4.35, 'Pure-heavy-water phase: all channels end in light', ha='center', weight='bold', fontsize=10)
for y, channel, chain, color in [(3.5, 'CC', r'$\nu_e+d\ \to\ e^-+p+p$', ORANGE),
                                 (2.5, 'ES', r'$\nu_\alpha+e^-\ \to\ \nu_\alpha+e^-$', BLUE),
                                 (1.5, 'NC', r'$\nu_\alpha+d\ \to\ \nu_\alpha+p+n$', GREEN)]:
    ax.text(.6, y, channel, color=color, weight='bold', fontsize=12)
    ax.text(1.55, y, chain, fontsize=12)
ax.text(1.55, .8, r'$n+d\ \to\ {}^3\!\mathrm{H}+\gamma\ \to$ secondary electrons', fontsize=11, color=GREEN)
ax.text(5, .1, r'$\alpha=e,\mu,\tau$; NC does not identify which flavour arrived.', ha='center', fontsize=10)
fig.savefig(Path(__file__).stem+'.png', facecolor='white')
plt.close(fig)
