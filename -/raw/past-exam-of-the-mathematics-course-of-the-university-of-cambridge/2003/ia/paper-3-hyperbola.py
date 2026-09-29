"""Hyperbola sketch; tested Python 3.14 / numpy 2.3.5 / matplotlib 3.10.7.
Generate an opaque basename PNG in caller CWD, honoring supplied MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x = np.linspace(-3.4, 3.4, 1000)
y = np.sqrt(1+x*x)
fig, ax = plt.subplots(figsize=(6, 6), layout='constrained')
ax.plot(x, y, color='#176b91', linewidth=2)
ax.plot(x, -y, color='#176b91', linewidth=2)
ax.plot(x, x, color='0.5', ls='--', linewidth=1, label=r'asymptotes $y=\pm x$')
ax.plot(x, -x, color='0.5', ls='--', linewidth=1)
ax.axhline(0, color='0.3', linewidth=.8)
ax.axvline(0, color='0.3', linewidth=.8)
ax.scatter([0,0],[1,-1], color='#b84326', zorder=5)
ax.annotate(r'$(0,1)$: $\mathcal{R}=1$', (0,1), (.7,.5), arrowprops={'arrowstyle':'->','color':'0.3'}, fontsize=10)
ax.annotate(r'$(0,-1)$: $\mathcal{R}=1$', (0,-1), (.7,-.6), arrowprops={'arrowstyle':'->','color':'0.3'}, fontsize=10)
ax.set(xlim=(-3.4,3.4), ylim=(-3.7,3.7), xlabel='$x$', ylabel='$y$', title=r'$y^2-x^2=1$: minimum curvature radius at the vertices')
ax.set_aspect('equal'); ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=9)
fig.savefig('paper-3-hyperbola.png', dpi=140, facecolor='white', transparent=False)
plt.close(fig)
