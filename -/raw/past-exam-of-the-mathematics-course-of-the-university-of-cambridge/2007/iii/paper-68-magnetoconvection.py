"""Original analytic magnetoconvection plots; tested with Python 3.14.

Run from the desired output directory. Uses the root numpy/matplotlib dependencies
and preserves a caller-supplied MPLCONFIGDIR. The right panel is a schematic
normal form, not fitted data from the magnetic layer.
"""
import os
import tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp(prefix='paper-68-mpl-')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), dpi=100, facecolor='white')
a = np.linspace(0.27, 2.3, 1200) * np.pi
s = a*a + np.pi**2
for Q, color in [(0, '#2c7bb6'), (100, '#d98b00'), (1000, '#7b3294')]:
    R = s*(s*s + Q*np.pi**2)/(a*a)
    label = f'Q = {Q}'
    axes[0].plot(a/np.pi, R/np.pi**4, color=color, label=label)
    j = np.argmin(R)
    axes[0].plot(a[j]/np.pi, R[j]/np.pi**4, 'o', color=color, ms=5)
axes[0].set(xlabel=r'Horizontal wavenumber $a/\pi$', ylabel=r'Steady threshold $R_s/\pi^4$',
            title='Vertical field selects narrower cells', yscale='log', ylim=(5, 1200))
axes[0].legend(frameon=False, loc='upper right')
axes[0].grid(alpha=.2, which='both')

mu = np.linspace(-.25, .45, 1000)
rplus = (1+np.sqrt(1+4*mu))/2
mneg = np.linspace(-.25, 0, 700)
rminus = (1-np.sqrt(1+4*mneg))/2
axes[1].axvspan(-.25, 0, color='#e6f0e2')
axes[1].plot(mu, np.sqrt(rplus), color='#238b45', lw=2, label='Stable finite amplitude')
axes[1].plot(mneg, np.sqrt(rminus), '--', color='#ce5927', lw=2, label='Unstable finite amplitude')
axes[1].plot([-.36, 0], [0, 0], color='#238b45', lw=2)
axes[1].plot([0, .45], [0, 0], '--', color='#ce5927', lw=2)
axes[1].plot(-.25, np.sqrt(.5), 'o', color='#333333', ms=5)
axes[1].text(-.125, .35, 'Bistability', ha='center', fontsize=10)
axes[1].set(xlabel=r'Distance from linear onset $\mu$', ylabel=r'Convective amplitude $|A|$',
            title=r'Schematic: $\dot A=\mu A+|A|^2A-|A|^4A$', xlim=(-.36, .45), ylim=(-.035, 1.25))
axes[1].legend(frameon=False, loc='upper left', fontsize=8)
axes[1].grid(alpha=.2)
fig.tight_layout(pad=1.5)
fig.savefig('paper-68-magnetoconvection.png', facecolor='white', transparent=False)
plt.close(fig)
