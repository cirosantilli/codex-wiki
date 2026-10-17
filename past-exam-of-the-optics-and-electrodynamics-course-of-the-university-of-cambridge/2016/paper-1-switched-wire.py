#!/usr/bin/env python3
"""Original educational diagram. Tested with Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run from the corresponding mirrored _media directory; writes a PNG basename to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})

u=np.r_[np.linspace(0,.999,200),np.geomspace(.002,5,1500)+1];valid=u>1;E=np.zeros_like(u);H=E.copy();N=E.copy();E[valid]=-1/np.sqrt(u[valid]**2-1);H[valid]=u[valid]/np.sqrt(u[valid]**2-1);N[valid]=u[valid]/(u[valid]**2-1)
fig,axs=plt.subplots(1,3,figsize=(10,3.2))
for ax,y,label,lim in zip(axs,[E,H,N],['Ez / E*','Hphi / H*','Nr / N*'],[(-5,.4),(-.2,5),(-.2,5)]):
 ax.plot(u[~valid],y[~valid],color='#12669b');ax.plot(u[valid],y[valid],color='#12669b');ax.axvline(1,color='#b36b16',ls='--',label='Causal front');ax.set(xlim=(0,6),ylim=lim,xlabel='u = ct / r',ylabel=label);ax.grid(alpha=.2)
axs[1].axhline(1,color='.5',ls=':',label='Static limit');axs[1].legend(fontsize=8);axs[0].text(1.15,-4.65,'Divergent at front',fontsize=8);axs[2].text(1.2,4.45,'Outward flux',fontsize=9)
fig.suptitle('Fixed-radius fields after an ideal abrupt line-current switch');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight')
