"""Original Cauchy-uniform convolution plot. Python 3.14; NumPy, Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

z = np.linspace(-6, 6, 1601)
h = (np.arctan(z+.5)-np.arctan(z-.5))/np.pi
f = 1/(np.pi*(1+z*z))
fig, ax = plt.subplots(figsize=(8.1, 4.8), facecolor='white')
ax.plot(z, h, color='#226a9f', linewidth=2.5, label='Cauchy + uniform displacement')
ax.plot(z, f, '--', color='#b36432', linewidth=1.6, label='standard Cauchy density')
height = 2*np.arctan(.5)/np.pi
ax.plot(0, height, 'o', color='#226a9f')
ax.annotate('unique mode: 0', (0, height), xytext=(1.6, .27), fontsize=11,
            arrowprops=dict(arrowstyle='->', color='#226a9f'))
ax.axvline(0, color='#999999', linewidth=.7, alpha=.5)
ax.set(xlim=(-6, 6), ylim=(0, .35), xlabel='$z$', ylabel='probability density')
ax.set_title('A symmetric density whose mean does not exist', fontsize=14)
ax.text(.5, -.24, r'Both tails: $h(z)\sim 1/(\pi z^2)$', transform=ax.transAxes,
        ha='center', fontsize=12)
ax.legend(loc='upper left', fontsize=9, frameon=False)
ax.spines[['top', 'right']].set_visible(False)
ax.grid(alpha=.15)
fig.subplots_adjust(left=.10, right=.97, bottom=.24, top=.89)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=155, facecolor='white')
plt.close(fig)
