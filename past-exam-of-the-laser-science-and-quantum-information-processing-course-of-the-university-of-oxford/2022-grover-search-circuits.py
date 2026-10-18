"""Original Grover-search networks; tested with Python 3.14 / matplotlib 3.10.7.

The sole figure output is the script basename in the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc

INK = '#17324d'
BLUE = '#e8f2fc'
ORANGE = '#fff0db'
fig, ax = plt.subplots(figsize=(9.6, 6.2), dpi=100)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.set_xlim(0, 12)
ax.set_ylim(-.2, 8.5)
ax.axis('off')

def text(x, y, s, size=13, **kw):
    ax.text(x, y, s, fontsize=size, color=INK, ha=kw.pop('ha', 'center'), va='center', **kw)

def wire(y, label, end=11.2):
    ax.plot([1.15, end], [y, y], color=INK, lw=1.4, zorder=1)
    text(.65, y, label, 15)

def gate(x, ys, label, face=BLUE, width=.8):
    low, high = min(ys)-.3, max(ys)+.3
    ax.add_patch(Rectangle((x-width/2, low), width, high-low,
                           facecolor=face, edgecolor=INK, lw=1.4, zorder=3))
    text(x, (low+high)/2, label, 16, zorder=4)

def measure(x, y):
    gate(x, [y], '', face='white', width=.7)
    ax.add_patch(Arc((x, y-.06), .44, .35, theta1=0, theta2=180,
                     color=INK, lw=1.2, zorder=4))
    ax.plot([x, x+.15], [y-.05, y+.16], color=INK, lw=1.2, zorder=4)

text(6, 8.15, 'One Grover iteration: one marked input among four', 18, weight='bold')
text(1.15, 7.5, 'Three-qubit oracle', 14, ha='left', weight='bold')
for y, ket in [(6.9, r'$|0\rangle$'), (6.0, r'$|0\rangle$'), (5.1, r'$|1\rangle$')]:
    wire(y, ket)
    gate(2, [y], '$H$')
gate(4, [5.1, 6, 6.9], r'$U_f$', ORANGE, 1.1)
gate(7.1, [6, 6.9], '$D$', BLUE, 1.1)
for y in [6, 6.9]:
    measure(9.5, y)
text(11.2, 6.45, r'$x_*$', 16)
text(9.5, 5.1, r'$|-\rangle$ unchanged', 12, bbox={'facecolor':'white', 'edgecolor':'none'})
text(4, 4.48, r'$U_f|x,y\rangle=|x,y\oplus f(x)\rangle$', 13)

text(1.15, 3.75, 'Two-qubit phase oracle', 14, ha='left', weight='bold')
for y in [3.15, 2.25]:
    wire(y, r'$|0\rangle$')
    gate(2, [y], '$H$')
gate(4, [2.25, 3.15], '$O_f$', ORANGE, 1.1)
gate(7.1, [2.25, 3.15], '$D$', BLUE, 1.1)
for y in [2.25, 3.15]:
    measure(9.5, y)
text(11.2, 2.7, r'$x_*$', 16)
text(4, 1.62, r'$O_f|x\rangle=(-1)^{f(x)}|x\rangle$', 13)
text(7.25, .78, r'$D=2|s\rangle\langle s|-I,\quad |s\rangle=\frac{1}{2}\sum_x|x\rangle$', 15)
text(6, .08, r'For marked input $11$: $O_f=\mathrm{CZ}$ and the output is $|11\rangle$ with certainty.', 12)
fig.subplots_adjust(left=.015, right=.985, bottom=.025, top=.985)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,
            facecolor='white', transparent=False, metadata={'Software':'codex-wiki figure generator'})
plt.close(fig)
