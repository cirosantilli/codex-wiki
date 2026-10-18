"""Dimensionless ceiling-constrained projectile range; output one PNG to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':10,'axes.titlesize':12,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,axes=plt.subplots(1,2,figsize=(10.2,3.9),layout='constrained')
x=np.linspace(0,1,501);h=.1;theta=np.arcsin(np.sqrt(2*h));R=np.sqrt(8*h*(1-2*h));xx=np.linspace(0,R,400)
ax=axes[0];ax.axhspan(h,.31,color='#f5d0bb',alpha=.7);ax.axhline(h,color='#ab4e25',linestyle=':',label='Roof')
ax.plot(x,x-x*x,color='#888888',linestyle='--',label=r'$45^\circ$: crosses roof');ax.plot(xx,xx*np.tan(theta)-xx*xx/(2*np.cos(theta)**2),color='#176a9e',linewidth=2.3,label='Ceiling-limited optimum')
ax.scatter([0,R],[0,0],s=20,color='#176a9e');ax.set(xlabel=r'$gx/u^2$',ylabel=r'$gy/u^2$',title=r'Low roof: $gH/u^2=0.1$',xlim=(-.015,1.02),ylim=(-.012,.31));ax.legend(loc='upper right',fontsize=8);ax.grid(alpha=.18)
ax=axes[1];hh=np.linspace(0,.65,600);rr=np.where(hh<=.25,np.sqrt(np.maximum(0,8*hh*(1-2*hh))),1)
ax.plot(hh,rr,color='#176a9e',linewidth=2.5,label='Actual maximum');wrong=np.linspace(.25,.5,200);ax.plot(wrong,np.sqrt(8*wrong*(1-2*wrong)),color='#ab4e25',linestyle='--',label='Continuing low-roof formula')
ax.axvline(.25,color='#777777',linestyle=':',linewidth=1);ax.scatter([.25],[1],s=24,color='#176a9e');ax.set(xlabel=r'Ceiling height $gH/u^2$',ylabel=r'Maximum range $gR_{\max}/u^2$',title='A high roof ceases to constrain the launch',xlim=(0,.65),ylim=(0,1.12));ax.legend(loc='lower right',fontsize=8);ax.grid(alpha=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'});plt.close(fig)
