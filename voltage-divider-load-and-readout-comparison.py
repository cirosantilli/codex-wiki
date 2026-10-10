"""Original divider circuits; tested with Python 3.14 and matplotlib 3.10.7.

Run from _media; output is an opaque, white PNG in the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(1, 3, figsize=(12, 6.2))
fig.patch.set_facecolor('white')
blue, orange = '#185b8c', '#b95415'


def wire(ax, x1, y1, x2, y2, color=blue):
    ax.plot([x1, x2], [y1, y2], lw=2, color=color)


def resistor(ax, x, lo, hi, text, color=blue, side='left'):
    mid = (lo+hi)/2
    wire(ax, x, lo, x, mid-.3, color)
    wire(ax, x, mid+.3, x, hi, color)
    ax.add_patch(Rectangle((x-.16, mid-.3), .32, .6, facecolor='white', edgecolor=color, lw=2))
    ax.text(x-.27 if side=='left' else x+.27, mid, text,
            ha='right' if side=='left' else 'left', va='center', color=color)


cases = [('No external load', None, '5.000000 V', r'$I_L=0$'),
         ('Strong loading', 10_000, '3.333333… V', r'$I_L=1/3\ \mathrm{mA}$'),
         ('Weak loading', 1_000_000, '4.975124… V', r'$I_L=5/1005\ \mathrm{mA}$')]
for ax, (title, load, readout, current) in zip(axes, cases):
    ax.set_xlim(-.1, 4.25); ax.set_ylim(-1.1, 5.6); ax.axis('off')
    ax.set_title(title, fontweight='bold', pad=12)
    ax.text(1.7, 5.12, 'Input held at +10 V', ha='center', color=blue)
    wire(ax, 1.7, 4.85, 1.7, 4.5)
    resistor(ax, 1.7, 2.5, 4.5, '$R_1$\n10 kΩ')
    resistor(ax, 1.7, .5, 2.5, '$R_2$\n10 kΩ')
    wire(ax, 1.7, .5, 3.05, .5)
    ax.plot(1.7, 2.5, 'o', color=blue, ms=5)
    wire(ax, 1.7, 2.5, 3.05, 2.5)
    ax.text(1.72, 2.69, '$V_{out}$', color=blue, fontsize=12)
    if load:
        label = '$R_L$\n10 kΩ' if load==10_000 else '$R_L$\n1 MΩ'
        resistor(ax, 3.05, .5, 2.5, label, orange, 'right')
    else:
        ax.plot([3.05, 3.05], [.5, 2.5], 'o', mfc='white', mec=blue, ms=6)
        ax.text(3.25, 1.5, 'Open', va='center', color=blue)
    wire(ax, 1.7, .5, 1.7, .22)
    for width, y in [(.55, .22), (.36, .11), (.18, 0)]:
        wire(ax, 1.7-width/2, y, 1.7+width/2, y)
    ax.text(1.7, -.2, 'Reference: 0 V', ha='center', va='top', color=blue)
    ax.text(2.0, -.68, current, ha='center', color=orange if load else blue)
    ax.text(2.0, -1.0, readout, ha='center', va='top', fontsize=16, fontweight='bold',
            bbox={'boxstyle':'round,pad=.4', 'facecolor':'#f2f6f9', 'edgecolor':blue})
fig.suptitle('Attaching a load changes the voltage being read', fontsize=18, y=.97)
fig.text(.5, .035, 'Predictions for fixed, ideal resistors and a 10 V ideal source. Readout adds no further load.\n'
         'Each finite load is in parallel with the lower arm; these are not measured results.',
         ha='center', va='bottom', fontsize=11)
fig.subplots_adjust(left=.04, right=.95, top=.84, bottom=.22, wspace=.27)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=110, facecolor='white')
plt.close(fig)
