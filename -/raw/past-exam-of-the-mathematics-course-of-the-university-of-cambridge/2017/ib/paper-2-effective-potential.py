"""Generate paper-2-effective-potential.png in the current working directory.

Original dimensionless diagram for a quadratic central potential, k>0 and h!=0.
Tested: Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5 (repository pins).
No command-line options or files outside the output directory are needed.
"""
from pathlib import Path
import os

os.environ.setdefault('MPLCONFIGDIR', '/tmp/2017-ib-paper-2-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

rho = np.linspace(.29, 2.5, 800)
fig, ax = plt.subplots(figsize=(7.6, 4.2), dpi=100)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
ax.plot(rho, rho**-2 + rho**2, color='#144f8c', lw=2.5,
        label=r'$V_{\rm eff}/(kmr_0^2)=\rho^{-2}+\rho^2$')
ax.plot(rho, rho**-2, '--', color='#b24e28', lw=1.5,
        label=r'Centrifugal term $\rho^{-2}$')
ax.plot(rho, rho**2, ':', color='#38864c', lw=1.9,
        label=r'Quadratic term $\rho^2$')
ax.axvline(1, ymin=0, ymax=2/8, color='#666666', lw=1)
ax.plot([1], [2], 'o', color='#144f8c', ms=6)
ax.annotate('Stable circular orbit', xy=(1, 2), xytext=(1.32, 3.5),
            arrowprops={'arrowstyle': '->', 'color': '#333333'}, fontsize=11)
ax.axhline(2.65, color='#555555', lw=.8, alpha=.7)
ax.text(.38, 2.79, 'Nearby radial motion', fontsize=10, color='#444444')
turns = np.sqrt([(2.65-np.sqrt(2.65**2-4))/2,
                 (2.65+np.sqrt(2.65**2-4))/2])
ax.plot(turns, [2.65, 2.65], 'o', color='#555555', ms=4)
ax.set(xlim=(.25, 2.5), ylim=(0, 8), xlabel=r'Radius $\rho=r/r_0$',
       ylabel=r'Energy / $kmr_0^2$')
ax.set_xticks([.5, 1, 1.5, 2, 2.5])
ax.legend(loc='upper center', fontsize=10, framealpha=1)
ax.spines[['top', 'right']].set_visible(False)
fig.subplots_adjust(left=.10, right=.98, bottom=.14, top=.97)
fig.savefig(Path.cwd()/'paper-2-effective-potential.png', dpi=100,
            facecolor='white', transparent=False)
plt.close(fig)
