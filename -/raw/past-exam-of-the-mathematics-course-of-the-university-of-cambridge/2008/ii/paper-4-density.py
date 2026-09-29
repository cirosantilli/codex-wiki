"""Conformal-time density evolution; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Writes paper-4-density.png to the caller's working directory; preserves MPLCONFIGDIR.
"""
import os
import tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR']=tempfile.mkdtemp(prefix='paper-4-density-mpl-')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axs=plt.subplots(1,2,figsize=(9.6,4),layout='constrained',facecolor='white')
t=np.linspace(0,1.5,400)
axs[0].plot(t,1/np.cos(np.pi/6+t/2)**2,label='Initially above 1',color='#ba4d32')
axs[0].plot(t,1/np.cosh(np.pi/6+t/2)**2,label='Initially below 1',color='#246cb4')
axs[0].set_title('Matter: w = 0; flatness is unstable')
t=np.linspace(0,np.pi/4-.004,400)
axs[1].plot(t,1/np.sin(np.pi/4+t)**2,label='Initially above 1',color='#ba4d32')
axs[1].plot(t,1/np.cosh(np.pi/4-t)**2,label='Initially below 1',color='#246cb4')
axs[1].set_title('Inflation: w = -1; approach to flatness')
for ax in axs:
    ax.set_facecolor('white')
    ax.axhline(1,color='#333333',ls='--',label='Flat: density parameter = 1')
    ax.set_xlabel('Conformal time (c = 1; origin chosen independently)')
    ax.set_ylabel('Density parameter')
    ax.grid(alpha=.2)
    ax.legend(fontsize=8)
axs[0].set_ylim(0,4)
axs[1].set_ylim(.4,2.15)
fig.savefig('paper-4-density.png',dpi=150,facecolor='white',transparent=False)
plt.close(fig)
