"""Original local Hopf sketches; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
Writes basename to caller CWD and leaves MPLCONFIGDIR unchanged.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axes=plt.subplots(1,5,figsize=(11,2.9),facecolor='white')
x=np.linspace(-1,1,80);X,Y=np.meshgrid(x,x);rr=X*X+Y*Y
cases=[(-.3,1,'(i) attracting origin'),(.3,1,'(ii) stable cycle'),(-.3,-1,'(iii) unstable cycle'),(.3,-1,'(iv) repelling origin')]
for ax,(mu,a,title) in zip(axes,cases):
    U=(mu-a*rr)*X-Y;V=(mu-a*rr)*Y+X
    ax.streamplot(x,x,U,V,density=.65,linewidth=.55,arrowsize=.7,color='#6d8796')
    if mu/a>0:
        t=np.linspace(0,2*np.pi,250);R=np.sqrt(mu/a)
        ax.plot(R*np.cos(t),R*np.sin(t),'-' if mu>0 else '--',color='#ad4737',lw=2)
    ax.plot(0,0,'o',color='black' if mu<0 else 'white',markeredgecolor='black')
    ax.set_aspect('equal');ax.set_xticks([]);ax.set_yticks([]);ax.set_title(title,fontsize=9)
ax=axes[4];mu=np.linspace(-.5,0,200);ax.plot(mu,np.sqrt(-mu),'--',color='#ad4737');ax.axhline(0,color='gray');ax.axvline(0,color='gray');ax.set_xlim(-.52,.2);ax.set_ylim(-.04,.82);ax.set_xlabel(r'$\mu$');ax.set_ylabel(r'$R$');ax.set_title('Subcritical branch',fontsize=9)
fig.tight_layout();fig.savefig(Path('paper-2-hopf.png'),dpi=150,facecolor='white',transparent=False);plt.close(fig)
