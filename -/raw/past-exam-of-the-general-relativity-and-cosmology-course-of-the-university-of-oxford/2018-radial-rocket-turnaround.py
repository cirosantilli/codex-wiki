"""Compare bounded radial thrust with the exact Schwarzschild hovering demand."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

q = 0.4  # r_s/r_I, illustrative rather than an assigned physical parameter
x = np.linspace(q + 0.012, 2.4, 1200)
demand = 1 / (x**2 * np.sqrt(1 - q/x))
lo, hi = 1.0, 2.0
for _ in range(70):
    mid = (lo + hi)/2
    if 1/(mid**2*np.sqrt(1-q/mid)) > 1:
        lo = mid
    else:
        hi = mid
xc = (lo + hi)/2

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, ax = plt.subplots(figsize=(7.5, 4.7), layout='constrained')
ax.axvspan(0, q, color='#dddddd', label='Horizon and interior')
ax.plot(x, demand, color='#16659c', lw=2.5, label=r'$g_{\rm hover}/g=1/[x^2\sqrt{1-0.4/x}]$')
ax.axhline(1, color='#b45b14', ls='--', lw=1.8, label='Maximum onboard acceleration')
ax.plot([1], [1/np.sqrt(1-q)], 'o', color='#b22428')
ax.annotate(r'Proposed $r_I$: thrust is insufficient', (1, 1/np.sqrt(1-q)),
            xytext=(1.2, 2.15), arrowprops={'arrowstyle': '->', 'color': '#b22428'},
            color='#992227')
ax.plot([xc], [1], 'o', color='#11703e')
ax.axvline(xc, ymax=1/3.4, color='#11703e', ls=':')
ax.annotate(r'$r_c/r_I\approx$'+f'{xc:.3f}', (xc, 1), xytext=(1.45, 1.35),
            arrowprops={'arrowstyle': '->', 'color': '#11703e'}, color='#11703e')
ax.text(1.37, 0.42, 'Turning requires a larger radius\nand sufficiently early braking.', color='#11703e')
ax.set(xlim=(0, 2.4), ylim=(0, 3.4), xlabel=r'Radius $x=r/r_I$',
       ylabel='Required hovering acceleration / thrust limit',
       title=r'Radial reversal with bounded proper thrust ($r_s/r_I=0.4$)')
ax.grid(alpha=0.2)
ax.legend(loc='upper right', fontsize=9)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white', transparent=False)
plt.close(fig)
