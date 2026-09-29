"""Original explanatory model; output is a basename in the working directory."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':9,'axes.titlesize':10,'axes.labelsize':10})

fig,axs=plt.subplots(1,2,figsize=(9,4.2),layout='constrained');xx=np.linspace(-.5,4,700);vv=np.linspace(-2.6,2.6,600);X,V=np.meshgrid(xx,vv);edges=np.arange(5)+.5;g=np.zeros_like(X)
for n in edges:g+=.5*((V/2>n-X).astype(float)+(-V/2>n-X).astype(float))
im=axs[0].pcolormesh(X,V,g,shading='auto',cmap='viridis',vmin=0,vmax=4);fig.colorbar(im,ax=axs[0],label=r'$G_d/(2e^2/h)$')
for n in edges:
 for s in [-1,1]:axs[0].plot(xx,s*2*(n-xx),color='white',lw=.7,alpha=.7)
axs[0].plot(1,1,'ro',ms=4);axs[0].set(xlim=(-.5,4),ylim=(-2.6,2.6),xlabel='Gate lowering / subband spacing',ylabel=r'$eV/\Delta E$',title='Rigid-threshold bias map')
for v in [0,.8,1.4]:
 gc=sum(.5*(1/(1+np.exp(np.clip((n-xx-v/2)/.015,-700,700)))+1/(1+np.exp(np.clip((n-xx+v/2)/.015,-700,700)))) for n in edges)
 axs[1].plot(xx,gc,lw=1.7,label=rf'$eV/\Delta E={v:g}$')
axs[1].set(xlim=(-.5,4),ylim=(0,4.2),xlabel='Gate lowering / subband spacing',ylabel=r'$G_d/(2e^2/h)$',title='Differential half plateaus');axs[1].legend(fontsize=8);axs[1].grid(alpha=.2)
fig.savefig('paper-1-bias-spectroscopy.png',dpi=170,facecolor='white');plt.close(fig)
