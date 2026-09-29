"""Ideal equal-arm single-source interferometer; Python 3.14, numpy/matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

wavelength = .025
theta_r = 1.22*wavelength/.85
baseline = wavelength/(2*np.sin(theta_r))
x = np.linspace(-2.1, 2.1, 1401)
theta = theta_r*x
phase = 2*np.pi*baseline*np.sin(theta)/wavelength
fig, ax = plt.subplots(figsize=(8,4.5),dpi=130,facecolor='white')
ax.set_facecolor('white')
ax.plot(x,2*(1+np.sin(phase)),label='A: geometric phase − π/2',color='#1764a4',lw=2)
ax.plot(x,2*(1-np.sin(phase)),label='B: swapped cables, phase + π/2',color='#c2410c',lw=2,ls='--')
ax.axhline(2,color='#777777',lw=.8,ls=':')
ax.set(xlim=(-2.1,2.1),ylim=(-.1,4.18),xlabel=r'Satellite angular offset $\theta/\theta_R$  ($\theta_R=2.056^\circ$)',ylabel=r'Signal strength / single-dish strength $I_0$',title='Swapping unequal cables interchanges maxima and nulls')
ax.set_xticks(np.arange(-2,2.1,.5)); ax.set_yticks(range(5))
ax.grid(alpha=.2); ax.legend(loc='upper center',bbox_to_anchor=(.5,-.20),frameon=False,ncol=1)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
plt.close(fig)
