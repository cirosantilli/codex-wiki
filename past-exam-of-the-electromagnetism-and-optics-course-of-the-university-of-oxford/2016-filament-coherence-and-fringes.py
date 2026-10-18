from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size':11,'axes.titlesize':13,'axes.labelsize':12})
fig,(ax,bx)=plt.subplots(1,2,figsize=(10.6,4.3),dpi=125,facecolor='white')
xi=np.linspace(0,3,1201);g=np.sinc(xi)
ax.plot(xi,g,lw=2.5,color='#2268a3',label=r'Signed source factor $g$')
ax.plot(xi,np.abs(g),lw=2,color='#b13939',ls='--',label=r'Physical visibility $|g|$')
ax.axhline(0,color='0.5',lw=.8);ax.plot(.5,2/np.pi,'o',color='#26764e')
ax.annotate(r'$|g|=2/\pi$',xy=(.5,2/np.pi),xytext=(1.1,.72),arrowprops={'arrowstyle':'->','color':'0.3'})
ax.set(xlim=(0,3),ylim=(-.3,1.08),xlabel=r'$\xi=hw/(\lambda R)$',ylabel='Normalized source factor',title='Uniform finite source')
ax.legend(loc='upper right',bbox_to_anchor=(1,.99),fontsize=9,frameon=False)
phi=np.linspace(-2*np.pi,2*np.pi,1201)
for val,c,style in [(0,'#2268a3','-'),(1,'#26764e',':'),(1.5,'#b13939','--')]:
 bx.plot(phi/np.pi,1+np.sinc(val)*np.cos(phi),lw=2,color=c,ls=style,label=fr'$\xi={val:g}$')
bx.set(xlim=(-2,2),ylim=(-.05,2.12),xlabel=r'$\alpha x/\pi$',ylabel=r'$I_x/(2I_0)$',title='Fringe profiles and phase reversal')
bx.legend(loc='upper right',fontsize=10,frameon=True,facecolor='white')
for a in (ax,bx):
 a.set_facecolor('white');a.spines[['top','right']].set_visible(False);a.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
