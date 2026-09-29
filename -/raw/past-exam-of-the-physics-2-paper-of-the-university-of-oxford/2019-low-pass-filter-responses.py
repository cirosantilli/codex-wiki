"""Original ideal filter responses; Python 3.14, NumPy and Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12, 'axes.spines.top':False, 'axes.spines.right':False})
fig, axes = plt.subplots(1, 2, figsize=(10, 4.4), layout='constrained', facecolor='white')
f = np.logspace(1, 6, 1000)
tau = 16e-6
h = 1/(1+2j*np.pi*f*tau)
for gain, label, color in [(1, 'Passive RC', '#2e73b5'), (-5, 'Active inverting', '#b34e31')]:
    axes[0].semilogx(f, abs(gain*h), label=label, color=color, lw=2)
    phase = np.angle(h, deg=True) + (180 if gain < 0 else 0)
    axes[1].semilogx(f, phase, label=label, color=color, lw=2)
for ax in axes:
    ax.axvline(1/(2*np.pi*tau), ls=':', color='#555555')
    ax.set_xlabel('Frequency (Hz)')
    ax.grid(alpha=0.22)
    ax.legend()
axes[0].set(ylabel=r'Amplitude ratio $|V_o/V_i|$', ylim=(0, 5.3), title='Same corner; active gain is five times larger')
axes[1].set(ylabel='Output phase relative to input (degrees)', ylim=(-100, 195), title='Active phase includes the inversion')
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', transparent=False)
