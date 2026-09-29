"""Original membrane transport and voltage-recording schematic; Python 3.14.

Run from _media with matplotlib 3.10.7. Outputs this script's basename.png.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Ellipse, Polygon

BLUE = '#176b91'
ORANGE = '#b35c12'
INK = '#213344'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12, 'text.color': INK})
fig, axes = plt.subplots(1, 2, figsize=(12, 6), dpi=120, facecolor='white')
fig.subplots_adjust(left=.025, right=.98, top=.86, bottom=.10, wspace=.10)
fig.suptitle('Membrane potential: transport tendencies and recording sign', fontsize=18, y=.96)
for ax in axes:
    ax.set(xlim=(0, 10), ylim=(0, 8))
    ax.axis('off')

a = axes[0]
a.set_title('A  Selective potassium pathway', fontsize=15, pad=14)
a.add_patch(Rectangle((.2, 1.5), 4.4, 5.9, facecolor='#f0f7fa', edgecolor='none'))
a.add_patch(Rectangle((5.4, 1.5), 4.4, 5.9, facecolor='#faf6ed', edgecolor='none'))
a.add_patch(Rectangle((4.6, 1.5), .8, 5.9, facecolor='#ead4dd', edgecolor='#87546c'))
a.text(2.35, 7.05, 'Inside\nhigher [K⁺]', ha='center', va='top', fontsize=14)
a.text(7.7, 7.05, 'Outside\nlower [K⁺]', ha='center', va='top', fontsize=14)
for y in (2.7, 5.6):
    a.text(4.33, y, '−', color=BLUE, ha='center', va='center', fontsize=21)
    a.text(5.68, y, '+', color=ORANGE, ha='center', va='center', fontsize=20)
a.add_patch(Rectangle((4.45, 3.0), 1.1, 2.0, facecolor='white', edgecolor='#87546c', lw=2))
a.annotate('', (7.9, 4.6), (2.0, 4.6), arrowprops={'arrowstyle': '-|>', 'color': ORANGE, 'lw': 3})
a.text(5, 5.0, 'Concentration difference: outward', ha='center', color=ORANGE, fontsize=11)
a.annotate('', (2.0, 3.5), (7.9, 3.5), arrowprops={'arrowstyle': '-|>', 'color': BLUE, 'lw': 3})
a.text(5, 3.08, 'Electrical influence: inward', ha='center', color=BLUE, fontsize=11)
a.text(5, 2.0, '$V_m<0$', ha='center', fontsize=17, bbox={'facecolor':'white','edgecolor':'none','pad':3})
a.text(5, 1.05, 'Only K⁺ crosses; balancing anions stay behind.\nAt equilibrium: opposing influences balance.', ha='center', va='top', fontsize=11)
a.text(5, .02, 'Bulk solutions nearly electroneutral; excess near membrane.', ha='center', fontsize=10)

b = axes[1]
b.set_title('B  Intracellular voltage recording', fontsize=15, pad=14)
b.add_patch(FancyBboxPatch((.35, 1.2), 9.3, 3.5, boxstyle='round,pad=.1', facecolor='#edf6fa', edgecolor=BLUE, lw=1.4))
b.text(7.25, 1.48, 'External seawater\nreference: $\\phi_{out}=0$', ha='center', fontsize=12)
b.add_patch(Ellipse((3.4, 2.9), 5.2, 2.6, facecolor='#fff5f7', edgecolor='#87546c', lw=2))
b.text(3.4, 2.25, 'Axon interior\n$\\phi_{in}<\\phi_{out}$', ha='center', fontsize=13)
b.add_patch(FancyBboxPatch((3.0, 5.7), 5.8, 1.5, boxstyle='round,pad=.12', facecolor='white', edgecolor=INK, lw=1.5))
b.text(5.9, 6.7, 'Voltage recorder', ha='center', fontsize=13)
b.text(5.9, 6.13, '$V_m=\\phi_{in}-\\phi_{out}<0$', ha='center', color=BLUE, fontsize=14)
b.plot([3.5, 1.9, 1.9], [5.7, 5.7, 4.5], color=INK, lw=1.6)
b.plot([8.2, 8.9, 8.9], [5.7, 5.7, 3.2], color=INK, lw=1.6)
b.text(3.5, 5.47, '+', ha='center', fontsize=18)
b.text(8.2, 5.47, '−', ha='center', fontsize=18)
b.add_patch(Polygon([[1.65,4.6],[2.15,4.6],[2.02,3.3],[1.9,3.0],[1.78,3.3]], closed=True, facecolor='white', edgecolor=INK, lw=1.5))
b.plot([8.9,8.9], [3.8,3.1], color=INK, lw=5)
b.text(.65, 5.1, 'Intracellular\nelectrode tip', fontsize=11, ha='left')
b.annotate('', (1.9,3.05), (.95,4.9), arrowprops={'arrowstyle':'->','color':INK,'lw':1})
b.text(7.05, 4.8, 'External reference\nelectrode', ha='center', fontsize=11)
b.annotate('', (8.9,3.4), (8.0,4.55), arrowprops={'arrowstyle':'->','color':INK,'lw':1})
b.text(5, .73, 'Negative readout after electrode-offset correction.\nNo feedback imposing membrane voltage.', ha='center', va='top', fontsize=11)
fig.text(.5, .025, 'Original conceptual schematics • no measured values, historical dimensions or particle counts', ha='center', fontsize=10)
fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
plt.close(fig)
