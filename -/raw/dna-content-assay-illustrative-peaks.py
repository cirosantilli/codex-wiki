"""Synthetic DNA-content curves, not experimental measurements or a fit.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media.
A deliberately arbitrary normalized mixture illustrates phase ambiguity.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1.35, 4.65, 3301)
def gaussian(center, sigma):
    return np.exp(-0.5*((x-center)/sigma)**2)/(sigma*np.sqrt(2*np.pi))

g1 = 0.50*gaussian(2, 0.085)
g2 = 0.20*gaussian(4, 0.11)
z = (x-2)/2
s = np.zeros_like(x)
mask = (z >= 0) & (z <= 1)
s[mask] = 0.30*3*z[mask]*(1-z[mask])  # beta(2,2), rescaled onto [2,4]
total = g1+s+g2
assert np.all(total >= 0)
assert abs(np.trapezoid(total, x)-1) < 1e-6

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(9, 5.6), dpi=100, facecolor='white')
for y, color, label in [(g1, '#4d7ac7', 'G₀ / G₁ component'),
                         (s, '#2b9b7c', 'S component'),
                         (g2, '#b76899', 'G₂ / M component')]:
    ax.fill_between(x, y, color=color, alpha=0.20)
    ax.plot(x, y, color=color, linewidth=1.4, label=label)
ax.plot(x, total, color='#17324d', linewidth=2.2, label='Synthetic sum')
ax.axvline(2, color='#4d7ac7', linestyle=':', linewidth=1)
ax.axvline(4, color='#b76899', linestyle=':', linewidth=1)
ax.set(xlim=(1.35, 4.65), ylim=(0, 3.1),
       xlabel='DNA-proportional fluorescence (C units for reference diploid cells)',
       ylabel='Illustrative event density (arbitrary units)')
ax.set_xticks([2, 3, 4], ['2C', '3C', '4C'])
ax.set_yticks([])
ax.text(2, 2.63, 'G₀ or G₁\namount alone cannot separate them',
        ha='center', fontsize=11, color='#365889')
ax.text(4, 1.0, 'G₂ or M', ha='center', fontsize=12, color='#8d4673')
ax.text(3, 0.38, 'S: intermediate DNA amount', ha='center', fontsize=11,
        color='#197459')
ax.spines[['top', 'right']].set_visible(False)
ax.legend(loc='upper right', frameon=False, fontsize=10)
fig.suptitle('Illustrative DNA-content assay peaks — NOT measured data',
             fontsize=15, weight='bold', y=0.98, color='#17324d')
fig.text(0.5, 0.025, 'Arbitrary widths and weights; intact singlets and one ploidy assumed.',
         ha='center', fontsize=10, color='#536575')
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.18, top=0.89)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
plt.close(fig)
