import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
fig,axes=plt.subplots(1,2,figsize=(9,4.2),dpi=100)
D=np.geomspace(1e-5,1e5,2000);D0=1.;Dp=1e3;Dm=Dp**(-3/5);Ksmall=Dp**(-2/5)
# The low-mass curve is a continuous matched asymptotic illustration.
belt=np.select([D<Dm,D<1,D<Dp],[Ksmall*D**(-3.5),D**(-4.5)/Dp,D**(-2.5)/Dp],default=D**(-3.5))
out=belt/np.where(D<1,1/D,D)
for ax,b,o,title in [(axes[0],D**(-3.5),D**(-3.5)/(D+1/D),'High mass: collisions dominate'),(axes[1],belt,out,'Low mass: depleted intermediate band')]:
 ax.loglog(D,b,color='tab:blue',lw=2,label='Belt')
 ax.loglog(D,o*.03,color='tab:orange',lw=2,label='Removed population (offset)')
 ax.set(xlabel=r'Diameter / $D_0$',ylabel=r'Differential number $n(D)$ (arbitrary units)',title=title,xlim=(1e-5,1e5))
 ax.legend(fontsize=8);ax.grid(alpha=.15)
axes[0].axvline(1,color='gray',ls=':',alpha=.5)
for d,l in [(Dm,r'$D_-$'),(1,r'$D_0$'),(Dp,r'$D_+$')]:
 axes[1].axvline(d,color='gray',ls=':',alpha=.5);axes[1].text(d*1.18,1e-18,l,fontsize=9)
axes[0].text(.00007,1e9,'Belt: -7/2',color='tab:blue',fontsize=9)
axes[0].text(.00005,1e3,'Removed: -5/2',color='tab:orange',fontsize=9)
axes[0].text(15,1e-10,'Removed: -9/2',color='tab:orange',fontsize=9)
for d,y,t in [(1e-4,1e10,'-7/2'),(.08,1e4,'-9/2'),(5,3e-4,'-5/2'),(3e3,1e-10,'-7/2')]:axes[1].text(d,y,t,color='tab:blue',fontsize=9)
for d,y,t in [(1e-4,1e3,'-5/2'),(.04,3e-3,'-7/2'),(2e3,1e-16,'-9/2')]:axes[1].text(d,y,t,color='tab:orange',fontsize=9)
fig.tight_layout();fig.savefig('paper-316-size-distributions.png',facecolor='white',transparent=False)
