"""Original spatial-gate myosin probability and force; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
x=np.linspace(-.2,7,2001);delta=.1;kon=10.;koff=1.;x0=1.
fig,axs=plt.subplots(1,2,figsize=(10.7,4.3),constrained_layout=True,facecolor='white')
for v,col in [(.2,'#1864ab'),(2.,'#d9480f')]:
 pb=-np.expm1(-kon*delta/v)
 prob=np.where(x<0,0,np.where(x<=delta,-np.expm1(-kon*np.maximum(x,0)/v),np.where(x<=x0,pb,pb*np.exp(-koff*(x-x0)/v))))
 axs[0].plot(x,prob,color=col,lw=2.2,label=fr'$v/(k_{{on}}\Delta x)={v:g}$')
axs[0].axvspan(0,delta,color='.8',alpha=.6)
axs[0].axvline(1,color='.5',ls=':',lw=1)
axs[0].text(.24,.89,'binding\nwindow',ha='left',fontsize=10)
axs[0].annotate(r'$x_0$',xy=(1,0),xytext=(1.17,.13),arrowprops={'arrowstyle':'->','color':'.3'})
axs[0].set(xlabel=r'$x/x_0$',ylabel='Probability bound to the current site',ylim=(-.02,1.05),title='Short capture window, plateau, detachment tail')
axs[0].legend(frameon=False,fontsize=9,loc='upper right')
u=np.linspace(.001,1.2,700);force=(-np.expm1(-1/u))*(.5-u*u)
axs[1].plot(u,force,color='#1864ab',lw=2.2)
axs[1].plot([0],[.5],'o',color='#1864ab');axs[1].axhline(0,color='.5',lw=1)
axs[1].axvline(1/np.sqrt(2),color='.5',lw=1,ls=':')
axs[1].text(.74,.37,r'$v=k_{off}x_0/\sqrt{2}$',fontsize=10)
axs[1].set(xlabel=r'$v/(k_{off}x_0)$',ylabel=r'$\overline{F} D/(\kappa x_0^2)$',title='Mean signed force in the narrow-window limit',xlim=(0,1.2))
for ax in axs:ax.grid(alpha=.15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
