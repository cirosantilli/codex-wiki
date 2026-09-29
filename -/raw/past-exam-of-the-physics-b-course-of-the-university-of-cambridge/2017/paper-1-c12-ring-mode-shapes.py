"""Original bead-ring mode displacements; Python 3.14, numpy and matplotlib.

Write the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,3,figsize=(10.5,3.7),layout='constrained',facecolor='white')
angles=np.deg2rad([90,-30,-150])
shapes=[([1,-1,0],r'$(1,-1,0)$'),([1,0,-1],r'$(1,0,-1)$'),([1,1,1],r'$(1,1,1)$')]
for ax,(coeff,title) in zip(axes,shapes):
    ax.set_facecolor('white')
    arc=np.linspace(0,2*np.pi,400)
    ax.plot(np.cos(arc),np.sin(arc),color='#bbbbbb',lw=2)
    for j,(theta,c) in enumerate(zip(angles,coeff),1):
        pos=np.array([np.cos(theta),np.sin(theta)])
        ax.scatter(*pos,s=100,color='#165b99',zorder=4)
        ax.text(*(1.2*pos),str(j),fontsize=12,ha='center',va='center')
        if c:
            direction=np.array([np.sin(theta),-np.cos(theta)])*c
            ax.annotate('',xy=pos+.46*direction,xytext=pos,arrowprops={'arrowstyle':'->','color':'#cc7a1d','lw':2})
        else:
            ax.text(*(pos+np.array([0,-.23])),'fixed',fontsize=9,ha='center')
    subtitle=r'$\omega=\sqrt{3k/m}$' if coeff!=[1,1,1] else r'$\omega=0$: rigid rotation'
    ax.set_title(title+'\n'+subtitle,fontsize=12)
    ax.set(xlim=(-1.5,1.5),ylim=(-1.4,1.5),aspect='equal')
    ax.axis('off')
fig.suptitle('Tangential displacements at a positive modal amplitude',fontsize=13)
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white')
