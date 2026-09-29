"""Original spring-triangle displacement diagrams; Python 3.14, NumPy, Matplotlib.

Run in the mirrored _media paper directory; writes the PNG to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

r=np.array([[0,1],[np.sqrt(3)/2,-.5],[-np.sqrt(3)/2,-.5]])
modes=[np.tile([1.,0.],(3,1)),np.tile([0.,1.],(3,1)),np.column_stack([-r[:,1],r[:,0]]),r]
labels=['Horizontal translation','Vertical translation','Infinitesimal rotation','Radial breathing']
freqs=[r'$\omega=0$',r'$\omega=0$',r'$\omega=0$',r'$\omega=\sqrt{3k/m}$']
fig,axes=plt.subplots(1,4,figsize=(11,3.5),facecolor='white')
for ax,mode,label,freq in zip(axes,modes,labels,freqs):
    for i,j in [(0,1),(1,2),(2,0)]:
        ax.plot(r[[i,j],0],r[[i,j],1],color='#94a3b8',lw=1.7,zorder=1)
    ax.scatter(r[:,0],r[:,1],s=60,color='#334155',zorder=3)
    for vertex,arrow in zip(r,mode):
        ax.annotate('',xy=vertex+.48*arrow,xytext=vertex,arrowprops={'arrowstyle':'-|>','lw':1.9,'color':'#be123c','mutation_scale':12})
    ax.set(title=label,xlim=(-1.65,1.65),ylim=(-1.25,1.8))
    ax.text(0,-1.18,freq,ha='center',va='top',fontsize=12)
    ax.set_aspect('equal')
    ax.axis('off')
fig.suptitle('Arrows show instantaneous displacement ratios',fontsize=12,y=.98)
fig.subplots_adjust(left=.02,right=.98,top=.83,bottom=.12,wspace=.12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=155,facecolor='white')
plt.close(fig)
