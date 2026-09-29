"""Original inventory and density example; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

BLUE = '#205c91'
ORANGE = '#b85f18'
GREEN = '#176b50'
plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig = plt.figure(figsize=(11, 6), dpi=120, facecolor='white')
fig.suptitle('Size, specific energy, and volume-weighted density', fontsize=18, weight='bold', y=.97)
fig.text(.5, .905, 'Hypothetical examples; curves are bulk scaling laws, not measured data', ha='center', color='#555555')
upper = fig.add_axes([.085, .57, .35, .25])
lower = fig.add_axes([.085, .17, .35, .25])
mass = np.linspace(1, 6, 101)
upper.plot(mass, 20 * mass, color=BLUE, linewidth=2.5)
upper.scatter([2, 4, 6], [40, 80, 120], color=BLUE, zorder=3)
upper.set(xlim=(.7, 6.3), ylim=(0, 135), xlabel='Mass m (kg)', ylabel='Internal energy U (kJ)', title='A: extensive inventory grows')
lower.plot(mass, np.full_like(mass, 20), color=GREEN, linewidth=2.5)
lower.scatter([2, 4, 6], [20, 20, 20], color=GREEN, zorder=3)
lower.set(xlim=(.7, 6.3), ylim=(0, 30), xlabel='Mass m (kg)', ylabel='Specific energy u (kJ/kg)', title='A: U/m stays fixed')
for ax in [upper, lower]:
    ax.grid(alpha=.2)
    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.spines[['top', 'right']].set_visible(False)
right = fig.add_axes([.50, .12, .47, .73])
right.set(xlim=(0, 10), ylim=(0, 8))
right.axis('off')
right.text(5, 7.45, 'Two separated parcels at T = 300 K', ha='center', fontsize=13, weight='bold')
right.text(5, 7.00, 'Equal temperature does not mean identical state', ha='center', fontsize=10, color='#555555')
right.add_patch(Rectangle((.5, 5.45), 2.25, 1, facecolor='#e5eff8', edgecolor=BLUE, linewidth=1.6))
right.add_patch(Rectangle((2.75, 5.45), 6.75, 1, facecolor='#fff0df', edgecolor=ORANGE, linewidth=1.6))
right.text(1.625, 5.95, 'A: 2 L', ha='center', color=BLUE, weight='bold')
right.text(6.125, 5.95, 'B: 6 L', ha='center', color=ORANGE, weight='bold')
right.text(1.625, 5.03, '2 kg', ha='center', color=BLUE)
right.text(6.125, 5.03, '3 kg', ha='center', color=ORANGE)
right.text(1.625, 4.60, r'$\rho_A=1000$ kg/m³', ha='center', color=BLUE, fontsize=10)
right.text(6.125, 4.60, r'$\rho_B=500$ kg/m³', ha='center', color=ORANGE, fontsize=10)
right.text(5, 3.84, 'Volume fractions: A = ¼, B = ¾', ha='center', weight='bold')
right.text(5, 3.27, '5 kg / 0.008 m³ = 625 kg/m³', ha='center', color=GREEN, fontsize=15, weight='bold')
right.text(5, 2.70, '¼ × 1000 + ¾ × 500 = 625', ha='center', color=GREEN, fontsize=13)
# Place density markers on one calibrated horizontal axis.
xpos = lambda rho: .6 + (rho - 450) / 600 * 8.8
right.plot([xpos(450), xpos(1050)], [1.45, 1.45], color='#777777', linewidth=1)
for rho, color, text_y, label in [(500, ORANGE, .90, 'B: 500'), (625, GREEN, 1.98, 'Composite: 625'), (750, '#666666', .55, 'Unweighted: 750'), (1000, BLUE, 1.98, 'A: 1000')]:
    x = xpos(rho)
    right.plot([x, x], [1.35, 1.55], color=color)
    right.scatter([x], [1.45], color=color, s=45, zorder=3)
    right.text(x, text_y, label, ha='center', color=color, fontsize=10, weight='bold' if rho == 625 else 'normal')
right.text(5, .03, 'Density (kg/m³); weights come from volume', ha='center', fontsize=10, color='#444444')
fig.text(.265, .045, 'A: each copy adds 2 kg and 40 kJ', ha='center', color='#444444', fontsize=10)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120, facecolor='white', transparent=False)
plt.close(fig)
