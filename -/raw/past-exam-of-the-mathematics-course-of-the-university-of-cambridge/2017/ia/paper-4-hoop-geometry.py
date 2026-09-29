#!/usr/bin/env python3
"""Original constructed geometry for Q11. Python3.14/mpl3.10.7/np2.3.5.
Run from the wiki root; output is under its mirrored _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(5.6,3.6),layout='constrained')
phi=np.linspace(0,2*np.pi,600);theta=.5
ax.plot(1+np.cos(phi),np.sin(phi),color='#174d82',lw=2)
P=np.array([1+np.cos(2*theta),np.sin(2*theta)])
ax.annotate('',(2.45,0),(-.25,0),arrowprops={'arrowstyle':'->','lw':.9})
ax.annotate('',(0,1.22),(0,-1.12),arrowprops={'arrowstyle':'->','lw':.9})
ax.text(2.3,-.14,"$x'$",fontsize=12);ax.text(-.13,1.12,"$y'$",fontsize=12)
ax.plot([0,P[0]],[0,P[1]],'k--',lw=1)
ax.plot([1,P[0]],[0,P[1]],color='gray',ls=':',lw=1.3)
ax.scatter([0,1,P[0]],[0,0,P[1]],color='black',s=[20,18,27],zorder=3)
ax.text(-.18,-.16,'$O$',fontsize=12);ax.text(.9,-.17,'$C$',fontsize=12);ax.text(P[0]+.08,P[1]+.02,'$P$',fontsize=12)
u=np.linspace(0,theta,80);ax.plot(.43*np.cos(u),.43*np.sin(u),'k',lw=.9)
ax.text(.47,.105,'$\\theta$',fontsize=12)
v=np.linspace(0,2*theta,100);ax.plot(1+.26*np.cos(v),.26*np.sin(v),color='gray',lw=1)
ax.text(1.3,.16,'$2\\theta$',fontsize=11)
n=np.array([np.cos(2*theta),np.sin(2*theta)]);tau=np.array([-n[1],n[0]])
for vec,label,color in ((n,'$\\mathbf{n}$','#b02e32'),(tau,'$\\tau$','#1c7353')):
    end=P+.32*vec;ax.annotate('',end,P,arrowprops={'arrowstyle':'->','color':color,'lw':1.5});ax.text(end[0]+.02,end[1]+.01,label,fontsize=11,color=color)
ax.set(xlim=(-.3,2.5),ylim=(-1.2,1.3),aspect='equal');ax.axis('off')
output=Path('paper-4-hoop-geometry.png')
output.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(output,dpi=100,facecolor='white');plt.close(fig)
