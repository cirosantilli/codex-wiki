from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':12,'axes.titlesize':13,'figure.facecolor':'white','axes.facecolor':'white'})
fig,axs=plt.subplots(1,3,figsize=(12,4.5),layout='constrained')
for ax in axs:
 ax.axhline(0,color='.5',lw=.8);ax.axvline(0,color='.5',lw=.8);ax.grid(alpha=.2);ax.set_aspect('equal');ax.set_xlabel('real part');ax.set_ylabel('imaginary part')
ax=axs[0];ax.scatter(.25,.5,c='#0072B2',s=65,zorder=4);ax.annotate(r'$1/4+i/2$',xy=(.25,.5),xytext=(.42,.7),arrowprops={'arrowstyle':'->'},fontsize=12);ax.set(xlim=(-.5,1.3),ylim=(-.4,1.4),title=r'$3z+z^*=1+i$')
ax=axs[1];theta=np.linspace(0,2*np.pi,400);ax.plot(np.sqrt(2)*np.cos(theta),np.sqrt(2)*np.sin(theta),'--',c='.6');roots=np.sqrt(2)*np.exp(1j*(np.pi/8+np.arange(4)*np.pi/2));ax.scatter(roots.real,roots.imag,c='#D55E00',s=55,zorder=4)
for k,z in enumerate(roots):ax.text(1.12*z.real,1.12*z.imag,rf'$z_{k}$',ha='center',va='center')
ax.set(xlim=(-2,2),ylim=(-2,2),title=r'$z^4=4i$: four points')
ax=axs[2];y=np.linspace(-3,3,400);ax.plot(1+y*y/4,y,c='#0072B2',lw=2.3);ax.axvline(0,c='#009E73',ls='--',lw=1.5);ax.scatter([1,2],[0,0],c=['#0072B2','#D55E00'],s=45,zorder=4);ax.annotate('vertex',xy=(1,0),xytext=(.3,-1.2),arrowprops={'arrowstyle':'->'},fontsize=11);ax.annotate('focus',xy=(2,0),xytext=(2.1,1.1),arrowprops={'arrowstyle':'->'},fontsize=11);ax.text(.1,2.6,'directrix x=0',color='#009E73',rotation=90,va='top',fontsize=10);ax.set(xlim=(-.4,3.7),ylim=(-3.2,3.2),title=r'$|z-2|=\mathrm{Re}\,z$: parabola')
fig.suptitle('Complex-plane loci: solve both the equations and their real-domain restrictions',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white');plt.close(fig)
