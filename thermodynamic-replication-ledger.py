"""Illustrate independent equilibrium replicas; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BLUE = '#205c91'
GREEN = '#176b50'
plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig = plt.figure(figsize=(10, 5.4), dpi=120, facecolor='white')
ax = fig.add_axes([0, 0, 1, 1])
ax.set(xlim=(0, 10), ylim=(0, 5.4))
ax.axis('off')
ax.text(5, 5.08, 'Replicate the inventory, preserve the state', ha='center', fontsize=19, weight='bold')
ax.text(5, 4.72, 'Independent identical copies at the same equilibrium state', ha='center', color='#444444')
centers = [2.35, 5.25, 8.15]
for count, center in enumerate(centers, 1):
    ax.text(center, 4.28, f'{count} copy' if count == 1 else f'{count} copies', ha='center', weight='bold', color=BLUE)
    for j in range(count):
        x = center + (j - (count - 1) / 2) * .52
        ax.add_patch(FancyBboxPatch((x - .20, 3.65), .40, .40, boxstyle='round,pad=.02', facecolor='#e5eff8', edgecolor=BLUE, linewidth=1.4))
    ax.text(center, 3.35, 'copies remain separated', ha='center', fontsize=10, color='#555555')
rows = [(r'Internal energy $U$', r'U_0'), (r'Entropy $S$', r'S_0'), (r'Volume $V$', r'V_0'), (r'Amount $n$', r'n_0')]
for i, (label, symbol) in enumerate(rows):
    y = 2.88 - i * .43
    ax.axhspan(y - .19, y + .19, xmin=.04, xmax=.96, facecolor='#f3f7fb' if i % 2 == 0 else 'white', zorder=0)
    ax.text(.45, y, label, va='center', fontsize=11)
    for count, center in enumerate(centers, 1):
        value = symbol if count == 1 else str(count) + symbol
        ax.text(center, y, '$' + value + '$', ha='center', va='center', color=BLUE, fontsize=14)
ax.add_patch(FancyBboxPatch((.4, .48), 9.2, .52, boxstyle='round,pad=.08', facecolor='#e6f2ec', edgecolor=GREEN))
ax.text(5, .76, r'Every copy and the composite:  $T=T_0$,  $p=p_0$,  $\mu=\mu_0$', ha='center', va='center', color=GREEN, fontsize=14)
ax.text(5, .16, r'$n$: amount in mol; entity count $N=nN_A$ also scales.  $\mu$: molar chemical potential.', ha='center', fontsize=10, color='#444444')
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=120, facecolor='white', transparent=False)
plt.close(fig)
