#!/usr/bin/env python3
"""Original schematic, not a copy of the exam image. Python 3.14.4.
Dependencies: matplotlib; documented in the root pyproject.toml.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

fig,ax=plt.subplots(figsize=(9,4.2),dpi=100,facecolor='white')
ax.set_facecolor('white');ax.set_xlim(-1.2,7.4);ax.set_ylim(-.5,3.0);ax.axis('off')
for yy in [0,2]:ax.plot([0,6.5],[yy,yy],color='black',lw=2)
ax.plot([0,0],[0,.86],color='black',lw=2);ax.plot([0,0],[1.14,2],color='black',lw=2)
ax.plot([-.3,.3],[.86,.86],color='black',lw=2.4)
ax.plot([-.16,.16],[1.14,1.14],color='black',lw=2.4)
ax.text(.38,.76,'+',fontsize=14);ax.text(.38,1.11,'−',fontsize=14)
ax.text(-.95,.97,r'$\mathcal{E}_0$',fontsize=17)
ax.plot([5,5],[0,.7],color='black',lw=2);ax.plot([5,5],[1.3,2],color='black',lw=2)
ax.add_patch(Rectangle((4.88,.7),.24,.6,facecolor='white',edgecolor='black',lw=2))
ax.text(5,.98,r'$R$',fontsize=13,ha='center',va='center')
for label,xx,yy,dx,dy in [('D',0,0,-.27,-.27),('G',0,2,-.3,.13),('E',5,0,-.05,-.27),('F',5,2,-.05,.13)]:
 ax.plot(xx,yy,'o',color='black',ms=4);ax.text(xx+dx,yy+dy,label,fontsize=15)
ax.annotate('',xy=(5.45,1.7),xytext=(5.45,.35),arrowprops={'arrowstyle':'->','color':'#b22222','lw':2.5})
ax.text(5.62,1.0,r'$I>0$',color='#b22222',fontsize=15)
ax.annotate('',xy=(6.4,2.6),xytext=(4.9,2.6),arrowprops={'arrowstyle':'->','color':'#1f5c99','lw':2})
ax.text(5.24,2.76,r'$\dot{s}$',color='#1f5c99',fontsize=16)
ax.add_patch(Circle((2.3,1),.12,edgecolor='black',facecolor='white',lw=1.4))
ax.plot(2.3,1,'o',color='black',ms=3)
ax.text(2.65,1.04,r'$B_0\,\mathbf{e}_z$',fontsize=14)
ax.text(2.65,.7,'(out of page)',fontsize=13)
ax.annotate('',xy=(6.95,0),xytext=(6.5,0),arrowprops={'arrowstyle':'->','color':'black'})
ax.text(7.04,-.06,r'$x$',fontsize=15)
ax.annotate('',xy=(0,2.62),xytext=(0,2.2),arrowprops={'arrowstyle':'->','color':'black'})
ax.text(-.12,2.72,r'$y$',fontsize=15)
ax.text(2.2,-.32,r'$0<x<s(t)$',fontsize=14)
fig.subplots_adjust(left=.03,right=.98,bottom=.10,top=.95)
dest=Path.cwd()/'paper-3-moving-bar.png';fig.savefig(dest,dpi=100,facecolor='white',transparent=False)
plt.close(fig)
