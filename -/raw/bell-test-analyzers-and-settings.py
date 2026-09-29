"""Draw a conceptual two-setting Bell apparatus. Python 3.14; matplotlib 3.10.7."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=120, facecolor='white')
ax.set(xlim=(0, 10), ylim=(0, 5.5))
ax.axis('off')
blue, red, ink = '#2466a5', '#b34f32', '#243444'

def box(x, y, w, h, text, color=ink, fill='#f5f7fa'):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.09',
                              linewidth=1.4, edgecolor=color, facecolor=fill))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', color=color)

def arrow(start, end, color=ink, dashed=False):
    ax.annotate('', xy=end, xytext=start, arrowprops={
        'arrowstyle': '->', 'lw': 1.7, 'color': color,
        'linestyle': '--' if dashed else '-'})

ax.text(5, 5.23, 'A pair, two independent basis choices, four joint outcomes',
        ha='center', fontsize=15, weight='bold', color=ink)
ax.text(5, 4.83, 'Conceptual ideal model • angles are physical polarizer angles',
        ha='center', fontsize=11, color=ink)
box(4.22, 3.55, 1.56, .68, 'Entangled\npair source')
box(.6, 3.48, 2.15, .82, 'Alice: choose one\n'+r'$a_0=0^\circ$  or  $a_1=45^\circ$', blue)
box(7.25, 3.48, 2.15, .82, 'Bob: choose one\n'+r'$b_0=22.5^\circ$  or  $b_1=-22.5^\circ$', red)
arrow((4.12, 3.9), (2.86, 3.9), blue)
arrow((5.88, 3.9), (7.14, 3.9), red)
ax.text(3.48, 4.05, 'photon', ha='center', color=blue)
ax.text(6.52, 4.05, 'photon', ha='center', color=red)
for x, c in [(1.68, blue), (8.32, red)]:
    for end in [x-.58, x+.58]:
        arrow((x, 3.38), (end, 2.8), c)
    box(x-1.03, 2.21, .85, .44, '+1', c)
    box(x+.18, 2.21, .85, .44, '−1', c)
    ax.text(x, 1.96, 'two analyzer outputs', ha='center', color=c, fontsize=10)
    arrow((x, 1.72), (3.72 if x<5 else 6.28, 1.33), c)
box(3.8, .91, 2.4, .72, 'Record setting + outcome\nMatch trial / timing labels')
ax.text(5, .48, r'Joint record: $n_{++},\ n_{+-},\ n_{-+},\ n_{--}$',
        ha='center', fontsize=12, color=ink)
ax.text(5, .08, 'Missed detections need an explicit trial rule; a coincidence alone does not close a loophole.',
        ha='center', fontsize=10, color=ink)
fig.subplots_adjust(left=.02, right=.98, top=.98, bottom=.03)
fig.savefig(Path(__file__).stem+'.png', facecolor='white', transparent=False)
plt.close(fig)
