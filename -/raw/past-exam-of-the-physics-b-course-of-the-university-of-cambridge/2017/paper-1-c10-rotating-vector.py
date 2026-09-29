"""Original infinitesimal-rotation diagram; Python 3.14, matplotlib, numpy.

Write the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots(figsize=(6.2,4.5),layout='constrained',facecolor='white')
ax.set_facecolor('white')
angle=.20
A=np.array([3.,.65])
Q=np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
Ap=Q@A
for endpoint,color in [(A,'#165b99'),(Ap,'#777777')]:
    ax.annotate('',xy=endpoint,xytext=(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':color})
ax.annotate('',xy=Ap,xytext=A,arrowprops={'arrowstyle':'->','lw':2,'color':'#c26b20'})
phi=np.linspace(np.arctan2(A[1],A[0]),np.arctan2(Ap[1],Ap[0]),100)
ax.plot(.9*np.cos(phi),.9*np.sin(phi),color='black')
ax.text(.85,.35,r'$d\theta$',fontsize=12)
ax.text(1.65,.18,r'$\mathbf{A}(t)$',fontsize=13,color='#165b99')
ax.text(1.4,1.08,r'$\mathbf{A}(t+dt)$',fontsize=12,color='#555555')
ax.text(3.1,.99,r'$d\mathbf{A}\simeq d\boldsymbol{\theta}\times\mathbf{A}$',fontsize=11,color='#a45d10')
ax.text(.12,1.8,r'$\odot\ d\boldsymbol{\theta}$',fontsize=15)
ax.text(.1,1.52,'Rotation axis out of page',fontsize=10)
ax.scatter([0],[0],color='black',s=20)
ax.text(-.04,-.15,'Common origin',fontsize=9)
ax.set(xlim=(-.3,4.8),ylim=(-.3,2.25),aspect='equal',title='A rotating basis changes vector direction')
ax.axis('off')
fig.savefig(Path(__file__).stem+'.png',dpi=145,facecolor='white')
