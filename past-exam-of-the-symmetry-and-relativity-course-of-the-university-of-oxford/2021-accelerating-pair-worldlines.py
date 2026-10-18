"""Original accelerated-pair worldlines; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Dimensionless units c = ell = 1; d = ell. Both branches include their inertial past.
t = np.linspace(-2, 3.2, 1400)
d, beta = 1.0, 0.6
gamma = 1 / np.sqrt(1 - beta**2)
f = np.sqrt(1 + np.maximum(t, 0)**2) - 1
xe, xp = -f, d + f
fig, axes = plt.subplots(1, 2, figsize=(9.0, 5.0), layout='constrained', facecolor='white')
for ax, moving in zip(axes, (False, True)):
    for x, colour, label in ((xe, '#2166ac', 'electron'), (xp, '#b2182b', 'positron')):
        xx, tt = (gamma*(x-beta*t), gamma*(t-beta*x)) if moving else (x, t)
        ax.plot(xx, tt, color=colour, lw=2.2, label=label)
    switch_x = np.array([0, d])
    sx, st = (gamma*switch_x, -gamma*beta*switch_x) if moving else (switch_x, np.zeros(2))
    ax.scatter(sx, st, c=['#2166ac', '#b2182b'], zorder=5, s=38)
    line_x = np.linspace(-3.0, 3.0, 100)
    ax.plot(line_x, -beta*line_x if moving else line_x*0, '--', color='0.4', lw=1.3, label='field switches on')
    ax.axvline(0, color='0.75', lw=0.7)
    ax.axhline(0, color='0.75', lw=0.7)
    ax.set(xlim=(-3, 3), ylim=(-2, 3.4), xlabel=(r"$x'/\ell$" if moving else r'$x/\ell$'), ylabel=(r"$ct'/\ell$" if moving else r'$ct/\ell$'))
    ax.set_aspect('equal', adjustable='box')
    ax.grid(alpha=0.18)
    ax.set_title(r"Moving frame $S'$: $v=0.6c$" if moving else r'Laboratory $S$: $d=\ell$')
axes[0].legend(loc='upper left', fontsize=9)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=140, facecolor='white', transparent=False)
