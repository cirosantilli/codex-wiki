"""Original matched modes of a string with two densities. Python 3.14, NumPy, Matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(3,1,figsize=(10,6.5),layout='constrained');x1=np.linspace(0,1,401);x2=np.linspace(1,4,1201)
for ax,q,title in zip(axs,[np.pi/3,2*np.pi/3,4*np.pi/3],[r'$k_1L=\pi/3$',r'$k_1L=2\pi/3$',r'$k_1L=4\pi/3$']):
 a=np.cos(q);b=np.sin(q);y1=a*np.sin(q*x1);y2=b*np.cos(q/3*(4-x2));scale=max(np.max(np.abs(y1)),np.max(np.abs(y2)));sgn=np.sign(a);y1*=sgn/scale;y2*=sgn/scale
 ax.plot(x1,y1,lw=2,label=r'dense: $\mu$');ax.plot(x2,y2,lw=2,label=r'light: $\mu/9$');ax.axvline(1,color='.5',ls='--',lw=1);ax.axhline(0,color='.75',lw=.8);ax.plot(0,0,'o',color='black',ms=4);ax.plot(4,y2[-1],'o',mfc='white',mec='black',ms=6)
 ax.set(xlim=(-.05,4.05),ylim=(-1.2,1.2),ylabel='mode shape',title=title);ax.legend(fontsize=9,loc='lower left',ncol=2)
axs[-1].set_xlabel(r'position $x/L$');fig.suptitle('Density junction at x/L = 1; fixed left end and free right end',fontsize=12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False);plt.close(fig)
