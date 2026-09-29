from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,ax=plt.subplots(1,2,figsize=(9,3.7))
x=np.linspace(0,np.pi/2,500)
for q in [1.2,np.pi-np.sqrt(2),3]:
 ax[0].plot(x,q*np.sin(x)*np.cos(x)-2*x+np.sin(x),label=fr'$q={q:.3f}$')
ax[0].axhline(0,color='black',lw=.7);ax[0].set(xlabel=r'Tilt $\theta$ (rad)',ylabel=r'$a\ddot\theta/g$',title=r'For $q=\Omega^2a/g>1$, stable nonzero zero')
ax[0].legend(fontsize=8)
x=np.linspace(-.9,.9,400)
ax[1].plot(x,x*x+np.cos(x)-.5*np.sin(x)**2-1,label='Exact effective potential')
ax[1].plot(x,5*x**4/24,'--',label=r'Quartic approximation $5\theta^4/24$')
ax[1].set(xlabel=r'Tilt $\theta$ (rad)',ylabel=r'$[U(\theta)-U(0)]/(mga)$',title=r'At $q=1$: stable quartic minimum');ax[1].legend(fontsize=8)

fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white',bbox_inches='tight')
plt.close(fig)
