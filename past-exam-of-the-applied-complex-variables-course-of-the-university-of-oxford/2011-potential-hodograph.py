"""Original solution planes. Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Writes 2011-potential-hodograph.png to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.7), facecolor='white')
blue, red = '#2166a5', '#ad443e'
a = axes[0]
a.fill_between([-2.7, 2.7], 0, 1, color='#e1edf8')
a.plot([-2.7, 2.7], [0, 0], color=blue, lw=2)
a.plot([-2.7, 2.7], [1, 1], color=red, lw=2)
a.scatter([0], [0], color='black', s=25, zorder=5)
a.text(0, -0.1, '$B:0$', ha='center', va='top')
a.text(-1.5, -0.24, '$AB$', ha='center')
a.text(1.5, -0.24, '$BC$', ha='center')
a.text(0, 1.1, r'Free streamline: $\psi=1$', ha='center', color=red)
a.text(-2.7, 0.5, r'$-\infty$', ha='center')
a.text(2.7, 0.5, r'$+\infty$', ha='center')
a.annotate('', (1.3, 0.48), (0.4, 0.48), arrowprops=dict(arrowstyle='->', color=blue))
a.text(2.35, -0.1, r'$\phi$', va='top')
a.set_title(r'Potential $w=\phi+i\psi$')
a.set_xlim(-3.2, 3.2);a.set_ylim(-0.6, 1.6)
a.axis('off')
for a, angle, title in [(axes[1], 135, r'Velocity $q=w^{\prime}$'), (axes[2], 180, 'Power $s=q^{4/3}$')]:
    a.add_patch(Wedge((0, 0), 1, 0, angle, facecolor='#e1edf8', edgecolor='none'))
    th = np.linspace(0, np.deg2rad(angle), 300)
    a.plot(np.cos(th), np.sin(th), color=red, lw=2)
    ends = [np.array([1., 0.]), np.array([np.cos(th[-1]), np.sin(th[-1])])]
    for p in ends:a.plot([0, p[0]], [0, p[1]], color=blue, lw=2)
    a.scatter([0], [0], color='black', s=25)
    a.text(0.02, -0.14, '$B:0$', ha='center')
    a.text(1.02, -0.12, r'$C,C^{\prime}:1$', ha='center', fontsize=10)
    if angle == 135:
        a.text(-0.79, 0.81, r'$A,A^{\prime}:e^{3\pi i/4}$', ha='center', fontsize=10)
        a.text(0.54, 0.89, '$|q|=1$', color=red)
        a.text(-0.17, 0.28, r'$3\pi/4$', fontsize=10)
    else:
        a.text(-1.02, -0.12, r'$A,A^{\prime}:-1$', ha='center', fontsize=10)
        a.text(0.26, 0.88, '$|s|=1$', color=red)
    a.set_title(title)
    a.set_aspect('equal');a.set_xlim(-1.5, 1.5);a.set_ylim(-0.4, 1.4);a.axis('off')
fig.tight_layout(w_pad=2)
fig.savefig('2011-potential-hodograph.png', dpi=160, facecolor='white')
