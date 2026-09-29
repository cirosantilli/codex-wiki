#!/usr/bin/env python3
"""Two equal masses and three equal springs; Python 3.14, NumPy/Matplotlib.
Writes a white-background PNG in the working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
fig,ax=plt.subplots(figsize=(8,4.2),layout='constrained',facecolor='white')
for y,signs,title in [(0,(1,1),r'In phase: $\omega=\sqrt{k/m}$; middle spring unchanged'),(-1.15,(1,-1),r'Opposite phase: $\omega=\sqrt{3k/m}$; middle extension $-2q$')]:
 ax.text(1.5,y+.61,title,ha='center',fontsize=11)
 for x in [0,3]:
  ax.plot([x,x],[y-.25,y+.25],lw=3,color='.3')
  for dy in np.linspace(-.23,.17,5):ax.plot([x-.1,x],[y+dy-.06,y+dy],color='.5',lw=.7)
 for l,r in [(0,1),(1,2),(2,3)]:
  xx=np.linspace(l+.12,r-.12,25);yy=np.zeros_like(xx);yy[1:-1]=.075*np.where(np.arange(len(xx)-2)%2,1,-1);ax.plot(np.r_[l,xx,r],np.r_[y,y+yy,y],lw=1.4,color='.4');ax.text((l+r)/2,y-.23,'k',ha='center',fontsize=10)
 for x,s in zip([1,2],signs):
  ax.add_patch(Circle((x,y),.105,facecolor='#e2edf8',edgecolor='#245d92',lw=1.4,zorder=3));ax.text(x,y,'m',ha='center',va='center',fontsize=10)
  ax.annotate('',xy=(x+.28*s,y+.27),xytext=(x,y+.27),arrowprops={'arrowstyle':'->','color':'#245d92','lw':2})
  ax.text(x+.13*s,y+.34,('q'if s>0 else '-q'),ha='center',fontsize=10,color='#245d92')
ax.set(aspect='equal',xlim=(-.25,3.25),ylim=(-1.6,.9));ax.axis('off');fig.suptitle('Small-oscillation modes between fixed walls',fontsize=14)
fig.savefig(Path.cwd()/'2010-two-mass-spring-modes.png',dpi=165,facecolor='white')
