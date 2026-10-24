# Python 3.14.4; numpy 2.3.5; matplotlib 3.10.7. Output in current working directory.
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({'figure.facecolor':'white','axes.facecolor':'white','font.size':10})
n=3
def root(delta):
    lo,hi=0.,max(2.,2/delta)
    for _ in range(80):
        mid=(lo+hi)/2
        if 1/(1+mid**n)>delta*mid:lo=mid
        else:hi=mid
    return (lo+hi)/2
fig,axs=plt.subplots(1,2,figsize=(9,4));u=np.linspace(0,2.5,400);delta=.25;us=root(delta)
axs[0].plot(u,1/(1+u**n),label='production');axs[0].plot(u,delta*u,label='loss');axs[0].plot(us,delta*us,'ko');axs[0].set(xlabel='$u$',ylabel='rate',title='One stable positive intersection');axs[0].legend(fontsize=8)
deltas=np.logspace(-3,3,400);roots=np.array([root(x)for x in deltas]);axs[1].loglog(deltas,roots,'k',lw=2,label=r'$u_*$');axs[1].loglog(deltas,deltas**(-1/(n+1)),'--',label=r'$\delta^{-1/(n+1)}$');axs[1].loglog(deltas,deltas**-1,':',label=r'$\delta^{-1}$');axs[1].set(xlabel=r'$\delta$',ylabel=r'$u_*$',ylim=(5e-4,10),title='Small- and large-loss asymptotes');axs[1].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.2)
fig.suptitle('Red-cell production feedback, representative Hill exponent n=3');fig.tight_layout();fig.savefig(Path('2008-rbc-equilibrium.png'),dpi=150,facecolor='white');plt.close(fig)
