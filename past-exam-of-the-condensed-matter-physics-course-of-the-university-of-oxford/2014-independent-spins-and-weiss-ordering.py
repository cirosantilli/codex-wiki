"""Original spin-response curves; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axs=plt.subplots(1,2,figsize=(12.1,4.7),layout='constrained',facecolor='white');x=np.linspace(-3,3,600)
a=axs[0];a.plot(x,np.tanh(x),color='#2563eb',lw=2.5,label=r'$M/(N\mu_B)=\tanh x$');a.plot(x,x,color='#dc2626',ls='--',lw=1.7,label=r'Weak-field $M/(N\mu_B)\simeq x$');a.axhline(0,color='#94a3b8',lw=1);a.axvline(0,color='#94a3b8',lw=1);a.set(xlabel=r'$x=\mu_B B/(k_B T)$',ylabel='Normalized magnetization',xlim=(-3,3),ylim=(-1.2,1.2),title='Independent spin-one-half moments');a.legend(fontsize=9);a.grid(alpha=.2)
t=np.linspace(.02,.9999,500);m=np.empty_like(t)
for j,tt in enumerate(t):
 low=1e-12;high=1.
 for _ in range(60):
  mid=(low+high)/2
  if np.tanh(mid/tt)-mid>0:low=mid
  else:high=mid
 m[j]=(low+high)/2
b=axs[1];b.plot(t,m,color='#2563eb',lw=2.5,label='Positive spontaneous branch');b.plot([0,1],[0,0],color='#94a3b8',ls='--',lw=1.5,label='Zero solution (unstable below 1)');b.plot([1,1.4],[0,0],color='#2563eb',lw=2.5);b.axvline(1,color='#dc2626',ls=':',lw=1.5);b.set(xlabel=r'Reduced temperature $t=T/T_C$',ylabel=r'$m=M/(N\mu_B)$',xlim=(0,1.4),ylim=(-.05,1.05),title=r'One-domain model: $m=\tanh(m/t)$');b.legend(fontsize=9,loc='center left');b.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
