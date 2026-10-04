"""Original schematic; tested with Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Output is a PNG basename in the caller's working directory; honors MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(12, 22, 800)
y = -1.5 * (x - 13)
y -= np.maximum(x - 21, 0)**2 * 2
fig, ax = plt.subplots(figsize=(9, 4.5), dpi=140, facecolor='white')
ax.set_facecolor('white')
for lo, hi, color, label in [(12, 17.2, '#dbeaf8', 'Lyman-alpha forest'),
                            (17.2, np.log10(2e20), '#e9efcf', 'Lyman limit'),
                            (np.log10(2e20), 22, '#f7dfd9', 'Damped systems')]:
    ax.axvspan(lo, hi, color=color)
    ax.text((lo+hi)/2, 1.3, label, ha='center', va='center', fontsize=10)
weak = x <= 14
ax.plot(x[weak], y[weak], color='#164778', lw=2.4, label=r'Weak forest: $f\propto N^{-1.5}$')
ax.plot(x[~weak], y[~weak], '--', color='#164778', lw=2, label='Schematic high-column continuation')
for threshold in [17.2, np.log10(2e20)]:
    ax.axvline(threshold, color='#676767', linestyle=':', lw=1.1)
ax.set(xlim=(12, 22), ylim=(-18, 2.5),
       xlabel=r'$\log_{10}[N_{\mathrm{HI}}/(\mathrm{cm}^{-2})]$',
       ylabel=r'$\log_{10} f(N,z)$ (arbitrary normalization)',
       title='Neutral-hydrogen column distribution and absorber classes')
ax.set_xticks(np.arange(12, 23))
ax.grid(axis='y', alpha=.25)
ax.legend(loc='lower left', fontsize=9, framealpha=.95)
fig.text(.5, .015, 'Illustrative shape at one epoch; no fitted high-column slope or survey normalization.',
         ha='center', fontsize=9)
fig.tight_layout(rect=(0, .05, 1, 1))
fig.savefig(Path('paper-73-column-distribution.png'), facecolor='white', transparent=False)
plt.close(fig)
