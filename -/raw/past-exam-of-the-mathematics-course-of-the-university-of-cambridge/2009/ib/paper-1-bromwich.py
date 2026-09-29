"""Original principal-branch inversion contour. Python 3.14, Matplotlib 3.10.7.
Writes paper-1-bromwich.png to the caller's CWD; preserves MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Arc
import numpy as np
fig,ax=plt.subplots(figsize=(7.8,5.3),dpi=120,facecolor='white')
ax.set_facecolor('white');blue='#1769aa';red='#b43d36'
def arrow(a,b,color=blue,style='-'):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='->',mutation_scale=12,lw=1.8,color=color,linestyle=style))
# Original solution diagram: rectangle and banks; bank offsets are schematic.
arrow((1,-2.6),(1,2.6));arrow((1,2.6),(-3.5,2.6))
arrow((-3.5,2.6),(-3.5,.12));arrow((-3.5,.12),(-.23,.12))
arrow((-.23,-.12),(-3.5,-.12));arrow((-3.5,-.12),(-3.5,-2.6));arrow((-3.5,-2.6),(1,-2.6))
theta=np.linspace(np.pi-.48,-np.pi+.48,180)
ax.plot(.26*np.cos(theta),.26*np.sin(theta),color=blue,lw=1.8)
arrow((.25*np.cos(-.8),.25*np.sin(-.8)),(.25*np.cos(-1.35),.25*np.sin(-1.35)))
ax.plot([-3.5,0],[0,0],color=red,lw=1,ls='--');ax.text(-2.7,-.4,'square-root cut',color=red,fontsize=11)
ax.axhline(0,color='#b0b0b0',lw=.7,zorder=0);ax.axvline(0,color='#b0b0b0',lw=.7,zorder=0)
for y,label in [(1,r'$i$'),(-1,r'$-i$')]:
 ax.scatter([0],[y],marker='x',s=65,color='#222222',zorder=6);ax.text(.16,y,label,fontsize=13)
ax.text(1.13,.6,r'$\Re s=\gamma>0$',rotation=90,va='center',fontsize=11,color=blue)
ax.text(-3.52,2.77,r'$-R+iR$',ha='left',fontsize=10)
ax.text(1,2.77,r'$\gamma+iR$',ha='right',fontsize=10)
ax.text(.35,-.47,r'$|s|=\varepsilon$',fontsize=10,color=blue)
ax.text(-2.25,1.7,'Close left for $t>0$',fontsize=12,color=blue)
ax.set_xlim(-3.9,1.8);ax.set_ylim(-3,3.25);ax.set_aspect('equal');ax.axis('off')
ax.set_title('Poles and branch-cut contribution',fontsize=14,pad=12)
fig.tight_layout();fig.savefig('paper-1-bromwich.png',facecolor='white',transparent=False);plt.close(fig)
