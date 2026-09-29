"""Original jet arrival-time geometry; Python 3.14, numpy, matplotlib.

Write paper-1-jet-arrival.png to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

plt.rcParams.update({'font.size': 10, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, (ax, curve) = plt.subplots(1, 2, figsize=(11.2, 4.7), layout='constrained')
x, z = 1.55, 2.25
ax.annotate('', (x, z), (0, 0), arrowprops={'arrowstyle': '-|>', 'lw': 2, 'color': '#1965b0'})
ax.plot([0, 0], [0, 3.7], color='#777777', ls='--', lw=1)
for xx, zz, col in [(0, 0, '#cc503e'), (x, z, '#009e73')]:
    ax.annotate('', (xx, 3.7), (xx, zz + 0.06), arrowprops={'arrowstyle': '->', 'lw': 1.6, 'color': col})
ax.scatter([0, x], [0, z], s=38, c=['#cc503e', '#009e73'], zorder=5)
ax.text(-0.18, -0.12, r'$A$', ha='right')
ax.text(x + .13, z, r'$B$', va='center')
ax.text(0.57, 1.05, r'$u\Delta t_e$', rotation=55, color='#1965b0', ha='center',
        bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
ax.annotate('', (x, -.4), (0, -.4), arrowprops={'arrowstyle': '<->', 'color': '#333333'})
ax.text(x/2, -.68, r'$u\Delta t_e\sin\theta$', ha='center')
ax.annotate('', (2.22, z), (2.22, 0), arrowprops={'arrowstyle': '<->', 'color': '#333333'})
ax.text(2.39, z/2, r'$u\Delta t_e\cos\theta$', rotation=90, va='center')
ax.plot([x, 2.2], [z, z], color='#bbbbbb', ls=':')
ax.plot([0, 2.2], [0, 0], color='#bbbbbb', ls=':')
angle = np.degrees(np.arctan2(z, x))
ax.add_patch(Arc((0, 0), 1.25, 1.25, theta1=angle, theta2=90, color='#333333'))
ax.text(.24, .83, r'$\theta$')
ax.text(.78, 3.95, 'Parallel rays to a distant observer', ha='center')
ax.text(.78, -1.12, r'$\Delta t_{\rm obs}=\Delta t_e(1-\beta\cos\theta)$', ha='center')
ax.set(xlim=(-.65, 3), ylim=(-1.4, 4.2), aspect='equal', title='Two emission events')
ax.axis('off')
theta = np.linspace(0, np.pi/2, 1000)
for beta, color in zip([.6, .8, .95, .995], ['#994f00', '#009e73', '#1965b0', '#882255']):
    apparent = beta*np.sin(theta)/(1-beta*np.cos(theta))
    curve.plot(np.degrees(theta), apparent, label=fr'$\beta={beta}$', color=color)
    maximum_theta = np.arccos(beta)
    curve.scatter(np.degrees(maximum_theta), beta/np.sqrt(1-beta**2), c=color, s=24)
curve.axhline(1, ls='--', lw=1, color='#555555', label=r'$u_t=c$')
curve.set(xlim=(0, 90), ylim=(0, 10.5), xlabel=r'Viewing angle $\theta$ (degrees)',
          ylabel=r'Apparent transverse speed $u_t/c$', title='Material speeds all below light speed')
curve.grid(alpha=.2)
curve.legend(frameon=False, loc='upper right')
fig.savefig('paper-1-jet-arrival.png', dpi=165, facecolor='white')
plt.close(fig)
