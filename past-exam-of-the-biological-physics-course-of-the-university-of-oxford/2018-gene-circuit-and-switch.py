"""Original model illustration; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,axs=plt.subplots(2,2,figsize=(10,7.5),layout='constrained');t=np.linspace(0,8,1001);h=.25;F=10
for name,y,d,color in [('I1',1-np.exp(-t),-np.log(1-h),'tab:blue'),('I4',np.exp(-t),-np.log(h),'tab:orange')]:
    axs[0,0].plot(t,y,label=name,color=color,lw=2);axs[0,0].plot(d,h,'o',color=color)
    z=np.where(t<=d,F*(1-np.exp(-t)),1+(F*(1-np.exp(-d))-1)*np.exp(-(t-d)))
    axs[0,1].plot(t,z,label=name,color=color,lw=2);axs[0,1].axvline(d,color=color,ls=':',alpha=.6)
axs[0,0].axhline(h,color='.5',ls='--',label='Y threshold 0.25');axs[0,0].set(xlabel=r'time $\alpha t$',ylabel=r'$Y/Y_s$',title='Rise or fall crosses the regulation threshold');axs[0,0].legend(fontsize=9)
axs[0,1].axhline(1,color='.5',ls='--');axs[0,1].set(xlabel=r'time $\alpha t$',ylabel=r'$Z/Z_s$',title='Both graded motifs produce pulses: F = 10');axs[0,1].legend()
for ax,gamma in zip(axs[1],[1.5,3]):
    q=np.linspace(0,gamma+.3,600)
    ax.plot(gamma/(1+q*q),q,label=r'$\dot Y=0$',lw=2);ax.plot(q,gamma/(1+q*q),label=r'$\dot Z=0$',lw=2)
    roots=np.roots([1,0,1,-gamma]);sym=next(x.real for x in roots if abs(x.imag)<1e-8)
    ax.plot(sym,sym,'o',mfc='black' if gamma<2 else 'white',mec='black',ms=8,label='stable' if gamma<2 else 'saddle')
    if gamma>2:
        hi=(gamma+np.sqrt(gamma*gamma-4))/2;lo=1/hi
        ax.plot([hi,lo],[lo,hi],'o',color='black',ms=7,label='stable alternatives')
    ax.set(xlabel='Y (reduced concentration)',ylabel='Z (reduced concentration)',xlim=(0,gamma+.3),ylim=(0,gamma+.3),title=rf'Quadratic Hill repression: $\gamma={gamma:g}$')
    ax.legend(fontsize=8)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
plt.close(fig)
