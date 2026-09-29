"""Chosen phenomenological conductivities, not experimental data or a microscopic model."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

f=np.linspace(1.05,5.95,2800)
t=np.tanh((f[:,None]-(np.arange(1,6)+.5))/.06)
k=1+.5*(1+t).sum(axis=1)
s=.08*(1-t*t).sum(axis=1)
rh=k/(s*s+k*k)
rxx=s/(s*s+k*k)
assert np.all(s>=0) and np.all(np.diff(k)>=0)
fig,(a,b)=plt.subplots(2,1,figsize=(10.4,7.4),sharex=True,gridspec_kw={'height_ratios':[1.6,1]})
fig.patch.set_facecolor('white')
fig.suptitle('A chosen Hall staircase and its longitudinal response',fontsize=17,y=.975)
a.plot(f,rh,lw=2.5,color='#245c8d',label=r'$|\rho_{yx}|/R_K=k/(s^2+k^2)$')
a.plot(f,1/f,'--',lw=1.6,color='#8b5e36',label=r'Classical comparison $1/f$')
for n in range(1,7):
    x=min(max(n,1.17),5.8)
    a.text(x,1/n+.035,f'N = {n}',fontsize=11,ha='center',color='#245c8d')
a.set(ylabel='Hall sheet resistivity / $R_K$',ylim=(.1,1.16))
a.legend(loc='upper right',fontsize=11,framealpha=1)
b.plot(f,rxx,lw=2.2,color='#a62d48')
b.set(xlabel=r'Continuous nominal filling factor $f=n_s h/(eB)$',ylabel=r'$\rho_{xx}/R_K$',ylim=(-.002,.041),xlim=(1.05,5.95),xticks=np.arange(1.5,6,.5))
for ax in [a,b]:
    ax.grid(alpha=.2)
    ax.tick_params(labelsize=11)
    ax.yaxis.label.set_size(12)
b.xaxis.label.set_size(12)
fig.text(.5,.035,'Stipulated smooth steps, width 0.06 and peak scale 0.08; one resolved branch per step.\nOriginal interpolation, not a historical spectrum, fit or localization calculation.',ha='center',fontsize=11,linespacing=1.45,color='#444')
fig.subplots_adjust(left=.115,right=.97,top=.9,bottom=.18,hspace=.12)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
plt.close(fig)
