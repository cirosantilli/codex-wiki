"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3; writes basename PNG to cwd, normally the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(7.5,3.5));x=np.linspace(-3,3,401);u=np.pi**(-.25)*np.exp(-x*x/2);v=np.sqrt(2)*x*u;direct=u[:,None]*v[None,:];exchange=v[:,None]*u[None,:];dens=[abs((direct+exchange)/np.sqrt(2))**2,abs((direct-exchange)/np.sqrt(2))**2];top=max(d.max() for d in dens)
for ax,d,t in zip(axs,dens,['Symmetric spatial state','Antisymmetric spatial state']):
 im=ax.imshow(d.T,origin='lower',extent=(-3,3,-3,3),cmap='Blues',vmin=0,vmax=top);ax.plot([-3,3],[-3,3],ls=':',lw=1,color='#b27735');ax.set(xlabel='Particle coordinate x1',ylabel='Particle coordinate x2',title=t)
fig.colorbar(im,ax=axs.ravel().tolist(),shrink=.8,label='Joint probability density');fig.subplots_adjust(wspace=.3,right=.85)

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
