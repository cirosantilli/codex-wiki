"""Original S=1/2 antiferromagnetic mean-field curve; root dependencies only."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def ordered_m(t):
    if t<=0: return 1.
    if t>=1: return 0.
    lo,hi=1e-12,1.
    for _ in range(90):
        m=(lo+hi)/2
        if np.tanh(m/t)>m: lo=m
        else: hi=m
    return (lo+hi)/2

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
t=np.linspace(0,1.2,800)
m=np.array([ordered_m(z) for z in t])
fig,axes=plt.subplots(1,2,figsize=(10,4),layout='constrained')
axes[0].plot(t,m,color='#126782',lw=2.5)
axes[0].set(xlabel=r'$T/T_N$',ylabel=r'$M_A/M_s$',title=r'Example: $S=1/2$, $m=\tanh(mT_N/T)$',xlim=(0,1.2),ylim=(0,1.05))
axes[0].axvline(1,color='.5',ls=':')
x=1-t
mask=(x>=0)&(x<=.12)
axes[1].plot(x[mask],m[mask]**2,lw=2.5,color='#126782',label='Self-consistent solution')
axes[1].plot(x[mask],3*x[mask],ls='--',color='#b3561b',label=r'Critical limit: $m^2=3(1-T/T_N)$')
axes[1].set(xlabel=r'$1-T/T_N$',ylabel=r'$m^2\propto$ magnetic Bragg intensity',title=r'Mean-field exponent $\beta=1/2$',xlim=(0,.12),ylim=(0,.38))
axes[1].legend(fontsize=10,frameon=False)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',transparent=False)
