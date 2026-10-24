#!/usr/bin/env python3
"""Original Schwarzschild critical-ray figure. Python3.12, NumPy and matplotlib.
Run from the desired output directory; writes the matching PNG in the CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(10,3.9),constrained_layout=True,facecolor='white')
x=np.linspace(2.001,10,1000);v=(1-2/x)/x**2
axes[0].plot(x,v,color='#155e75',lw=2,label='Null radial potential')
axes[0].axhline(1/27,color='#a33b27',ls='--',label='Critical energy')
axes[0].plot(3,1/27,'o',color='#a33b27');axes[0].annotate('Unstable maximum',(3,1/27),xytext=(4.4,.034),arrowprops={'arrowstyle':'->'})
axes[0].set(xlabel=r'$r/m$',ylabel=r'$m^2 V/J^2$',title='Circular photon orbit',ylim=(0,.043));axes[0].legend(loc='lower right',fontsize=8)
phi=np.linspace(-6,2,1000);q=.01*np.exp(phi);u=(1-8*q+4*q*q)/(3*(1+2*q)**2)
axes[1].plot(phi,1/u,color='#155e75',lw=2,label=r'$A=0.01$ outward branch')
axes[1].axhline(3,color='#a33b27',ls='--',label=r'$A=0$: circular orbit')
axes[1].set(xlabel=r'$\phi$',ylabel=r'$r/m$',title='Critical separatrix',ylim=(2.6,10));axes[1].legend(loc='upper left',fontsize=8)
for ax in axes:ax.set_facecolor('white');ax.grid(alpha=.2)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=170,facecolor='white')
