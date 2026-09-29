"""Original 3D angular-pressure illustration, not an experimental record.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; writes radiation-pressure-isotropic-angular-average.png.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc

BLUE, GREEN = '#1768a8', '#16805c'
fig, (geometry, weights) = plt.subplots(1, 2, figsize=(10, 4.9), facecolor='white', gridspec_kw={'width_ratios': [1, 1.25]})
fig.subplots_adjust(left=.035, right=.975, bottom=.20, top=.79, wspace=.25)
fig.suptitle('Isotropic radiation: grazing paths transfer less normal momentum', fontsize=15, y=.96)
geometry.set(xlim=(0, 1), ylim=(0, 1), aspect='equal')
geometry.axis('off')
geometry.set_title('Incoming hemisphere at a wall', fontsize=12, pad=12)
geometry.add_patch(Rectangle((.78, .025), .06, .95, facecolor='#dbe5eb', edgecolor='#263846'))
geometry.plot([.03, .78], [.5, .5], ls='--', lw=1.3, color='#5b6670')
for start in [(.12, .9), (.08, .68), (.06, .5), (.08, .32), (.12, .10)]:
    geometry.annotate('', (.765, .5), start, arrowprops={'arrowstyle': '-|>', 'color': BLUE, 'lw': 1.8, 'mutation_scale': 13})
geometry.add_patch(Arc((.78, .5), .5, .5, theta1=149, theta2=180, color='#bb5c13', lw=1.7))
geometry.text(.48, .56, r'$\theta$', color='#bb5c13', fontsize=15)
geometry.text(.1, .44, 'Normal line', fontsize=10, color='#5b6670')
geometry.text(.87, .5, 'Wall', rotation=90, fontsize=11, va='center')
geometry.text(.47, -.09, 'Arrival rate: one cos θ\nNormal momentum: another cos θ', ha='center', va='top', fontsize=11)

theta = np.linspace(0, np.pi / 2, 501)
angle = np.rad2deg(theta)
weights.plot(angle, np.sin(theta), color=BLUE, lw=2.4, label=r'Directional energy weight: $\sin\theta$')
weights.plot(angle, np.sin(theta) * np.cos(theta)**2, color=GREEN, lw=2.4, label=r'Pressure weight: $\sin\theta\cos^2\theta$')
weights.fill_between(angle, np.sin(theta) * np.cos(theta)**2, color=GREEN, alpha=.13)
weights.set(xlim=(0, 90), ylim=(0, 1.08), xticks=[0, 30, 60, 90], xlabel='Incidence angle θ (degrees)', ylabel='Angular density per radian')
weights.set_title('3D hemisphere weights after azimuth integration', fontsize=12, pad=12)
weights.grid(alpha=.18)
weights.spines[['top', 'right']].set_visible(False)
weights.legend(loc='upper left', fontsize=9, frameon=False)
weights.text(43, .55, r'$\int_0^{\pi/2}\sin\theta\,d\theta=1$' + '\n' + r'$\int_0^{\pi/2}\sin\theta\cos^2\theta\,d\theta=1/3$', fontsize=12, bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .92, 'pad': 3})
fig.text(.71, .035, r'$p=2\,[u/(4\pi)]\,(2\pi)\,(1/3)=u/3$', ha='center', fontsize=13)
fig.savefig(Path(__file__).stem + '.png', dpi=110, facecolor='white')
plt.close(fig)
