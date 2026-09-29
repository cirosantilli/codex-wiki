"""Complex loci, Gaussian ODE graph, and trochoids; original illustrations."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(2,2,figsize=(10,8.2),layout='constrained')
ax=axes[0,0];theta=np.linspace(0,2*np.pi,600);roots=3*np.exp(2j*np.pi*np.arange(3)/3);ax.plot(3*np.cos(theta),3*np.sin(theta),ls='--',color='.6');ax.scatter(roots.real,roots.imag,color='#176ca6',s=55,zorder=5);ax.set(title=r'Three roots of $z^3=27$',xlabel='Re z',ylabel='Im z',aspect='equal',xlim=(-3.6,3.6),ylim=(-3.6,3.6))
ax=axes[0,1];x=np.linspace(-1.8,3.8,500);ax.plot(x,(x-1)**2+2,color='#176ca6',lw=2);ax.scatter([1],[2],color='black');ax.annotate('vertex (1, 2)',(1,2),xytext=(1.35,4),arrowprops=dict(arrowstyle='-',color='.4'));ax.set(title=r'$y=(x-1)^2+2$',xlabel='Re z = x',ylabel='Im z = y',ylim=(0,11))
ax=axes[1,0];x=np.linspace(-3,5,500);ax.plot(x,1+np.exp(-(x-1)**2/2),color='#176ca6',lw=2);ax.axhline(1,color='.5',ls='--');ax.scatter([1],[2],color='black');ax.set(title=r'$y=1+e^{-(x-1)^2/2}$',xlabel='x',ylabel='y',ylim=(.85,2.15))
ax=axes[1,1];theta=np.linspace(0,2*np.pi,900);alpha=np.deg2rad(20)
for ratio,color in [(.6,'#29915e'),(1.,'#176ca6'),(1.4,'#bb4b27')]:ax.plot(theta*np.cos(alpha)+ratio*np.sin(theta),-theta*np.sin(alpha)+ratio*np.cos(theta),label=f'a/r = {ratio:g}',color=color,lw=1.8)
ang=2*np.pi-np.arccos(-np.cos(alpha)/1.4);xp=ang*np.cos(alpha)+1.4*np.sin(ang);yp=-ang*np.sin(alpha)+1.4*np.cos(ang);ax.annotate('',xy=(xp,yp+.45),xytext=(xp,yp),arrowprops=dict(arrowstyle='->',lw=2,color='#bb4b27'))
ax.set(title='Downhill rolling, inclination 20°',xlabel='x/r',ylabel='y/r');ax.legend(fontsize=8)
for ax in axes.flat:ax.axhline(0,color='.7',lw=.5);ax.axvline(0,color='.7',lw=.5);ax.grid(alpha=.13)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
