"""Hydraulic depth branches; Python 3.14 NumPy/Matplotlib, cwd output."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def depths(x, q, energy=1.):
    b=1+x*x
    if abs(q*q/(2*b*b)-4*energy**3/27)<1e-10:
        return 2*energy/3,2*energy/3
    roots=np.roots([1,-energy,0,q*q/(2*b*b)])
    real=sorted(z.real for z in roots if abs(z.imag)<1e-7 and z.real>0)
    return real[0],real[-1]

x=np.linspace(-2.2,2.2,700)
qc=np.sqrt(8/27)
lo,hi=np.array([depths(v,.8*qc) for v in x]).T
lc,hc=np.array([depths(v,qc) for v in x]).T
fig,axes=plt.subplots(1,3,figsize=(12.3,4.3),dpi=130,facecolor='white',sharey=True)
axes[0].plot(x,hi,label='Entirely subcritical',color='#245b8c')
axes[0].plot(x,lo,label='Entirely supercritical',color='#bd7a1b')
axes[0].set_title('Below critical discharge')
axes[1].plot(x,np.where(x<0,hc,lc),color='#245b8c',label='Accelerating control')
axes[1].plot(x,np.where(x<0,lc,hc),color='#bd7a1b',ls='--',label='Reverse smooth branch')
axes[1].scatter([0],[2/3],color='#245b8c')
axes[1].set_title('Smooth hydraulic control')
bj=np.sqrt(32/27);xj=np.sqrt(bj-1);h1=.5;h2=(np.sqrt(17)-1)/4
e2=h2+qc*qc/(2*bj*bj*h2*h2)
up=np.where(x<0,hc,lc);mask=x<=xj
axes[2].plot(x[mask],up[mask],color='#245b8c')
xx=x[x>=xj];post=np.array([depths(v,qc,e2)[1] for v in xx])
axes[2].plot(xx,post,color='#245b8c',label='Control then jump')
axes[2].plot([xj,xj],[h1,h2],color='#9d3a35',lw=2.4,label='Dissipative jump')
axes[2].set_title('Momentum-conserving jump')
for ax in axes:
    ax.axvline(0,color='#b5bdc3',lw=.8,ls=':')
    ax.set_xlabel(r'$x/L$');ax.set_ylim(0,1.13);ax.legend(fontsize=8,frameon=False)
    ax.spines[['top','right']].set_visible(False)
axes[0].set_ylabel(r'Lower-layer depth $h/H$')
fig.suptitle('Hydraulic branches for width $b=1+(x/L)^2$',fontsize=14)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-76-hydraulic-branches.png',facecolor='white',transparent=False)
plt.close(fig)
