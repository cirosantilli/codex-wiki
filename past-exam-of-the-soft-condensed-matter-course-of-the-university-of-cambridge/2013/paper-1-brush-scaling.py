"""Original scaling curves in the brush regime, not source artwork."""
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.titlesize':11})
x=np.logspace(-3,0,500);fig,axs=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
for ax,q,title in [(axs[0],'height','Brush height'),(axs[1],'fraction','Mean volume fraction')]:
 for nu,col,label in [(.5,'#2166ac',r'$\theta$ solvent'),(.6,'#b2182b','Good solvent')]:
  exponent=(1-nu)/(2*nu) if q=='height' else (3*nu-1)/(2*nu)
  valid=x>=400**(-2*nu);ax.loglog(x[valid],x[valid]**exponent,color=col,lw=2,label=label)
 ax.axvline(1,color='black',ls=':');ax.axhline(1,color='grey',ls=':');ax.set(xlim=(5e-4,2),ylim=(.02,1.5),xlabel=r'$\Sigma=sa^2$',ylabel=r'$H/(Na)$' if q=='height' else r'$\phi$',title=title);ax.legend();ax.grid(alpha=.2)
fig.suptitle(r'Blob scaling for $N=400$; upper boundary $\Sigma\sim1$',fontsize=12)
fig.savefig('paper-1-brush-scaling.png',dpi=170,facecolor='white');plt.close(fig)
