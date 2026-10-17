"""Constructed neutral XY vortex pair; arrows show order-parameter orientation."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
axis=np.linspace(-2.7,2.7,27)
x,y=np.meshgrid(axis,axis);z=x+1j*y
phase=np.angle(z+1)-np.angle(z-1)
mask=(abs(z+1)>.3)&(abs(z-1)>.3)
fig,ax=plt.subplots(figsize=(6.4,6),facecolor='white',layout='constrained')
ax.quiver(x[mask],y[mask],np.cos(phase)[mask],np.sin(phase)[mask],angles='xy',scale_units='xy',scale=7.5,pivot='mid',color='#2a627e',width=.005)
for center,color,label in [((-1,0),'#b45f16',r'$q=+1$'),((1,0),'#744a91',r'$q=-1$')]:
    ax.add_patch(Circle(center,.28,facecolor='white',edgecolor=color,lw=1.8))
    ax.text(center[0],-.48,label,ha='center',color=color,fontsize=12,bbox=dict(facecolor='white',edgecolor='none',pad=1))
    ax.add_patch(Circle(center,.67,fill=False,edgecolor=color,ls='--',lw=1.2))
ax.add_patch(Circle((0,0),2.35,fill=False,edgecolor='.5',ls=':',lw=1.5))
ax.text(0,2.55,'Large circuit: net winding 0',ha='center',fontsize=11,bbox=dict(facecolor='white',edgecolor='none',pad=2))
ax.set(xlim=(-2.9,2.9),ylim=(-2.9,2.9),aspect='equal',xlabel=r'$x$ (chosen units)',ylabel=r'$y$ (chosen units)',title=r'$\theta=\arg(z+1)-\arg(z-1)$')
fig.savefig('paper-1-ptcp2012-vortex-pair.png',dpi=170,facecolor='white')
plt.close(fig)
