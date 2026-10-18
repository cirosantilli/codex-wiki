"""Original schematic level assignments, using only the paper's rounded wavelengths.

Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
The sole output is a PNG in the caller's current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

p1 = 1 / (689e-9)
s3 = p1 + 1 / (688e-9)
fig, ax = plt.subplots(figsize=(11.5, 8), dpi=110, facecolor='white')
ax.set_facecolor('white')
ax.set_xlim(-0.5, 11.2)
ax.set_ylim(-0.7, 9.8)
ax.axis('off')
blue, red, grey = '#165d8d', '#a93b31', '#39434a'

def level(x1, x2, y, term, config, energy, side='right'):
    ax.plot([x1, x2], [y, y], color=grey, lw=2)
    if side == 'right':
        ax.text(x2 + 0.14, y, term + '\n' + f'{energy / 1e6:.3f}' + r'$\times10^6$', ha='left', va='center', fontsize=11.5)
    else:
        ax.text(x1 - 0.12, y, term + '\n' + f'{energy / 1e6:.3f}' + r'$\times10^6$', ha='right', va='center', fontsize=11.5)
    ax.text((x1 + x2) / 2, y + 0.22, config, ha='center', va='bottom', fontsize=11, color=grey)

def arrow(x1, y1, x2, y2, label, color, textx, texty, dashed=False):
    ax.annotate('', xy=(x2, y2 - 0.035), xytext=(x1, y1 + 0.035), arrowprops=dict(arrowstyle='<->', lw=1.7, color=color, linestyle='--' if dashed else '-'))
    ax.text(textx, texty, label, color=color, fontsize=12, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='none', pad=2))

level(1.7, 4.0, 0.0, r'$^1S_0$', r'$5s^2$', 0, 'left')
level(1.7, 4.0, 5.35, r'$^1P_1$', r'$5s5p$', 1 / (461e-9), 'left')
level(1.7, 4.0, 8.6, r'$^1S_0$', r'$5s6s$', 1 / (461e-9) + 1 / (1.12e-6), 'left')
level(6.0, 8.7, 2.15, r'$^3P_0$', '', s3 - 1 / (679e-9))
level(6.0, 8.7, 3.35, r'$^3P_1$', '', p1)
level(6.0, 8.7, 4.55, r'$^3P_2$', r'$5s5p$', s3 - 1 / (707e-9))
level(6.0, 8.7, 8.1, r'$^3S_1$', r'$5s6s$', s3)
arrow(2.4, 0, 2.4, 5.35, '461 nm', blue, 2.4, 3.0)
arrow(2.9, 5.35, 2.9, 8.6, r'1.12 $\mu$m', blue, 2.9, 6.9)
arrow(3.6, 0, 6.0, 3.35, '689 nm\nweak', red, 4.8, 1.5, True)
arrow(6.25, 2.15, 6.25, 8.1, '679 nm', blue, 6.25, 6.1)
arrow(7.3, 3.35, 7.3, 8.1, '688 nm', blue, 7.3, 6.65)
arrow(8.35, 4.55, 8.35, 8.1, '707 nm', blue, 8.35, 7.15)
ax.text(2.85, 9.35, 'Singlet levels', fontsize=15, ha='center', weight='bold', color=grey)
ax.text(7.35, 9.35, 'Triplet levels', fontsize=15, ha='center', weight='bold', color=grey)
ax.text(5.3, -0.52, r'Numbers: $(E-E_g)/(hc)$ in m$^{-1}$. Vertical spacings are schematic.', fontsize=12, ha='center', color=grey)
fig.subplots_adjust(left=0.035, right=0.985, top=0.985, bottom=0.03)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False, metadata={'Software': 'Matplotlib'})
plt.close(fig)
