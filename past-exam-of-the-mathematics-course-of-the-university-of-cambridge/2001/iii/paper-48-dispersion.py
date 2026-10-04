"""Rotating shallow-water dispersion; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Write only paper-48-dispersion.png in the caller's working directory.
The caller controls MPLCONFIGDIR; no environment variable is changed here.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

k = np.linspace(0, 4, 501)
w = np.sqrt(1+k*k)
fig, (left, right) = plt.subplots(1, 2, figsize=(9, 4), layout='constrained')
fig.patch.set_facecolor('white')
left.plot(k, w, color='#176b9c', label='Positive wave branch')
left.plot(k, -w, color='#b85a17', label='Negative wave branch')
left.axhline(0, color='#3d7837', linestyle='--', label='Geostrophic branch')
left.plot(k, k, ':', color='0.55', label='Gravity-wave asymptote')
left.plot(k, -k, ':', color='0.55')
left.set(xlabel=r'$K R_D$', ylabel=r'$\omega/f$', title='Dispersion', xlim=(0, 4), ylim=(-4.4,4.4))
left.legend(fontsize=8, loc='upper left')
z = k[k > .12]
right.plot(z, np.sqrt(1+z*z)/z, color='#8c338d', label='Phase speed')
right.plot(k, k/w, color='#176b9c', label='Group speed')
right.axhline(1, color='0.4', linestyle=':', label=r'Gravity-wave speed $c_0$')
right.set(xlabel=r'$K R_D$', ylabel=r'Speed / $c_0$', title='Positive-branch speeds', xlim=(0,4), ylim=(0,3.4))
right.legend(fontsize=8)
for ax in (left,right):
    ax.set_facecolor('white')
    ax.grid(alpha=.2)
fig.suptitle('Rotating shallow-water waves', fontsize=13)
fig.savefig(Path('paper-48-dispersion.png'), dpi=130, facecolor='white', transparent=False)
plt.close(fig)
