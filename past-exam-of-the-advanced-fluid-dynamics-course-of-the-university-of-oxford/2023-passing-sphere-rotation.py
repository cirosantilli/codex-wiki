"""Original one-way Stokes-sphere rotation model; write PNG only in cwd.

Tested with Python3.14, NumPy2.3.5, Matplotlib3.10.7; root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
s = np.linspace(-7, 7, 1001)
rate = -.75/(1+s*s)**1.5
fraction = .5*(1+s/np.sqrt(1+s*s))
fig, axes = plt.subplots(1, 2, figsize=(10.2, 3.9), dpi=130, facecolor='white')
ax = axes[0]
ax.plot(s, rate, color='#236c9d', lw=2)
ax.axhline(0, color='#777777', lw=.7)
ax.axvline(0, color='#888888', ls=':', lw=1)
ax.plot(0, -.75, 'o', color='#236c9d')
ax.text(.4, -.74, 'Closest passage', color='#236c9d')
ax.set(ylabel=r'$\Omega_y\ell^2/(aU)$', title='Rotation about the negative y axis', ylim=(-.85, .055))
ax = axes[1]
ax.plot(s, fraction, color='#9a4a27', lw=2)
ax.axhline(1, color='#888888', ls='--', lw=1)
ax.axvline(0, color='#888888', ls=':', lw=1)
ax.plot(0, .5, 'o', color='#9a4a27')
ax.text(.5, .36, 'Half the final angle\nat closest passage', color='#9a4a27')
ax.set(ylabel=r'$\theta_y/[-3a/(2\ell)]$', title='Finite total angle after passage', ylim=(-.05, 1.1))
for ax in axes:
    ax.set(xlim=(-7, 7), xlabel=r'Passage coordinate $Ut/\ell=-Z/\ell$')
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(alpha=.18)
fig.suptitle('Prescribed isolated-sphere flow: angular rate and accumulated rotation', fontsize=13)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
