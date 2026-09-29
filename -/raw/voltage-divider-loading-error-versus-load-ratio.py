"""Exact loading-error curves; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.

Run from _media; output is an opaque, white PNG in the current directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(9.6, 6.1))
fig.patch.set_facecolor('white')
x = np.logspace(-2, 3, 601)
for a, color in [(.1, '#59843e'), (1, '#185b8c'), (10, '#b95415')]:
    e = a / (a+(a+1)*x)
    ax.loglog(x, 100*e, color=color, lw=2.5,
              label=rf'$R_1/R_2={a:g}$', zorder=3)
ax.axhline(1, color='#777777', ls='--', lw=1.3)
ax.text(.014, 1.13, '1% shortfall', color='#555555', fontsize=11)
for xi, text, offset in [(1, '33.333…%', (16, 12)),
                         (10, '4.7619…%', (15, 14)),
                         (100, '0.497512…%', (-117, -29))]:
    yi = 100/(1+2*xi)
    ax.plot(xi, yi, 'o', color='#185b8c', ms=6, zorder=5)
    ax.annotate(text, (xi, yi), xytext=offset, textcoords='offset points',
                fontsize=11, color='#185b8c',
                bbox={'facecolor':'white', 'edgecolor':'none', 'pad':2},
                arrowprops={'arrowstyle':'-', 'color':'#185b8c'})
ax.plot(49.5, 1, 's', color='#185b8c', ms=5, zorder=5)
ax.annotate('Equal arms: x ≥ 49.5\nfor error ≤ 1%', (49.5, 1), xytext=(32, 35),
            textcoords='offset points', fontsize=11,
            arrowprops={'arrowstyle':'->', 'color':'#555555'},
            bbox={'facecolor':'white', 'edgecolor':'none', 'pad':3})
ax.set_xlim(.01, 1000); ax.set_ylim(.006, 110)
ax.set_xlabel(r'Load ratio $x=R_L/R_2$ (logarithmic scale)')
ax.set_ylabel(r'Loading shortfall $100e$ (%) (logarithmic scale)')
ax.set_title('Loading error depends on resistance ratios', fontweight='bold', pad=16)
ax.grid(True, which='major', color='#dddddd', lw=.8)
ax.legend(loc='lower left', framealpha=1, title=r'$e=a/[a+(a+1)x]$')
fig.text(.5, .025, 'Exact steady DC model: positive resistances, nonzero input voltage.\n'
         'Markers are calculations for equal arms, not measurements.', ha='center', fontsize=11)
fig.subplots_adjust(left=.12, right=.97, bottom=.2, top=.88)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=115, facecolor='white')
plt.close(fig)
