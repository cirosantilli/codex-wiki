from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle
plt.rcParams.update({'font.size':13,'axes.titlesize':14,'figure.facecolor':'white','axes.facecolor':'white'})
ratio=6.295;ecc=(ratio-1)/(ratio+1);p=2*ratio/(ratio+1);th=np.linspace(0,np.pi,500);rr=p/(1+ecc*np.cos(th))
fig,axs=plt.subplots(1,2,figsize=(12,5.8),layout='constrained');ax=axs[0]
for rad in [1,ratio]:ax.add_patch(Circle((0,0),rad,fill=False,color='.65',lw=1.1))
ax.plot(rr*np.cos(th),rr*np.sin(th),lw=2.5,color='#0072B2',label='Hohmann coast');ax.scatter(0,0,c='#c4a000',s=65,label='planet (not to scale)')
ax.scatter([1,-ratio],[0,0],c='#D55E00',s=45,zorder=5)
ax.annotate('first prograde burn',xy=(1,0),xytext=(.4,-2.5),arrowprops={'arrowstyle':'->','color':'#D55E00'},color='#D55E00',fontsize=11)
ax.annotate('second prograde burn',xy=(-ratio,0),xytext=(-6.2,-3.7),arrowprops={'arrowstyle':'->','color':'#D55E00'},color='#D55E00',fontsize=11)
ax.set(xlim=(-7,7),ylim=(-7,7),aspect='equal',xlabel=r'$x/r_0$',ylabel=r'$y/r_0$');ax.legend(loc='upper right',fontsize=10);ax.set_title('Two circular orbits and their tangent transfer ellipse');ax.grid(alpha=.15)
ax=axs[1];eta=np.geomspace(1,100,600);h=np.sqrt(2*eta/(1+eta))-1+(1-np.sqrt(2/(1+eta)))/np.sqrt(eta);slow=1-1/np.sqrt(eta)
ax.semilogx(eta,h,lw=2.4,label='Hohmann total',color='#0072B2');ax.semilogx(eta,slow,lw=2.4,label='slow circular spiral',color='#D55E00');ax.axhline(np.sqrt(2)-1,color='.4',ls='--',label='one-burn escape');ax.axvline(ratio,color='.75',lw=1);ax.set(xlabel=r'outer / inner radius $r_1/r_0$',ylabel=r'total impulse per mass / $\sqrt{GM/r_0}$',ylim=(0,1.02));ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=11);ax.set_title('Hohmann costs less than a slow circular spiral')
fig.suptitle('Constant satellite mass, coplanar prograde orbits; escape has no final circularization burn',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white');plt.close(fig)
