"""Functional probe comparison; Python 3.14, matplotlib 3.10.7. Run in _media."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.8), dpi=110)
fig.patch.set_facecolor('white')
blue, orange = '#176a9a', '#b74e15'
for ax in axes:
    ax.set(xlim=(0, 10), ylim=(0, 10))
    ax.axis('off')
left, right = axes
left.set_title('Transport: is there a conducting path?', weight='bold', pad=16)
left.add_patch(Rectangle((1.2, 4.2), 7.6, 1.8, facecolor='#eeeeee', edgecolor='#555555'))
left.text(5, 4.95, 'Ceramic specimen', ha='center')
xs = [1.7, 3.6, 6.4, 8.3]
for x in xs:
    left.add_patch(Circle((x, 5.9), .12, color=orange))
left.plot([1.7, 1.7, .4, .4, 9.6, 9.6, 8.3, 8.3], [5.9, 3.5, 3.5, 2.3, 2.3, 3.5, 3.5, 5.9], color=blue, lw=2)
left.add_patch(Rectangle((3.7, 1.9), 2.6, .8, fc='white', ec=blue, zorder=3))
left.text(5, 2.3, 'Drive current I', ha='center', va='center')
left.annotate('', xy=(.4, 2.65), xytext=(.4, 3.25), arrowprops={'arrowstyle': '->', 'color': blue, 'lw': 2})
left.plot([3.6, 3.6, 4.1], [5.9, 7.3, 7.3], color=orange, lw=2)
left.plot([6.4, 6.4, 5.9], [5.9, 7.3, 7.3], color=orange, lw=2)
left.add_patch(Rectangle((4.1, 6.8), 1.8, 1, fc='white', ec=orange))
left.text(5, 7.3, 'Vₐᵦ', va='center', ha='center', fontsize=14)
left.text(5, 8.4, 'High impedance sense meter', ha='center')
left.text(3.6, 6.2, 'a', ha='center', color=orange)
left.text(6.4, 6.2, 'b', ha='center', color=orange)
left.text(5, .75, 'Repeat with ±I; check heating and offsets.\nA small Vₐᵦ can reflect a narrow connected path.', ha='center', va='center', linespacing=1.6, fontsize=10)
right.set_title('Magnetism: how does the sample respond?', weight='bold', pad=16)
right.add_patch(Rectangle((2.2, 4.5), 2.4, 2.0, fc='#eeeeee', ec='#555555'))
right.text(3.4, 5.5, 'Sample', ha='center')
for y in [4.2, 6.8]:
    right.add_patch(FancyArrowPatch((1.0, y), (5.8, y), arrowstyle='->', mutation_scale=14, color=blue, lw=2))
right.text(3.4, 7.4, 'Controlled applied field H', ha='center', color=blue)
right.annotate('', xy=(6.1, 5.5), xytext=(4.7, 5.5), arrowprops={'arrowstyle': '->', 'color': orange, 'lw': 2})
right.add_patch(Rectangle((6.2, 4.65), 3.4, 1.7, fc='white', ec=orange))
right.text(7.9, 5.5, 'Calibrated\nmagnetometer', va='center', ha='center')
right.text(5, 3.25, 'Compare magnetic histories', ha='center', weight='bold')
right.text(5, 2.5, 'Cool without H → apply H: shielding\nCool with H present: test expulsion', va='center', ha='center', linespacing=1.7, fontsize=10)
right.text(5, .75, 'Subtract background; specify geometry.\nTransport zero does not imply full expulsion.', ha='center', va='center', linespacing=1.6, fontsize=10)
fig.suptitle('Two independent questions about superconductivity', fontsize=16, weight='bold', y=.98)
fig.text(.5, .02, 'Original functional schematic; no historical dimensions, readings or instrument layout.', ha='center', color='#555555', fontsize=10)
fig.subplots_adjust(left=.025, right=.975, bottom=.08, top=.85, wspace=.15)
fig.savefig(Path(__file__).stem + '.png', facecolor='white', dpi=110)
