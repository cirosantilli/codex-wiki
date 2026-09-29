"""Original functional cycle; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run from _media. All times and pressure levels are chosen schematic values.
The shaded operating window is stipulated, not derived from thermodynamics.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig = plt.figure(figsize=(11, 6.6), facecolor='white')
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.3], hspace=0.45, wspace=0.30)
ax = fig.add_subplot(gs[0, 0])
ax.set(xlim=(0, 10), ylim=(0, 6))
ax.axis('off')
ax.add_patch(Rectangle((1, 1.3), 5.6, 3.8, facecolor='#e8f4fc', edgecolor='#26536b', lw=2))
ax.text(3.8, 3.2, 'Transparent liquid\ncontrolled temperature', ha='center')
ax.annotate('Beam', xy=(1, 2), xytext=(-0.1, 1.0), arrowprops={'arrowstyle': '->', 'lw': 2}, va='center')
ax.add_patch(Rectangle((3.1, 0.7), 1.4, 0.6, color='#aaa'))
ax.annotate('Piston: pressure control', xy=(3.8, 0.7), xytext=(3.8, -0.1), ha='center', arrowprops={'arrowstyle': '->'})
for y, label in [(4.5, 'View 1'), (2.5, 'View 2')]:
    ax.add_patch(Rectangle((8, y - 0.25), 1.2, 0.5, facecolor='#eee', edgecolor='black'))
    ax.plot([6.6, 8], [3.5, y], color='#777', ls='--')
    ax.text(8.6, y + 0.5, label, ha='center')
ax.text(0.1, 5.6, 'A  Functional arrangement', weight='bold')
ax = fig.add_subplot(gs[0, 1])
ax.axis('off')
ax.text(0, 0.97, 'B  Preparation and readout', weight='bold', va='top')
ax.text(0, 0.70, 'Prepare sensitivity before passage.\nPhotograph after bubble growth.', linespacing=1.6, va='top')
ax.text(0, 0.18, 'Recording can be selected after passage.', color='#26536b', va='top')
ax = fig.add_subplot(gs[1, :])
# A deliberately invented waveform with an equilibrium reference at fixed T.
t = np.array([0, 1.4, 2.1, 7.6, 8.3, 10])
p = np.array([1, 1, 0.35, 0.35, 1, 1])
ax.axvspan(2.1, 7.6, color='#e6f3e7', label='Stipulated sensitive window')
ax.plot(t, p, color='#26536b', lw=2.8, label='Chosen pressure cycle')
ax.axhline(0.7, color='#777', ls='--', lw=1.5)
ax.text(9.9, 0.72, r'$p_{\rm sat}(T)$, fixed $T$', ha='right', va='bottom', color='#555')
ax.axvline(3.1, color='#d27716', lw=3)
ax.text(3.1, 1.12, 'Beam', ha='center', color='#9b5200')
ax.axvline(5.6, color='#824891', lw=2)
ax.text(5.6, 1.12, 'Flash + stereo views', ha='center', color='#824891')
ax.annotate('', xy=(5.6, 0.18), xytext=(3.1, 0.18), arrowprops={'arrowstyle': '<->', 'color': '#555'})
ax.text(4.35, 0.07, 'Bubble growth', ha='center')
ax.text(0.7, 0.80, 'Hold', ha='center')
ax.text(8.6, 0.30, 'Recompress\nand clear', ha='center')
ax.set(xlim=(0, 10), ylim=(0, 1.25), xlabel='Arbitrary time coordinate (no historical delays)', ylabel='Normalized pressure')
ax.set_yticks([0.35, 0.7, 1], ['Low', 'Equilibrium', 'High'])
ax.set_xticks([])
ax.spines[['top', 'right']].set_visible(False)
ax.set_title('C  Prepare → expose → photograph → reset', loc='left', fontsize=12, weight='bold', pad=20)
fig.suptitle('Bubble chamber: pressure cycle synchronized with the beam', fontsize=16, weight='bold', y=0.98)
fig.subplots_adjust(top=0.9, bottom=0.10, left=0.12, right=0.97)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
