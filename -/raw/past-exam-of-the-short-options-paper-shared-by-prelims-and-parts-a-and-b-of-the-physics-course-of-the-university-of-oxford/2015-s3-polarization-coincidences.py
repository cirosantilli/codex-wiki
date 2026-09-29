"""Original quantum/classical coincidence comparison. Output matching PNG in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

degrees=np.linspace(0,180,241)
a,b=np.meshgrid(np.deg2rad(degrees),np.deg2rad(degrees))
classical=.5*(np.cos(a)**2*np.cos(b)**2+np.sin(a)**2*np.sin(b)**2)
bell=.5*np.cos(a-b)**2
fig,axes=plt.subplots(1,3,figsize=(11,3.6),layout='constrained')
for ax,values,title in zip(axes[:2],[classical,bell],['Equal HH/VV classical mixture',r'Entangled $\Phi^+$ state']):
    im=ax.imshow(values,origin='lower',extent=(0,180,0,180),vmin=0,vmax=.5,cmap='viridis',aspect='equal')
    ax.set(title=title,xlabel=r'$\theta_A$ (degrees)',ylabel=r'$\theta_B$ (degrees)',xticks=[0,90,180],yticks=[0,90,180])
fig.colorbar(im,ax=axes[:2],shrink=.75,label='Unconditional coincidence probability')
ax=axes[2];t=np.deg2rad(degrees)
ax.plot(degrees,.5*(np.cos(t)**4+np.sin(t)**4),label='classical mixture',color='#b45c2b')
ax.axhline(.5,label=r'$\Phi^+$',color='#1769aa')
ax.set(title='Equal analyzer angles',xlabel='Common angle (degrees)',ylabel='Coincidence probability',xlim=(0,180),ylim=(0,.55),xticks=[0,45,90,135,180])
ax.grid(alpha=.2);ax.legend(loc='lower center')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
