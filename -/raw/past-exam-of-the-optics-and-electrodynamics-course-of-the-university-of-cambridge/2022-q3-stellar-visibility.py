"""Original uniform-disk solution plot; Python 3.14, root pyproject dependencies.

Write opaque PNG basename in cwd, including in the mirrored _media directory.
Bessel visibility is evaluated by its convergent power series, without SciPy.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

alpha, wavelength = 226e-9, 570e-9
def visibility(baseline):
    x = np.pi*np.asarray(baseline)*alpha/wavelength
    term = np.ones_like(x)
    total = term.copy()
    for j in range(1, 65):
        term *= -x*x/(4*j*(j+1))
        total += term
    return total

fig, (short, long) = plt.subplots(1, 2, figsize=(9, 3.9), dpi=130, facecolor='white')
d = np.linspace(0, .005, 500)
short.plot(d*1000, (1-visibility(d))*1e6, color='#31688e', lw=2)
short.scatter([1], [(1-visibility(.001))*1e6], color='#d55e00', zorder=3)
short.annotate(r'$1-V=1.94\times10^{-7}$ at 1 mm', (1, .193944),
               (1.3, 2.25), fontsize=9, arrowprops=dict(arrowstyle='->', color='#d55e00'))
short.set(xlabel='Slit separation d / mm', ylabel=r'Visibility loss $(1-V)\times10^6$',
          title='Millimetre baselines barely resolve the disk', xlim=(0,5), ylim=(0,5.2))
D = np.linspace(0, 6, 1500)
Dzero = 3.8317059702075125/np.pi*wavelength/alpha
long.plot(D, np.abs(visibility(D)), color='#31688e', lw=2)
long.axvline(Dzero, color='#d55e00', ls='--', lw=1)
long.annotate('First null: 3.076 m', (Dzero, 0), (3.5, .55), fontsize=10,
              arrowprops=dict(arrowstyle='->', color='#d55e00'))
long.set(xlabel='Collector separation D / m', ylabel='Fringe visibility V',
         title='Uniform disk: angular diameter 226 nrad', xlim=(0,6), ylim=(-.025,1.06))
for ax in (short, long):
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.2)
fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
