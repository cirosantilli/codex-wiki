"""Original conformal-map diagrams, with matching PNG output in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1,3,figsize=(10,3.9),layout='constrained')
colors=['#2479ac','#cb732d','#36894d','#9a59a5']
vertices=[0,1,1+1j,1j,0]
edges=[np.linspace(vertices[j],vertices[j+1],250)for j in range(4)]
for i,ax in enumerate(axes):
    for j,e in enumerate(edges):
        if i==0:w=e
        elif i==1:w=np.exp(e)
        else:
            e=e[np.abs(e)>.00001]
            w=np.log(np.abs(e))+1j*np.angle(e)
        ax.plot(w.real,w.imag,color=colors[j],lw=2)
    ax.set_aspect('equal')
    ax.grid(alpha=.18)
    ax.axhline(0,color='.6',lw=.6)
    ax.axvline(0,color='.6',lw=.6)
axes[0].set(title='Input square, a = 1',xlabel='Real part',ylabel='Imaginary part',xlim=(-.2,1.2),ylim=(-.2,1.2))
axes[1].set(title=r'Exponential: $w=e^z$',xlabel='Real part',xlim=(.3,2.9),ylim=(-.2,2.5))
axes[2].set(title=r'Logarithm: $z=\log w$',xlabel='Real part',xlim=(-2.2,.6),ylim=(-.2,1.8))
for y in [0,np.pi/2]:
    axes[2].annotate('',(-2.15,y),(-1.65,y),arrowprops={'arrowstyle':'->','color':'.35'})
axes[2].text(-1.9,.75,r'continues to $-\infty$',fontsize=9)
axes[2].scatter([0,np.log(2)/2,0],[0,np.pi/4,np.pi/2],s=18,color='black',zorder=4)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
