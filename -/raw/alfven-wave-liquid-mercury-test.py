"""Draw the functional chain of Lundquist's 1949 mercury test.

Python 3.14 / Matplotlib 3.10.7. Run from _media to emit the matching PNG.
Original functional diagram, not a dimensional reconstruction or historical data.
Apparatus: Sheyko (2014), p.8 fig.1.4; resonance limitation: Tigrine et al.
(2019), GJI 219 S83, section 1, doi:10.1093/gji/ggz112.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(10, 5.8), facecolor='white')
ax.set_xlim(0, 10)
ax.set_ylim(0, 5.8)
ax.axis('off')
BLUE = '#176c9c'
RED = '#b33e38'

def box(x, y, w, h, text, color='#eaf2f6'):
    patch = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
                           facecolor=color, edgecolor='#527385', linewidth=1.4)
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', linespacing=1.5)

# Connections show function, not the layout of undocumented drive/optics hardware.
box(0.30, 0.90, 2.05, 1.10, 'Vary drive\nfrequency')
box(7.40, 3.65, 2.15, 1.15, 'Floating mirror\nand scale\nSurface-motion readout')
ax.add_patch(Rectangle((3.55, 1.05), 2.50, 3.70, edgecolor='#56656d',
                       facecolor='#dbe8ed', linewidth=2))
ax.plot([3.55, 6.05], [4.30, 4.30], color=BLUE, lw=2)
ax.text(4.80, 3.25, 'Mercury\nin a cylinder', ha='center', va='center', linespacing=1.5)
ax.add_patch(Rectangle((3.75, 1.28), 2.10, 0.12, facecolor=RED, edgecolor=RED))
ax.text(4.80, 1.80, 'Bottom disk', ha='center', color=RED)
ax.annotate('', xy=(5.38, 1.10), xytext=(4.20, 1.10),
            arrowprops={'arrowstyle': '<->', 'color': RED, 'lw': 2})
ax.text(4.80, 0.70, 'Oscillating azimuthal motion', ha='center', color=RED, fontsize=10)
ax.annotate('', xy=(3.66, 1.38), xytext=(2.43, 1.45),
            arrowprops={'arrowstyle': '->', 'color': RED, 'lw': 1.8})
ax.annotate('', xy=(7.24, 4.23), xytext=(6.13, 4.23),
            arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 1.8})
ax.annotate('', xy=(6.60, 4.65), xytext=(6.60, 1.15),
            arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 2.5})
ax.text(6.83, 2.90, 'Axial field $B_0$', ha='left', va='center', rotation=90, color=BLUE)
ax.text(4.80, 5.40, "Lundquist's early liquid-metal test (1949)", ha='center', fontsize=16)
ax.text(4.80, 5.02, 'Functional schematic • not to scale', ha='center', color='#555555', fontsize=11)
box(7.15, 1.20, 2.55, 1.50, 'Frequency scan seeks\na standing-wave resonance\n\nNo resolved peak established', color='#fff0e6')
ax.text(5, 0.15, 'Cylinder, disk and surface readout are documented; drive and optical hardware are not reconstructed.',
        ha='center', fontsize=10, color='#444444')
fig.subplots_adjust(left=0.015, right=0.985, top=0.985, bottom=0.02)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
