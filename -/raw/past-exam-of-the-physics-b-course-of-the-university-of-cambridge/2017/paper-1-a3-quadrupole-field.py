"""Original planar-quadrupole sketch; Python 3.14, matplotlib and numpy from pyproject.toml.

Write the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-2.2,2.2,301)
y=np.linspace(-2.2,2.2,301)
X,Y=np.meshgrid(x,y)
fig,ax=plt.subplots(figsize=(6.4,5.6),layout='constrained',facecolor='white')
ax.set_facecolor('white')
levels=[-3,-1.5,-.5,.5,1.5,3]
cs=ax.contour(X,Y,X**2-Y**2,levels=levels,colors='#cc7a1d',linewidths=.8,alpha=.8)
ax.clabel(cs,fmt='%g',fontsize=8)
ax.streamplot(x,y,-X,Y,color='#165b99',density=.85,arrowsize=1.2,linewidth=1.2)
ax.axhline(0,color='#777777',lw=.6)
ax.axvline(0,color='#777777',lw=.6)
ax.scatter([0],[0],s=20,color='black',zorder=4)
ax.set(xlim=(-2.2,2.2),ylim=(-2.2,2.2),aspect='equal',xlabel=r'$x$ (arbitrary length unit)',ylabel=r'$y$ (same unit)',title=r'Planar quadrupole: $V=A(x^2-y^2)$, $A>0$')
ax.text(.03,.03,'Blue: field lines     Orange: equipotentials',transform=ax.transAxes,fontsize=9,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white')
