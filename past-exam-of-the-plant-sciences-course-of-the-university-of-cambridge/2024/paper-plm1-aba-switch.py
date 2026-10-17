"""Original qualitative ABA switch; Python 3.14, matplotlib and numpy.

Write the PNG basename into the current working directory for Makefile rendering.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(figsize=(9.0, 5.6), layout='constrained')
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 10), ylim=(0, 6.2))
ax.axis('off')

def box(x, y, text, width=2.25, height=0.7, color='#e9f3f1'):
    ax.add_patch(FancyBboxPatch((x-width/2, y-height/2), width, height,
        boxstyle='round,pad=0.06', facecolor=color, edgecolor='#34555e', lw=1.3))
    ax.text(x, y, text, ha='center', va='center', fontsize=11)

def edge(start, end, inhibit=False):
    if inhibit:
        a, b = np.array(start), np.array(end)
        ax.plot([a[0], b[0]], [a[1], b[1]], color='#9a3544', lw=1.8)
        v = b-a
        perp = np.array([-v[1], v[0]]) / np.linalg.norm(v) * 0.13
        ax.plot([b[0]-perp[0], b[0]+perp[0]], [b[1]-perp[1], b[1]+perp[1]], color='#9a3544', lw=2)
    else:
        ax.annotate('', xy=end, xytext=start,
                    arrowprops={'arrowstyle':'-|>', 'color':'#256b70', 'lw':1.8})

ax.text(5, 6.0, 'ABA-dependent release of a kinase brake', ha='center', fontsize=15, weight='bold')
box(1.5, 4.9, 'ABA-bound\nPYR/PYL receptor')
box(5, 4.9, 'Clade-A PP2C\n(e.g. ABI1)', color='#f8ebec')
box(8.5, 4.9, 'OST1 / SnRK2.6\nkinase')
edge((2.75,4.9),(3.7,4.9), True)
edge((6.25,4.9),(7.2,4.9), True)
box(1.5, 3.2, 'Calcium signal')
box(5, 3.2, 'Calcium-dependent\nprotein kinases')
box(8.5, 3.2, 'SLAC1 activation\nby phosphorylation')
edge((2.75,3.2),(3.7,3.2))
edge((6.25,3.2),(7.2,3.2))
edge((8.5,4.5),(8.5,3.65))
ax.text(5.3,2.4,'Convergent inputs; calcium elevation is not obligatory in every response', ha='center', fontsize=9.5)
box(8.5, 1.6, 'Anion efflux')
box(5, 1.6, 'Depolarization\nand K+ efflux')
box(1.5, 1.6, 'Water loss, lower\nturgor, closure')
edge((8.5,2.8),(8.5,2.05))
edge((7.25,1.6),(6.3,1.6))
edge((3.75,1.6),(2.8,1.6))
ax.text(5,0.5,'Arrows: promotion or downstream consequence    Blunt ends: inhibition\nQualitative schematic; feedback and additional transport targets omitted', ha='center', fontsize=10, color='#43515a')
fig.savefig('paper-plm1-aba-switch.png', dpi=160, facecolor='white')
plt.close(fig)
