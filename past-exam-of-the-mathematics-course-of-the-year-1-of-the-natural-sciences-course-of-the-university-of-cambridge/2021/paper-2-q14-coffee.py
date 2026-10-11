"""Original coffee probability plots; Python 3.14, NumPy 2.3,
Matplotlib 3.10. The PNG is written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

plt.rcParams.update({'font.size':10,'figure.facecolor':'white'})
fig,(ax,joint)=plt.subplots(1,2,figsize=(9.3,3.9),layout='constrained')
v=np.linspace(270,330,500)
p=np.pi/120*np.cos(np.pi*(v-300)/60)
ax.plot(v,p,color='#256c9c',lw=2)
mask=(v>=290)&(v<=310)
ax.fill_between(v[mask],0,p[mask],color='#bdddf2',label='passes: probability 1/2')
ax.axhline(0,color='0.5',lw=1)
ax.set(xlim=(265,335),ylim=(0,.029),xlabel='Volume (mL)',ylabel=r'Density ($\mathrm{mL}^{-1}$)',title='One cup')
ax.legend(loc='upper left',frameon=False,fontsize=9)
ax.set_xticks([270,290,300,310,330])
q=np.linspace(-np.pi/2,np.pi/2,250);X,Y=np.meshgrid(q,q)
joint.contourf(X,Y,.25*np.cos(X)*np.cos(Y),levels=14,cmap='Blues')
joint.add_patch(Polygon([[0,np.pi/2],[np.pi/2,0],[np.pi/2,np.pi/2]],facecolor='#ed8a50',alpha=.55,edgecolor='#a14218',lw=1.5))
joint.plot([0,np.pi/2],[np.pi/2,0],color='#a14218',lw=1.7)
joint.text(.82,1.05,r'$X+Y\geq\pi/2$',fontsize=9,ha='center',rotation=-25)
joint.set(xlim=(-np.pi/2,np.pi/2),ylim=(-np.pi/2,np.pi/2),aspect='equal',xlabel='$X$',ylabel='$Y$',title='Two independent cups')
for setter in [joint.set_xticks,joint.set_yticks]:setter([-np.pi/2,0,np.pi/2],labels=[r'$-\pi/2$','0',r'$\pi/2$'])
joint.text(-1.4,-1.3,r'$p_{X,Y}=\frac{1}{4}\cos X\cos Y$',fontsize=10)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
