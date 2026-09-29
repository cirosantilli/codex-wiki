"""Original Darcy-convection mode visualization; write PNG to cwd."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','savefig.facecolor':'white'})
x=np.linspace(0,2,151);z=np.linspace(0,1,91);X,Z=np.meshgrid(x,z)
theta=np.sin(np.pi*X)*np.sin(np.pi*Z)/(2*np.pi)
u=np.pi*np.cos(np.pi*X)*np.cos(np.pi*Z)
w=np.pi*np.sin(np.pi*X)*np.sin(np.pi*Z)
fig,ax=plt.subplots(figsize=(9.5,4.2),dpi=100)
c=ax.pcolormesh(X,Z,theta,cmap='RdBu_r',vmin=-1/(2*np.pi),vmax=1/(2*np.pi),shading='auto',rasterized=True)
ax.streamplot(x,z,u,w,density=(1.1,.85),color='#263238',linewidth=.9,arrowsize=1.1)
ax.set(xlim=(0,2),ylim=(0,1),xlabel='$x$',ylabel='$z$',title='Warm rising and cool sinking critical rolls')
ax.set_aspect('equal')
cb=fig.colorbar(c,ax=ax,pad=.035,fraction=.03)
cb.ax.set_title(r'$\theta_1$', pad=8)
fig.subplots_adjust(left=.065,right=.94,top=.90,bottom=.16)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100)
plt.close(fig)
