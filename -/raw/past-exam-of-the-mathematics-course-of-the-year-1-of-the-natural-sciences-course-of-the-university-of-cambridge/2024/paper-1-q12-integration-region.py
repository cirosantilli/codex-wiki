"""Generate paper-1-q12-integration-region.png in the current directory.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/nst-2024-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np

R, d = 1.0, 0.45
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), layout='constrained', facecolor='white')
angles = np.linspace(0, 2*np.pi, 500)
s = np.linspace(-d, R, 450)
r = np.sqrt(np.maximum(0, R*R-s*s))
for ax in axes:
    ax.fill_between(s, -r, r, color='#d9eaf5')
    ax.plot(R*np.cos(angles), R*np.sin(angles), color='#17679a', linewidth=1.6)
    ax.plot([-d, -d], [-np.sqrt(R*R-d*d), np.sqrt(R*R-d*d)], color='#b3472d', linewidth=2)
    ax.axhline(0, color='gray', linewidth=0.7)
    ax.plot(0, 0, 'ko', markersize=3)
    ax.annotate('outward', (0.98, 0), (0.55, 0.1), fontsize=9,
                arrowprops={'arrowstyle': '->', 'color': 'gray'})
    ax.set(xlim=(-1.12, 1.22), ylim=(-1.12, 1.12), xlabel='axial coordinate $s$')
    ax.set_aspect('equal')
    ax.set_xticks([-d, 0, R], ['$-d$', '$0$', '$R$'])
    ax.set_yticks([])
axes[0].set_title(r'Cylindrical slices: $-d\leq s\leq R$')
s0=0.4
r0=np.sqrt(R*R-s0*s0)
axes[0].plot([s0, s0], [0, r0], color='#222222', linewidth=2)
axes[0].annotate(r'$\sqrt{R^2-s^2}$', (s0, r0/2), (0.48, 0.5), fontsize=10)
axes[0].text(-1.03, -1.02, 'White segment is removed', fontsize=9)
axes[1].set_title('Spherical shells: split at $r=d$')
axes[1].add_patch(Circle((0,0), d, facecolor='#a8cee7', edgecolor='#17679a', linestyle='--'))
# A shell at r>d has an angular limit at the cutting plane.
rho=0.83
theta=np.arccos(-d/rho)
arc=np.linspace(0, theta, 120)
axes[1].plot(rho*np.cos(arc), rho*np.sin(arc), color='#8051a1', linewidth=2)
axes[1].plot([0,-d], [0,rho*np.sin(theta)], color='#8051a1', linewidth=1.4)
axes[1].text(0.03, -0.19, r'$r\leq d$:'+'\nall angles', fontsize=9)
axes[1].annotate(r'$\theta_{\max}=\arccos(-d/r)$', (-d,rho*np.sin(theta)),
                 xytext=(-1.04,1.03), fontsize=9,
                 arrowprops={'arrowstyle':'->','color':'#8051a1'})
axes[1].text(-1.04, -1.02, r'$r>d$: keep $r\cos\theta\geq-d$', fontsize=9)
fig.suptitle('Question 12: meridional section of one end piece ($R=1$, $d=0.45$)', fontsize=12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=130, facecolor='white')
plt.close(fig)
