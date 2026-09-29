"""Original mechanical schematic and nondimensional search model; Python 3.14."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), layout='constrained', facecolor='white')
a = axes[0]
a.set(xlim=(0, 10), ylim=(0, 6), title='A  Dual-trap transcription readout')
for x in (1.5, 8.5):
    a.add_patch(Circle((x, 3), .75, facecolor='#c5e4f5', edgecolor='#16719a', lw=2))
    a.plot([x, x], [1.8, 4.2], color='#de824b', alpha=.6, lw=3)
    a.text(x, 1.2, 'trapped bead', ha='center')
a.plot([2.25, 5.0], [3, 3], color='#328750', lw=3)
a.text(3.7, 3.4, 'DNA tether', ha='center')
a.add_patch(Circle((5.4, 3), .48, facecolor='#f6d581', edgecolor='#8d6514', lw=2))
a.text(5.4, 4.0, 'RNA polymerase', ha='center')
a.plot([5.88, 7.75], [3, 3], color='#73529b', lw=2)
a.text(7, 3.4, 'attachment', ha='center')
a.annotate('', xy=(6.3, 2.1), xytext=(4.6, 2.1), arrowprops={'arrowstyle':'->', 'lw':2})
a.text(5.45, 1.6, 'motion changes tether length', ha='center')
a.text(5, .3, 'One base pair ≈ 0.34 nm; schematic not to scale', ha='center', fontsize=10)
a.axis('off')
a = axes[1]
x = np.linspace(.15, 4, 600)
a.plot(x, 1/x, label='3D contribution  $1/u$', color='#16899d')
a.plot(x, x, label='1D contribution  $u$', color='#d48120')
a.plot(x, x+1/x, label='total  $u+1/u$', color='#49368a', lw=2.5)
a.scatter([1], [2], color='#49368a', zorder=4)
a.annotate('minimum: equal costs', (1, 2), (1.4, 4.5), arrowprops={'arrowstyle':'->'})
a.set(xlabel=r'$u=\lambda/\lambda_*$', ylabel=r'$\tau/\sqrt{AB}$', ylim=(0, 8), title='B  Sliding and relocation balance')
a.legend(frameon=False)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=110, facecolor='white')
