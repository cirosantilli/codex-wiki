"""Steady accretion-disk profiles; Python 3.14.4, matplotlib 3.10.7, numpy 2.3.5.

Write an opaque 840 x 380 PNG to CWD for the existing shared Makefile rule.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
x=np.geomspace(1,64,600)
fig,axes=plt.subplots(1,2,figsize=(8.4,3.8),dpi=100,facecolor='white')
for ax,lam in zip(axes,[.01,30.]):
    y=1+(lam-1)/np.sqrt(x)
    ax.plot(x,y,lw=2.1,color='#24598b',label='Total surface density')
    ax.axhline(1,color='#777777',ls=':',lw=1.1,label='Large-radius limit')
    if lam>1:ax.plot(x,(lam-1)/np.sqrt(x),color='#b75b30',ls='--',lw=1.5,label='Inner-torque contribution')
    ax.set(xscale='log',xlim=(1,64),ylim=(0,1.12 if lam<1 else 32),xlabel=r'$r/r_{\mathrm{in}}$',title=r'$\lambda='+str(lam)+r'$')
    ax.set_xticks([1,4,16,64]);ax.xaxis.set_major_formatter(ScalarFormatter())
    ax.grid(alpha=.15)
    ax.legend(fontsize=8,loc='lower right' if lam<1 else 'upper right')
axes[0].set_ylabel(r'$3\pi\bar\nu\Sigma/\dot M$')
axes[1].set_ylabel(r'$3\pi\bar\nu\Sigma/\dot M$')
fig.subplots_adjust(left=.085,right=.98,bottom=.17,top=.88,wspace=.33)
fig.savefig(Path.cwd()/'paper-321-surface-density.png',facecolor='white',transparent=False)
plt.close(fig)
