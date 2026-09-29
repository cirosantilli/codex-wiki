"""Original mixed-frame simultaneity diagram; write PNG into the working directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8.8, 6.2), dpi=150, facecolor='white')
ax.set_facecolor('white')
x = np.linspace(-1.8, 2.7, 400)
ax.fill_between(x, np.abs(x), 2.1, where=np.abs(x) <= 2.1,
                color='#eeeeee', label='Future light cone of O')
ax.plot(x, np.abs(x), color='#858585', lw=1.1, linestyle=':')
ax.plot(x, .5*x, color='#007c83', lw=2.0, label=r"$t'=0$, boost $v=0.5c$")
ax.axhline(1, color='#b54831', lw=2.0, label=r'$t=1$, original frame')
ax.axvline(0, color='#535353', lw=1.0)
ax.scatter([0, 2, 0], [0, 1, 1], s=55, color='#20232a', zorder=5)
ax.annotate(r'$O=(0,0)$', (0,0), xytext=(-78,-22), textcoords='offset points', fontsize=13)
ax.annotate(r'$C=(1,2)$', (2,1), xytext=(8,9), textcoords='offset points', fontsize=13)
ax.annotate(r'$D=(1,0)$', (0,1), xytext=(10,12), textcoords='offset points', fontsize=13)
ax.annotate('', xy=(.05,.91), xytext=(.05,.10), arrowprops=dict(arrowstyle='->', color='#535353', lw=1.4))
ax.text(.13,.45, 'timelike\nseparation', fontsize=11, va='center', color='#535353')
ax.text(1.10, -.73, r'$c=1$; coordinates are $(t,x)$', fontsize=11)
ax.set(xlim=(-1.7,2.8), ylim=(-.9,2.05), xlabel=r'Space $x$', ylabel=r'Time $t$')
ax.set_aspect('equal', adjustable='box')
ax.set_title('Simultaneity in changing frames is not transitive', fontsize=15, pad=13)
ax.legend(loc='upper left', framealpha=1, fontsize=10)
ax.grid(alpha=.16)
fig.tight_layout()
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, facecolor='white')
