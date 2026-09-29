"""Render a clamped SH-mode sketch to a PNG basename in the current directory.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
import os
from pathlib import Path
os.environ.setdefault('MPLCONFIGDIR', str(Path.cwd() / '.matplotlib-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(.035,5,900)
fig,axes=plt.subplots(1,3,figsize=(10.5,4.2),dpi=100,facecolor='white',layout='constrained')
axes[0].plot(x,np.sqrt(1+x*x),color='#204b9b',lw=2.5)
axes[0].plot(x,x,color='0.55',ls='--',lw=1)
axes[0].scatter([0],[1],color='#204b9b',zorder=3)
axes[0].set(xlabel=r'$k/q_n$',ylabel=r'$\omega/(c_s q_n)$',title='Dispersion and cutoff',xlim=(0,5),ylim=(0,5.3))
axes[1].plot(x,np.sqrt(1+x*x)/x,color='#b43c31',lw=2.5)
axes[1].set(xlabel=r'$k/q_n$',ylabel=r'$c/c_s$',title='Phase velocity',xlim=(0,5),ylim=(.85,4))
axes[2].plot(x,x/np.sqrt(1+x*x),color='#177449',lw=2.5)
axes[2].set(xlabel=r'$k/q_n$',ylabel=r'$c_g/c_s$',title='Group velocity',xlim=(0,5),ylim=(0,1.1))
for ax in axes:
 ax.set_facecolor('white');ax.grid(alpha=.2)
for ax in axes[1:]:ax.axhline(1,color='0.5',ls='--',lw=1)
fig.suptitle('Clamped shear-horizontal waveguide: one transverse mode',fontsize=13)
fig.savefig('paper-2-sh-waveguide.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
