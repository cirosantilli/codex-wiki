"""Original solution figure; Python 3.14, root NumPy/Matplotlib dependencies.
Write the opaque PNG basename in cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

R, L, C, V = 10., .15, 10e-6, 15.
alpha = R/(2*L)
w0 = 1/np.sqrt(L*C)
wd = np.sqrt(w0*w0-alpha*alpha)
t = np.linspace(0, .100, 4000)
env = V/(L*wd)*np.exp(-alpha*t)
peak_t = np.arctan(wd/alpha)/wd
peak_i = V/(L*wd)*np.exp(-alpha*peak_t)*np.sin(wd*peak_t)
fig, ax = plt.subplots(figsize=(8.3, 4.3), dpi=130, facecolor='white')
ax.plot(t*1000, env*np.sin(wd*t)*1000, color='#31688e', lw=1.5)
ax.plot(t*1000, env*1000, '--', color='0.5', lw=1)
ax.plot(t*1000, -env*1000, '--', color='0.5', lw=1)
ax.axhline(0, color='0.4', lw=.6)
ax.scatter([peak_t*1000], [peak_i*1000], color='#d55e00', zorder=3)
ax.annotate('First peak: 115 mA at 1.875 ms', (peak_t*1000, peak_i*1000), (18, 105),
            fontsize=10, arrowprops=dict(arrowstyle='->', color='#d55e00'))
ax.annotate(r'$T_d=7.702$ ms', (24, -75), fontsize=11)
ax.text(53, 86, r'Envelope: $\pm122.6e^{-t/(30\,\mathrm{ms})}$ mA', fontsize=10)
ax.set(xlim=(0, 100), ylim=(-130, 137), xlabel='Time / ms', ylabel='Discharge current / mA',
       title=r'Series discharge: $Q=12.25$, initial slope $100$ A/s')
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
