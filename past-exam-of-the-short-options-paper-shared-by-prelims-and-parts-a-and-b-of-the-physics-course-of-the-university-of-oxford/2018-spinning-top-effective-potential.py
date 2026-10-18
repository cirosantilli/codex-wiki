from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})

fig,axes=plt.subplots(1,2,figsize=(9,4.8),layout='constrained')
theta=np.linspace(0,np.pi-.025,1000)
for ax,alpha in zip(axes,[.5,2.]):
 v=np.tan(theta/2)**2-alpha*np.sin(theta/2)**2
 ax.plot(theta,v,color='#16659c',lw=2.5);ax.axhline(0,color='#777777',lw=1)
 ax.set(xlim=(0,np.pi),ylim=(-.3,2.2),xlabel=r'Polar tilt $\theta$',ylabel=r'$V(\theta)/C^2$',title=rf'$\alpha={alpha:g}$')
 ax.set_xticks([0,np.pi/2,np.pi],[r'$0$',r'$\pi/2$',r'$\pi$']);ax.grid(alpha=.2)
axes[0].text(.2,1.5,'Stable vertical orientation\nSmall signed-tilt oscillations',fontsize=10)
alpha=2.;tm=2*np.arccos(alpha**(-.25));vm=-(np.sqrt(alpha)-1)**2;tzero=2*np.arccos(alpha**(-.5))
axes[1].scatter([tm,tzero],[vm,0],color=['#11703e','#b22428'])
axes[1].annotate('Off-axis minimum',(tm,vm),(.2,.45),arrowprops={'arrowstyle':'->'},fontsize=10)
axes[1].annotate('Zero-energy\nouter turn',(tzero,0),(1.8,.65),arrowprops={'arrowstyle':'->'},fontsize=10)
axes[1].text(.2,1.5,'Unstable vertical orientation\nNear-pole delay diverges',fontsize=10)
fig.suptitle(r'Effective top potential, $C=I_3\omega/I_1$',fontsize=13)

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white', transparent=False)
plt.close(fig)
