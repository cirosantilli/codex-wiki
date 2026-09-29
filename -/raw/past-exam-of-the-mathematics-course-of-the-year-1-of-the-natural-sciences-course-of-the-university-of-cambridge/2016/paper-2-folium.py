"""Original folium sketch. Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Run in the mirrored _media directory; the white PNG is saved to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def point(t):
    return 3*t/(1+t**3), 3*t*t/(1+t**3)


fig, ax = plt.subplots(figsize=(6.8, 6.0), layout='constrained', facecolor='white')
for t in [np.linspace(-150, -1.008, 8000), np.linspace(-.992, 0, 3000),
          np.r_[0, np.geomspace(.001, 2000, 4000)]]:
    ax.plot(*point(t), color='#0072b2', lw=2)
x = np.linspace(-4, 4, 200)
ax.plot(x, -1-x, '--', color='#777777', label=r'Asymptote $x+y+a=0$')
ax.plot([0, 1.5], [0, 1.5], 'o', color='#d55e00', ms=5)
ax.annotate(r'$t=1$', (1.5, 1.5), xytext=(1.9, 1.9),
            arrowprops={'arrowstyle': '-', 'color': '#555555'})
ax.annotate(r'$t=0,\ t\to\pm\infty$', (0, 0), xytext=(.35, -.55), fontsize=10,
            arrowprops={'arrowstyle': '-', 'color': '#555555'})
for start, end in [(.19, .28), (1.7, 2.1), (-.55, -.6), (-1.75, -1.6)]:
    ax.annotate('', xy=point(end), xytext=point(start),
                arrowprops={'arrowstyle': '->', 'lw': 2, 'color': '#0072b2'})
ax.text(-2.7, 2.7, r'$t\to-1^+$', fontsize=11)
ax.text(2.0, -2.7, r'$t\to-1^-$', fontsize=11)
ax.axhline(0, color='#444444', lw=.8)
ax.axvline(0, color='#444444', lw=.8)
ax.set(xlim=(-3.2, 3.8), ylim=(-3.2, 3.8), xlabel=r'$x/a$', ylabel=r'$y/a$',
       title=r'Folium of Descartes ($a>0$); arrows increase $t$')
ax.set_aspect('equal')
ax.grid(alpha=.17)
ax.legend(loc='upper right', fontsize=9)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=160, facecolor='white')
