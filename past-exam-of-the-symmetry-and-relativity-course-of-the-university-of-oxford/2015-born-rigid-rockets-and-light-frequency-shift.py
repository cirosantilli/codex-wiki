from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,axs=plt.subplots(1,2,figsize=(11.5,5.8),layout='constrained');ax=axs[0];ell=.8;t=np.linspace(0,4,500);F=np.sqrt(1+t*t);H=np.sqrt((1+ell)**2+t*t)
ax.plot(F,t,color='#174c75',lw=2,label='rear F');ax.plot(H,t,color='#b35b15',lw=2,label='front H')
tr=((1+ell)**2-1)/(2*(1+ell));xr=((1+ell)**2+1)/(2*(1+ell));ax.annotate('',xy=(xr,tr),xytext=(1+ell,0),arrowprops=dict(arrowstyle='->',lw=2,color='black'));ax.scatter([1+ell,xr],[0,tr],color='black',s=24)
eta=.8;xp=np.array([np.cosh(eta),(1+ell)*np.cosh(eta)]);tp=np.array([np.sinh(eta),(1+ell)*np.sinh(eta)]);ax.plot(xp,tp,'--',color='#7b4280',lw=1.6);ax.text(np.mean(xp)+.05,np.mean(tp)+.12,'comoving simultaneity',fontsize=9,color='#7b4280',rotation=27)
ax.plot([0,4],[0,4],':',color='gray',lw=1);ax.set(xlim=(0,4.7),ylim=(-.12,4.2),xlabel='x / a',ylabel='ct / a',title='Illustrative L/a = 0.8');ax.legend(frameon=False,loc='upper left');ax.set_aspect('equal');ax.grid(alpha=.15)
ax=axs[1];l=np.linspace(0,3.5,500);ratio=1+l;velocity=((1+l)**2-1)/((1+l)**2+1);ax.plot(l,ratio,color='#174c75',lw=2,label=r'$\omega_F/\omega_H=1+L/a$');bx=ax.twinx();bx.plot(l,velocity,color='#b35b15',lw=2,ls='--',label='receiver speed / c');ax.set(xlabel='L / a',ylabel='Received / emitted frequency',title='A blueshift at the accelerating rear rocket');bx.set(ylabel='Reception speed / c',ylim=(0,1));ax.grid(alpha=.15);ax.legend(loc='upper left',frameon=False,fontsize=10);bx.legend(loc='lower right',frameon=False,fontsize=10)
fig.suptitle('Born-rigid hyperbolic motion and light transfer between the rockets',fontsize=15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,transparent=False)
