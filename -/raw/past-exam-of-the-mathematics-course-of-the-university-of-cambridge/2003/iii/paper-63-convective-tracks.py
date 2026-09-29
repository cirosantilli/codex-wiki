"""Schematic fixed-mass tracks for the stated opacity; output to caller CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6.4, 4.5), layout='constrained')
y = np.linspace(1.0, -1.0, 220)
for hydrogen, mu, color in [(0.7, 8/13, '#a23b27'), (0.8, 4/7, '#17609c')]:
    shift = 8*np.log10(mu/(4/7))
    x = (y+shift)/20
    ax.plot(x, y, color=color, lw=2.5, label=rf'$X={hydrogen},\ \mu={mu:.3f}$')
    k = 100
    ax.annotate('', xy=(x[k+25], y[k+25]), xytext=(x[k], y[k]),
                arrowprops={'arrowstyle':'->','color':color,'lw':2.5})
ax.set_xlim(0.075, -0.065)
ax.set_ylim(-1.12,1.12)
ax.set_xlabel(r'$\log_{10}(T_e/T_*)$   (hotter to the left)')
ax.set_ylabel(r'$\log_{10}(L/L_*)$')
ax.set_title('Same mass, fixed opacity coefficient')
ax.grid(alpha=.22)
ax.legend(loc='upper right', framealpha=.95)
fig.savefig(Path('paper-63-convective-tracks.png'), dpi=135, facecolor='white')
