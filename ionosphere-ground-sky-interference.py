"""Original ionospheric path/interference schematic. Python 3.14; numpy/matplotlib.

Run from _media; writes this generator's basename.png to the working directory.
The physical ray is qualitative; dashed geometry and fringe data are a stipulated
nondispersive example, not a reconstruction of historical measurements.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig = plt.figure(figsize=(11, 5.1), layout='constrained')
gs = fig.add_gridspec(2, 2, height_ratios=[4, 1.15])
ax = fig.add_subplot(gs[0, 0])
ax.set(xlim=(-12, 162), ylim=(-15, 139), xlabel='Station separation (km)', ylabel='Height (km)')
ax.set_title('Two arrivals; one receiver', fontweight='bold')
for lower in np.arange(65, 112, 4):
    ax.axhspan(lower, lower + 4, color='#6ca6d8', alpha=0.04 + 0.002 * (lower - 65), lw=0)
ax.text(7, 124, 'Ionosphere: a graded plasma', color='#315b80')
x = np.linspace(0, 150, 500)
y = 88 * (1 - ((x - 75) / 75)**2)
ax.plot(x, y, color='#b54b20', lw=2.5, label='Curved skywave (schematic)')
ax.add_patch(FancyArrowPatch((104, float(88*(1-((104-75)/75)**2))), (112, float(88*(1-((112-75)/75)**2))), arrowstyle='->', color='#b54b20', mutation_scale=13, lw=2))
ax.plot([0, 75, 150], [0, 100, 0], '--', color='#555555', lw=1.5, label='Equivalent straight-ray model')
ax.plot([0, 150], [0, 0], color='#157870', lw=2.5, label='Ground wave')
ax.annotate('', (116, 0), (101, 0), arrowprops={'arrowstyle': '->', 'color': '#157870', 'lw': 2})
ax.plot([75, 75], [0, 100], ':', color='#777777')
ax.text(79, 45, '$h=100$ km\n(equivalent)', fontsize=9)
for xx, label in [(0, 'T'), (150, 'R')]:
    ax.plot(xx, 0, 'o', color='black', ms=5)
    ax.text(xx, -10, label, ha='center', weight='bold')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.22), fontsize=8.5, frameon=False)
ax.spines[['top', 'right']].set_visible(False)

ax = fig.add_subplot(gs[0, 1])
f = np.linspace(0, 12, 1500)
power = 1 + 0.7**2 + 2 * 0.7 * np.cos(2*np.pi*f/3)
ax.plot(f, power, color='#6d3c91', lw=2)
ax.set(xlabel='Frequency change from a maximum (kHz)', ylabel='Normalized squared received field', xlim=(0,12), ylim=(0,3.45), xticks=[0,3,6,9,12])
ax.set_title('Sweep frequency; count fringes', fontweight='bold')
ax.axhline(0.09, color='#999999', ls=':', lw=0.8)
ax.annotate('', xy=(3,3.12), xytext=(0,3.12), arrowprops={'arrowstyle':'<->','lw':1.2})
ax.text(1.5,3.24, r'$\Delta f=3$ kHz', ha='center')
ax.text(6,0.43, r'$A_g=1,\quad A_s=0.7$', ha='center', bbox={'facecolor':'white','edgecolor':'none','alpha':0.9})
ax.grid(alpha=0.16)
ax.spines[['top','right']].set_visible(False)

flow=fig.add_subplot(gs[1,:]);flow.axis('off')
labels=['Transmitter\ncontrolled frequency sweep', 'Ground + sky paths\ndifferent propagation delays', 'Tuned receiver + detector\nsuperposed field → fringes']
centers=[0.16,0.50,0.84]
for center,label in zip(centers,labels):
    flow.add_patch(FancyBboxPatch((center-.145,.18),.29,.65,boxstyle='round,pad=0.01',facecolor='#f4f7fa',edgecolor='#6f8091', transform=flow.transAxes))
    flow.text(center,.5,label,ha='center',va='center',fontsize=9,transform=flow.transAxes)
for left,right in [(0.315,.345),(.655,.685)]:
    flow.annotate('',(right,.5),(left,.5),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.5})
fig.savefig(Path(__file__).stem + '.png', dpi=120, facecolor='white', transparent=False)
