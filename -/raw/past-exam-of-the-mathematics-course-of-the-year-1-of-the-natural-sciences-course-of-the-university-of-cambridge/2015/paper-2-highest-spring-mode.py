"""Original highest spring mode; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

The PNG is saved to cwd, normally the mirrored _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

s=np.linspace(0,2,700)
curves=[np.cos(2*np.pi*s),-np.sqrt(2)*np.cos(2*np.pi*s),np.cos(2*np.pi*s)]
fig,axes=plt.subplots(3,1,figsize=(6.6,5.0),sharex=True,sharey=True,layout='constrained',facecolor='white')
for i,(ax,v,color) in enumerate(zip(axes,curves,['#0072b2','#d55e00','#009e73']),1):
    ax.plot(s,v,color=color,lw=2)
    ax.axhline(0,color='#777777',lw=.7)
    ax.set(ylabel=rf'$x_{i}/(A/2)$',ylim=(-1.6,1.6))
    ax.grid(alpha=.16)
axes[-1].set_xlabel(r'$t/(2\pi/\omega_3)$')
axes[0].set_title(r'Highest mode: outer masses together, middle mass opposite')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
