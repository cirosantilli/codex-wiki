"""Original explanatory diagram; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axes=plt.subplots(1,2,figsize=(9.5,3.8),layout='constrained')
a1=np.array([1.,0]);a2=np.array([.5,np.sqrt(3)/2])
for i in range(-3,4):
    for j in range(-2,3):
        p=i*a1+j*a2
        axes[0].scatter(*p,s=180,color='#b9d5ed',edgecolor='#2166ac')
axes[0].set(xlim=(-2.6,2.6),ylim=(-1.9,1.9),title='Triangular (111) monolayer');axes[0].set_aspect('equal');axes[0].axis('off')
angles=np.arange(6)*np.pi/3
for radius,ax,title in [(1,axes[1],'Alternating step families')]:
    for k,angle in enumerate(angles):
        p=radius*np.array([np.cos(angle),np.sin(angle)])
        q=radius*np.array([np.cos(angle+np.pi/3),np.sin(angle+np.pi/3)])
        ax.plot([p[0],q[0]],[p[1],q[1]],lw=5,color='#2166ac' if k%2==0 else '#d6604d')
        centre=(p+q)/2
        ax.text(*(1.35*centre),'A' if k%2==0 else 'B',ha='center',va='center')
ax.set(title=title,xlim=(-1.6,1.6),ylim=(-1.4,1.4));ax.set_aspect('equal');ax.axis('off')
fig.suptitle('Equal A/B step energies favor a hexagon; strong asymmetry favors a triangle')

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=155,facecolor='white')
plt.close(fig)
