#!/usr/bin/env python3
"""Original B2 root diagram. Python3.12, matplotlib; PNG written to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(5.4,5.1),layout='constrained',facecolor='white')
short=[(1,0),(-1,0),(0,1),(0,-1)];long=[(1,1),(1,-1),(-1,1),(-1,-1)]
for roots,color,label in[(short,'#155e75','Short roots'),(long,'#6b4f9d','Long roots')]:
 for x,y in roots:ax.plot([0,x],[0,y],color=color,alpha=.45,lw=1)
 ax.scatter(*zip(*roots),color=color,s=55,label=label,zorder=3)
for x,y,text,offset in[(0,1,r'$\alpha_1=e_2$',(-.05,.12)),(1,-1,r'$\alpha_2=e_1-e_2$',(-.8,-.22))]:
 ax.annotate('',(x,y),(0,0),arrowprops={'arrowstyle':'->','color':'#ad3e23','lw':2.5});ax.text(x+offset[0],y+offset[1],text,color='#ad3e23',fontsize=12)
ax.axhline(0,color='gray',lw=.7);ax.axvline(0,color='gray',lw=.7)
ax.set(xlim=(-1.4,1.55),ylim=(-1.5,1.5),aspect='equal',xlabel=r'$e_1$ coordinate',ylabel=r'$e_2$ coordinate',title=r'$B_2$ roots and simple roots')
ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.legend(loc='upper left',fontsize=8);ax.set_facecolor('white')
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
