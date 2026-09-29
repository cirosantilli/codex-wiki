"""Original explanatory figure; Python 3.14 with NumPy and Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(10,4.7),layout='constrained');gamma=1.4;r=3.;rp=3.;v1=1.;v2=1/r;p1=1.;p2=r**gamma;p3=rp*p2;v4p=rp**(1/gamma);v=np.linspace(v2,v4p,800);pex=p3*(v2/v)**gamma
ax=axs[0];vcomp=np.linspace(v2,1,300);ax.plot(vcomp,vcomp**-gamma,color='#427b9f',label='compression adiabat');ax.plot([v2,v2],[p2,p3],color='#a64d45');ax.plot(v,pex,color='#a64d45',label='expansion adiabat');ax.plot([1,1],[rp,1],color='#777777',ls='--',label='Otto heat rejection');ax.plot([1,v4p],[1,1],color='#3f8267',label='Atkinson heat rejection')
for vv,pp,lab in [(1,1,'1'),(v2,p2,'2'),(v2,p3,'3'),(1,rp,'4'),(v4p,1,"4′")]:
 ax.plot(vv,pp,'ko',ms=3);ax.annotate(lab,(vv,pp),xytext=(5,5),textcoords='offset points',fontsize=9)
ax.set(xlim=(.2,2.4),ylim=(0,15.5),xlabel=r'$V/V_1$',ylabel=r'$p/p_1$',title='Ideal cycles with shared compression and heat input');ax.legend(fontsize=8,loc='upper right');ax.grid(alpha=.15)
ax=axs[1];vv=np.linspace(1,v4p,400);pp=rp/vv**gamma;ax.fill_between(vv,1,pp,color='#8bb69d',alpha=.65);ax.plot(vv,pp,color='#a64d45');ax.plot([1,v4p],[1,1],color='#3f8267');ax.plot([1,1],[1,rp],color='#777777',ls='--')
etaO=1-r**(1-gamma);etaA=1-gamma*r**(1-gamma)*(rp**(1/gamma)-1)/(rp-1)
ax.text(1.13,2.6,r'$\Delta W=\int(p_{\rm expansion}-p_1)\,dV>0$',fontsize=10);ax.text(1.1,.25,f'Illustration: ηO = {etaO:.3f}, ηA = {etaA:.3f}',fontsize=10)
ax.set(xlim=(.85,2.4),ylim=(0,3.4),xlabel=r'$V/V_1$',ylabel=r'$p/p_1$',title='Added net work during extended expansion');ax.grid(alpha=.15)
fig.suptitle(r'Illustrative calculation: $r=3$, $r_p=3$, $\gamma=1.4$; no additional exam data')

fig.savefig(Path(__file__).stem+'.png',dpi=150,bbox_inches='tight',facecolor='white');plt.close(fig)
