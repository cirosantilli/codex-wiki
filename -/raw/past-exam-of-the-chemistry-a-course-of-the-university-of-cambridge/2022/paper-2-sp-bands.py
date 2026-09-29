"""Original s/p chain dispersions, with Hermitian odd-in-k mixing."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

u=np.linspace(0,np.pi,601)
fig,axes=plt.subplots(2,2,figsize=(9.2,6.7),layout='constrained')
blue='#245c9f';orange='#b45309'
Es=-3-2*np.cos(u);Ep=3+2*np.cos(u)
axes[0,0].plot(u,Es,color=blue,lw=2,label='$s$');axes[0,0].plot(u,Ep,color=orange,lw=2,label='$p_\\sigma$')
for y in [-3,3]:axes[0,0].axhline(y,color='0.65',ls=':',lw=1)
axes[0,0].set_title('Separated bands: $\\alpha_s=-3$, $\\alpha_p=3$, $t_s=t_p=1$',fontsize=10)
axes[0,0].annotate('',(np.pi,1),(np.pi,-1),arrowprops={'arrowstyle':'<->','color':'0.3'})
axes[0,0].text(np.pi-.1,.1,'$E_g$',ha='right',fontsize=11)
axes[0,0].legend(frameon=False,loc='center left',fontsize=10)
gamma=.65
D=np.sqrt(((Es-Ep)/2)**2+4*gamma**2*np.sin(u)**2)
for y in [Es,Ep]:axes[0,1].plot(u,y,color='0.6',ls='--',lw=1)
axes[0,1].plot(u,(Es+Ep)/2-D,color=blue,lw=2)
axes[0,1].plot(u,(Es+Ep)/2+D,color=orange,lw=2)
axes[0,1].set_title('Separated bands with mixing: $|\\beta_{sp}|=0.65$',fontsize=10)
axes[0,1].text(.08,0,'dashed: unmixed',fontsize=10,color='0.4')
axes[1,0].plot(u,-2*np.cos(u),color=blue,lw=2,label='pure $s$')
axes[1,0].plot(u,2*np.cos(u),color=orange,lw=2,label='pure $p_\\sigma$')
axes[1,0].plot(np.pi/2,0,'ko',ms=4)
axes[1,0].set_title('Equal on-site energies, no mixing: $t=1$',fontsize=11)
axes[1,0].legend(frameon=False,loc='upper right',fontsize=10)
gamma=.35;D=np.sqrt(np.cos(u)**2+gamma**2*np.sin(u)**2)
axes[1,1].plot(u,-2*D,color=blue,lw=2,label='$E_-$')
axes[1,1].plot(u,2*D,color=orange,lw=2,label='$E_+$')
axes[1,1].annotate('',(np.pi/2,2*gamma),(np.pi/2,-2*gamma),arrowprops={'arrowstyle':'<->','color':'0.3'})
axes[1,1].text(np.pi/2+.1,0,'$4\\gamma$',fontsize=11,va='center')
axes[1,1].set_title('Equal on-site energies, mixing: $\\gamma=0.35<t=1$',fontsize=11)
axes[1,1].legend(frameon=False,loc='upper right',fontsize=10)
for i,ax in enumerate(axes.flat):
    ax.set(xlim=(0,np.pi),xlabel='$ka$',ylabel='energy / arbitrary unit')
    ax.set_xticks([0,np.pi/2,np.pi],['$0$','$\\pi/2$','$\\pi$'])
    ax.set_ylim((-5.7,5.7) if i<2 else (-2.5,2.5))
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.14)
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
plt.close(fig)
