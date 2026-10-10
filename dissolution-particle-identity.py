"""Original dissolution schematic. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media; writes dissolution-particle-identity.png to the working directory.
Particle positions and sizes are explanatory choices, not experimental data.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import numpy as np

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=120, facecolor='white')
ax.set(xlim=(0, 10), ylim=(0, 6.5), aspect='equal')
ax.axis('off')
blue, orange, green = '#176b9a', '#bf5c18', '#278264'
ax.text(5, 6.22, 'Dissolution changes distribution, not the element inventory',
        ha='center', fontsize=15, weight='bold')
ax.text(2.0, 5.73, 'Before: solute together', ha='center', weight='bold')
ax.text(7.55, 5.73, 'After: dispersed among water', ha='center', weight='bold')

def panel(x, y, w=3.4, h=1.6):
    ax.add_patch(Rectangle((x, y), w, h, facecolor='#fcfdff',
                           edgecolor='#788792', lw=1.5))

def particle(x, y, color, text='', r=.135):
    ax.add_patch(Circle((x, y), r, facecolor=color, edgecolor='white', lw=.7))
    if text:
        ax.text(x, y, text, ha='center', va='center', color='white', fontsize=8.8)

# Both rows conserve exactly the same number of solute symbols.
neutral_before = [(1.68, 4.36), (1.96, 4.36), (1.68, 4.64), (1.96, 4.64)]
neutral_after = [(6.53, 4.43), (7.46, 4.87), (8.54, 4.28), (8.80, 4.92)]
ion_before = [(1.50 + .30 * i, 1.88 + .30 * j, (i+j) % 2)
              for j in range(2) for i in range(4)]
ion_after = [(6.47, 1.85, 0), (6.55, 2.60, 1), (7.20, 2.15, 0),
             (7.55, 2.73, 1), (8.18, 1.82, 1), (8.50, 2.48, 0),
             (9.0, 1.98, 0), (9.05, 2.83, 1)]
assert len(neutral_before) == len(neutral_after) == 4
assert [sum(p[2] == v for p in ion_before) for v in (0,1)] == [4,4]
assert [sum(p[2] == v for p in ion_after) for v in (0,1)] == [4,4]
for y in (3.8, 1.35):
    panel(.35, y)
    panel(5.90, y)
# Water positions are deliberately arranged; avoid overlap with the solute.
for y, particles in ((3.8, neutral_after), (1.35, ion_after)):
    for xx in np.linspace(6.1, 9.1, 10):
        for yy in np.linspace(y+.16, y+1.44, 5):
            if all(np.hypot(xx-p[0], yy-p[1]) > .25 for p in particles):
                particle(xx, yy, '#a9cddd', r=.055)
for x,y in neutral_before+neutral_after:
    particle(x,y,green,r=.13)
for points in (ion_before, ion_after):
    for x,y,kind in points:
        particle(x,y,blue if kind == 0 else orange, 'Na+' if kind == 0 else 'Cl−')
for y in (4.60, 2.15):
    ax.add_patch(FancyArrowPatch((3.95,y), (5.65,y), arrowstyle='-|>',
                                 mutation_scale=20, color='#384e60', lw=1.8))
    ax.text(4.80,y+.25, 'dissolve',ha='center',fontsize=11)
ax.text(2.05, 3.51, '4 neutral molecules', ha='center', color=green)
ax.text(7.60, 3.51, 'The same 4 molecules', ha='center', color=green)
ax.text(2.05, 1.06, 'Ionic crystal: 4 Na+ and 4 Cl−', ha='center',fontsize=11)
ax.text(7.60, 1.06, 'The same 4 Na+ and 4 Cl−', ha='center',fontsize=11)
particle(1.15,.51,'#a9cddd',r=.065)
ax.text(1.36,.51,'water molecule (schematic)',va='center',fontsize=10.5)
ax.text(6.0,.51,'No measured sizes, positions, or hydration geometry',
        va='center',fontsize=9.5)
fig.subplots_adjust(left=.02, right=.98, bottom=.02, top=.98)
fig.savefig(Path('dissolution-particle-identity.png'), facecolor='white', transparent=False)
plt.close(fig)
