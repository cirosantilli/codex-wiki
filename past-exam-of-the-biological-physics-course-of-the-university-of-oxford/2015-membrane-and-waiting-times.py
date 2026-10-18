"""Original qualitative voltage sketch and exact two-state/Erlang curves."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 3, figsize=(13, 4), layout='constrained', facecolor='white')
t = np.linspace(0, 8, 1000)
for width, label in [(.65, 'Usual repolarization'), (1.8, 'Reduced outward K current')]:
    rise = np.where(t < 1, np.exp(-((t - 1) / .18)**2), np.exp(-((t - 1) / width)**2))
    axes[0].plot(t, rise, lw=2, label=label)
axes[0].set(xlabel='Time (schematic)', ylabel='Voltage elevation (schematic)', title='Conditional broadening sketch', xlim=(0, 7), ylim=(-.05, 1.15))
axes[0].legend(fontsize=9, frameon=False)
axes[0].text(.96, .55, 'Not source data;\nnot an ionic-current simulation.', fontsize=9, ha='right', transform=axes[0].transAxes, bbox={'facecolor': 'white', 'alpha': .9, 'edgecolor': 'none'})
axes[1].plot(t, .6 * (1 - np.exp(-t)), lw=2, color='#176b87')
axes[1].axhline(.6, color='.5', ls='--')
axes[1].set(xlabel=r'$(k_f+k_b)t$', ylabel='B occupancy probability', title=r'Two states: $k_f/(k_f+k_b)=0.6$', xlim=(0, 8), ylim=(0, 1))
for n, color in [(2, '#176b87'), (3, '#c05229')]:
    density = t * np.exp(-t) if n == 2 else .5 * t**2 * np.exp(-t)
    axes[2].plot(t, density, color=color, lw=2, label=f'n = {n}')
    xmode = n - 1
    height = xmode * np.exp(-xmode) if n == 2 else .5 * xmode**2 * np.exp(-xmode)
    axes[2].plot([xmode], [height], 'o', color=color)
axes[2].set(xlabel=r'$kt$', ylabel=r'$p_n(t)/k$', title='Sequential waiting-time densities', xlim=(0, 8), ylim=(0, .43))
axes[2].legend(frameon=False)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', metadata={'Software': 'matplotlib'})
