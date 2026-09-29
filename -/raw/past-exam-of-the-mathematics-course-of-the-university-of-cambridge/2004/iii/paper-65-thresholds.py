"""Derived alpha-squared Omega marginal curves. Python 3.14/numpy 2.3.5/matplotlib 3.10.7.
Output: paper-65-thresholds.png in caller CWD only. Preserves supplied MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

k=np.linspace(-3,3,1501)
fig,axs=plt.subplots(1,2,figsize=(11,5),sharey=True,layout='constrained')
for ax,omega in zip(axs,[1.,8.]):
    p=1+k*k
    alpha=2*p*p/np.sqrt(4*p**3+omega**2*k*k)
    ax.plot(k,alpha,color='#216c9e',lw=2.2,label='Marginal |α|')
    ax.set(xlim=(-3,3),ylim=(.35,3.3),xlabel='k / |ℓ|',title=f'|Ω| / (ηℓ²) = {omega:g}   (critical value = 2)')
    ax.grid(alpha=.2)
    if omega<2:
        ax.scatter([0],[1],color='#a34721',s=35,zorder=4)
        ax.annotate('Minimum at k = 0',(0,1),xytext=(20,23),textcoords='offset points',fontsize=10,arrowprops={'arrowstyle':'-'})
    else:
        lo,hi=0.,1/3
        for _ in range(80):
            x=(lo+hi)/2
            F=4*(1+x)**3+omega**2*(3*x-1)
            if F<0:lo=x
            else:hi=x
        kc=np.sqrt((lo+hi)/2)
        pp=1+kc*kc
        amin=2*pp*pp/np.sqrt(4*pp**3+omega**2*kc*kc)
        ax.scatter([-kc,kc],[amin,amin],color='#a34721',s=35,zorder=4)
        ax.scatter([0],[1],facecolors='white',edgecolors='#216c9e',s=35,zorder=4)
        ax.vlines([-kc,kc],.35,amin,colors='#a34721',linestyles=':',lw=1.1)
        ax.text(-kc,.38,r'$-k_c$',ha='center',va='bottom',fontsize=10)
        ax.text(kc,.38,r'$+k_c$',ha='center',va='bottom',fontsize=10)
        ax.annotate('Central local maximum',(0,1),xytext=(22,30),textcoords='offset points',fontsize=9,arrowprops={'arrowstyle':'-'})
    ax.legend(loc='upper center',fontsize=9)
axs[0].set_ylabel('Marginal |α| / (η|ℓ|)')
fig.suptitle('Threshold curves from the full alpha-squared Omega dispersion relation')
fig.savefig(Path.cwd()/'paper-65-thresholds.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
