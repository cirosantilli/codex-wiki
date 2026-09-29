"""Original exact crossed-field trajectories; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(9.2, 6.8), layout='constrained', facecolor='white')
# c=m=e=1. Electric dominated E=2, B=1; boost w=1/2.
w = 0.5
g = 1/np.sqrt(1-w*w)
a = np.sqrt(3)
s = np.linspace(0, 2.6, 600)
x = -g/a*(np.cosh(s)-1)
zprime = -g*w/a*s
zlab = g*g*w/a*(np.sinh(s)-s)
# Magnetic dominated E=1, B=2; B'=sqrt(3), angular frequency B'/g.
omega = np.sqrt(3)/g
rho = w/omega
theta = np.linspace(0, 4*np.pi, 900)
xmag = rho*(np.cos(theta)-1)
zmagprime = -rho*np.sin(theta)
zmaglab = g*rho*(theta-np.sin(theta))
items = [
    (axes[0,0], x, zprime, 'Electric dominated: pure-electric frame', True),
    (axes[0,1], x, zlab, 'Electric dominated: laboratory', False),
    (axes[1,0], xmag[:450], zmagprime[:450], 'Magnetic dominated: pure-magnetic frame', True),
    (axes[1,1], xmag, zmaglab, 'Magnetic dominated: laboratory', False),
]
for ax, xx, zz, title, primed in items:
    ax.plot(zz, xx, color='#2166ac', lw=2.1)
    ax.plot(zz[0], xx[0], 'o', color='#b2182b', ms=5, label='released from rest in lab')
    for frac in (0.22, 0.63):
        i = int(frac*(len(xx)-1))
        j = min(i+14, len(xx)-1)
        ax.annotate('', xy=(zz[j],xx[j]), xytext=(zz[i],xx[i]), arrowprops={'arrowstyle':'->','color':'#2166ac','lw':1.8})
    ax.set(xlabel=(r"$z'$" if primed else r'$z$'), ylabel=(r"$x'$" if primed else r'$x$'), title=title)
    ax.grid(alpha=0.2)
    ax.margins(0.12)
    ax.set_aspect('equal', adjustable='datalim')
axes[1,1].text(0.45, 0.09, 'cusps: electron momentarily at rest', transform=axes[1,1].transAxes, fontsize=8, ha='center')
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
