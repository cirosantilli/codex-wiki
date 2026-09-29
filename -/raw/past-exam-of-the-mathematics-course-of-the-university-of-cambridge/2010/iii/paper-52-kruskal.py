"""Draw Schwarzschild's Kruskal extension. Python 3.14; root numpy/matplotlib.

Writes paper-52-kruskal.png only to the caller's working directory.
MPLCONFIGDIR is supplied by the caller and is not changed here.
"""
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8.0, 5.7), dpi=140, facecolor='white')
ax.set_facecolor('white')
x = np.linspace(-2.25, 2.25, 1401)
boundary = np.sqrt(1 + x*x)
ax.fill_between(x, -boundary, boundary, color='#f2f2f2', zorder=0)
ax.fill_between(x, -x, boundary, color='#c6e3f4', zorder=1)
ax.plot(x, boundary, color='#9a2631', lw=2.4, zorder=3)
ax.plot(x, -boundary, color='#9a2631', lw=2.4, zorder=3)
ax.plot(x, x, '--', color='#294654', lw=1.5, zorder=2)
ax.plot(x, -x, '--', color='#294654', lw=1.5, zorder=2)
ax.scatter([0], [0], s=27, color='black', zorder=5)
ax.annotate('bifurcation sphere', xy=(0, 0), xytext=(-.95, .24), fontsize=9,
            arrowprops={'arrowstyle': '->', 'lw': .8})
ax.text(1.57, 0, 'I\nright exterior', ha='center', va='center', fontsize=11)
ax.text(-1.57, 0, 'III\nleft exterior', ha='center', va='center', fontsize=11)
ax.text(0, .74, 'II\nblack hole', ha='center', va='center', fontsize=11)
ax.text(0, -.73, 'IV\nwhite hole', ha='center', va='center', fontsize=11)
ax.text(0, 1.55, r'$r=0$ future singularity', ha='center', color='#9a2631', fontsize=10)
ax.text(0, -1.55, r'$r=0$ past singularity', ha='center', color='#9a2631', fontsize=10)
ax.annotate('future horizon\n'+r'$U_K=0$', xy=(.65, .65), xytext=(1.80, 1.40),
            fontsize=9, ha='center', arrowprops={'arrowstyle': '->', 'lw': .8})
ax.annotate('past horizon\n'+r'$V_K=0$', xy=(.65, -.65), xytext=(1.80, -1.40),
            fontsize=9, ha='center', arrowprops={'arrowstyle': '->', 'lw': .8})
ax.annotate('future', xy=(-2.11, 1.05), xytext=(-2.11, .55), ha='center', fontsize=9,
            arrowprops={'arrowstyle': '->', 'lw': 1})
ax.text(-2.11, -2.63, r'Blue: ingoing PG chart, $V_K>0$ and $U_KV_K<1$', fontsize=10, va='center')
ax.set_xlim(-2.32, 2.32)
ax.set_ylim(-2.76, 2.69)
ax.set_aspect('equal')
ax.set_xlabel(r'$X_K=(V_K-U_K)/2$')
ax.set_ylabel(r'$T_K=(V_K+U_K)/2$')
ax.set_title('Kruskal extension and the ingoing free-fall chart', fontsize=13, pad=12)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)
fig.subplots_adjust(left=.10, right=.96, bottom=.12, top=.89)
fig.savefig('paper-52-kruskal.png', facecolor='white', transparent=False)
plt.close(fig)
