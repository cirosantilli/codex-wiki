"""Original Argand sketches of three complex root sets; save only to cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,3,figsize=(12,4.7),dpi=150,facecolor='white')
for ax in axes:
 ax.set_facecolor('white');ax.axhline(0,lw=.7,color='#888888');ax.axvline(0,lw=.7,color='#888888');ax.set_aspect('equal');ax.set_xlabel('Re z');ax.set_ylabel('Im z');ax.grid(alpha=.15)
theta=np.linspace(0,2*np.pi,500)
ax=axes[0];r=2**.2;roots=r*np.exp(1j*(np.pi/15+2*np.pi*np.arange(5)/5))
ax.plot(r*np.cos(theta),r*np.sin(theta),ls=':',color='#777777')
ax.scatter(roots.real,roots.imag,color='#19678b',s=40,zorder=4)
for k,z in enumerate(roots):ax.annotate(str(k),(z.real,z.imag),xytext=(5,5),textcoords='offset points',fontsize=10)
ax.set(xlim=(-1.45,1.45),ylim=(-1.45,1.45));ax.set_title(r'$z^5=1+i\sqrt{3}$',fontsize=13)
ax.text(.5,-.3,r'$r=2^{1/5}$, five equally spaced roots',ha='center',fontsize=10,transform=ax.transAxes)
ax=axes[1];ang=np.log(2);direction=np.exp(1j*ang);rad=np.exp(-np.pi/4)
ax.plot([0,.7*direction.real],[0,.7*direction.imag],color='#007c83',lw=1.4)
ax.scatter([rad*direction.real],[rad*direction.imag],color='#007c83',s=40,zorder=4)
small=np.exp(-np.pi/4-2*np.pi)*direction;ax.scatter([0],[0],facecolor='white',edgecolor='#007c83',s=25,zorder=5)
ax.annotate('$k=0$',(rad*direction.real,rad*direction.imag),xytext=(-1,12),textcoords='offset points',fontsize=11)
ax.annotate(r'$k\geq1$: approach zero', (small.real,small.imag),xytext=(.04,.14),arrowprops=dict(arrowstyle='->',lw=.8),fontsize=9)
ax.annotate('$k<0$: farther out',xy=(.62*direction.real,.62*direction.imag),xytext=(.05,.61),arrowprops=dict(arrowstyle='->',lw=.8),fontsize=9)
ax.set(xlim=(-.1,.7),ylim=(-.1,.7));ax.set_title(r'$[\sqrt{2}(1+i)]^i$',fontsize=13)
ax.text(.5,-.3,r'$r_k=e^{-\pi/4-2\pi k}$, angle $\ln2$',ha='center',fontsize=10,transform=ax.transAxes)
ax=axes[2];ax.plot(np.cos(theta),np.sin(theta),color='#b54831',lw=2)
ax.scatter([-1],[0],s=65,facecolor='white',edgecolor='#b54831',lw=2,zorder=5)
ax.annotate('excluded',(-1,0),xytext=(-.95,.43),arrowprops=dict(arrowstyle='->',lw=.8),fontsize=10)
ax.set(xlim=(-1.45,1.45),ylim=(-1.45,1.45));ax.set_title(r'$\mathrm{Re}[(z-1)/(z+1)]=0$',fontsize=12)
ax.text(.5,-.3,r'$|z|=1$, except $z=-1$',ha='center',fontsize=10,transform=ax.transAxes)
fig.subplots_adjust(left=.06,right=.985,bottom=.25,top=.87,wspace=.42)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,facecolor='white')
