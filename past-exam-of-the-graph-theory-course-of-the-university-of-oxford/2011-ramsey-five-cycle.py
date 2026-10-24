"""Original Ramsey lower-bound illustration; Python 3.14, NumPy 2.3, Matplotlib 3.10.
The output PNG is written to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
angles=np.pi/2+2*np.pi*np.arange(5)/5
points=np.column_stack([np.cos(angles),np.sin(angles)])
fig,axes=plt.subplots(1,2,figsize=(8,4.2),facecolor='white')
for j,ax in enumerate(axes):
    color='#c23838' if j==0 else '#2075b4'
    step=1 if j==0 else 2
    for i in range(5):
        k=(i+step)%5
        ax.plot(points[[i,k],0],points[[i,k],1],color=color,lw=2.4,zorder=1)
    ax.scatter(points[:,0],points[:,1],s=190,color='white',edgecolor='#202020',lw=1.5,zorder=2)
    for i,(x,y) in enumerate(points):ax.text(x,y,str(i+1),ha='center',va='center',fontsize=9,zorder=3)
    ax.set(aspect='equal',xlim=(-1.25,1.25),ylim=(-1.2,1.25));ax.axis('off')
    ax.set_title('A five-cycle' if j==0 else 'Its complementary edges',fontsize=13)
fig.suptitle('Neither colour contains a triangle on these five vertices',fontsize=14)
fig.tight_layout(rect=(0,0,1,.92))
fig.savefig(Path.cwd()/'2011-ramsey-five-cycle.png',dpi=170,facecolor='white')
