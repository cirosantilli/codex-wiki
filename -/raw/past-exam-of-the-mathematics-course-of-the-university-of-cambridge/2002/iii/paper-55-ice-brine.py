"""Original similarity sketches; PNG basename written only to caller CWD.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7. Caller MPLCONFIGDIR unchanged.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

H=1.;eps=.1;C0=2.
F=lambda x:math.sqrt(math.pi)*x*math.exp(x*x)*math.erfc(x)
def values(lb):
    cb=C0/(1-F(lb));la=(lb-math.sqrt(lb*lb+2*cb/(H*eps*eps)))/2
    residual=1-cb-H*(lb-la)*math.sqrt(math.pi)*eps*math.exp((eps*lb)**2)*math.erfc(eps*lb)
    return la,cb,residual
lo,hi=-2.,-.001
for _ in range(100):
    mid=(lo+hi)/2
    if values(mid)[2]>0:lo=mid
    else:hi=mid
lb=(lo+hi)/2;la,cb,_=values(lb);a=eps*la;b=eps*lb
x=np.unique(np.r_[np.linspace(-.8,2.1,900),np.linspace(b-.08,b+.25,400),a,b])
T=np.empty_like(x);C=np.zeros_like(x)
for i,z in enumerate(x):
    if z<a:T[i]=0
    elif z<b:T[i]=-cb*(z-a)/(b-a)
    else:
        T[i]=-1+(1-cb)*math.erfc(z)/math.erfc(b)
        C[i]=C0+(cb-C0)*math.erfc(z/eps)/math.erfc(lb)
TL=-C
fig,axes=plt.subplots(1,3,figsize=(11,4),dpi=120,facecolor='white')
for ax in axes:ax.set_facecolor('white');ax.grid(alpha=.16)
axes[0].plot(x,T,lw=2,color='#1c5c9b',label='Temperature')
axes[0].plot(x,TL,'--',lw=1.6,color='#a53e35',label='Local liquidus')
axes[1].plot(x[x<b],C[x<b],lw=2,color='#30734b')
axes[1].plot(x[x>=b],C[x>=b],lw=2,color='#30734b')
axes[1].plot([b,b],[0,cb],':',lw=1.8,color='#30734b')
for ax in axes[:2]:
    ax.axvspan(a,b,color='#e2f0f8',zorder=0)
    ax.axvline(a,color='#666666',lw=.8);ax.axvline(b,color='#666666',lw=.8)
    ax.set_xlabel(r'$z/(2\sqrt{\kappa t})$')
    ax.text(a,.96,'a',transform=ax.get_xaxis_transform(),ha='center',va='top',fontsize=9,bbox={'facecolor':'white','edgecolor':'none','alpha':.8})
    ax.text(b,.96,'b',transform=ax.get_xaxis_transform(),ha='center',va='top',fontsize=9,bbox={'facecolor':'white','edgecolor':'none','alpha':.8})
axes[0].set_ylabel(r'$(T-T_m)/(T_m-T_\infty)$')
axes[0].set_title('Thermal and liquidus profiles')
axes[0].legend(fontsize=8,frameon=False,loc='lower left')
axes[1].set(title='Salt-free ice and diluted brine',ylabel=r'$mC/(T_m-T_\infty)$',ylim=(-.05,2.15))
caxis=np.linspace(0,2.15,200)
axes[2].plot(caxis,-caxis,'--',lw=1.6,color='#a53e35',label='Liquidus')
salt=x>=b
axes[2].plot(C[salt],T[salt],lw=2,color='#1c5c9b',label='Brine path')
axes[2].plot([0,0],[-cb,0],lw=3,color='#6ca9cc',label='Pure ice')
axes[2].plot([0,cb],[-cb,-cb],':',color='#666666',label='Interface tie-line')
axes[2].scatter([cb,2],[-cb,-1],s=25,color='#1c5c9b')
axes[2].annotate('Interface',xy=(cb,-cb),xytext=(.7,-.25),arrowprops={'arrowstyle':'->'},fontsize=8)
axes[2].annotate('Far brine',xy=(2,-1),xytext=(1.3,-.65),arrowprops={'arrowstyle':'->'},fontsize=8)
axes[2].set(title='Temperature–concentration path',xlabel=r'$mC/(T_m-T_\infty)$',ylabel=r'$(T-T_m)/(T_m-T_\infty)$')
axes[2].legend(fontsize=7.5,frameon=False,loc='lower left')
fig.suptitle(r'Ice between freshwater and cold brine: $\epsilon=0.1$, $S=1$, $mC_0/\Delta T=2$',fontsize=12)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-55-ice-brine.png',facecolor='white',transparent=False)
plt.close(fig)
