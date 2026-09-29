"""Original explanatory diagram; tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})

fig,axes=plt.subplots(1,2,figsize=(10.5,4.6),layout='constrained')
def change(ax,p,q,kind):
    color={'keep':'.6','break':'#d6604d','form':'#1b7837'}[kind]
    ax.plot([p[0],q[0]],[p[1],q[1]],color=color,lw=3,ls='--' if kind!='keep' else '-')
def panel(ax,n,labels,edges,title,note):
    angles=np.linspace(np.pi/2,np.pi/2+2*np.pi,n,endpoint=False)
    p=np.column_stack([np.cos(angles),np.sin(angles)])
    for i,j,kind in edges:change(ax,p[i],p[j],kind)
    for t,pt in zip(labels,p):ax.text(*pt,t,ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none','pad':5},fontsize=12)
    ax.text(0,-1.55,note,ha='center',va='top',fontsize=10)
    ax.set(title=title,xlim=(-1.5,1.5),ylim=(-2.1,1.35));ax.set_aspect('equal');ax.axis('off')
panel(axes[0],6,['O','a','b','c','d','e'],[(0,1,'break'),(1,2,'keep'),(2,3,'keep'),(3,4,'form'),(4,5,'keep'),(5,0,'keep')],'[3,3]: allyl ketene acetal','Break O–a; form c–d\nπ bonds: a=b and O=e\nProduct side chain: c–CH₂–CO₂Et')
panel(axes[1],5,['N⁺','a','b','c','y⁻'],[(0,1,'break'),(1,2,'keep'),(2,3,'keep'),(3,4,'form'),(4,0,'keep')],'[2,3]: allylic ammonium ylide','Break N–a; form c–y\nMove b=c to a=b\nN becomes neutral')
fig.suptitle('Atom maps for concerted rearrangements: red breaks, green forms')

fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=155,facecolor='white')
plt.close(fig)
