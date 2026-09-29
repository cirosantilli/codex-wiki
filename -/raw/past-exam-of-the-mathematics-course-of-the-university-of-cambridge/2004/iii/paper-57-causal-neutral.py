"""Original neutral/naked causal diagrams. Python 3.14; Matplotlib and NumPy.
Writes the fixed PNG basename to the caller's working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig,axes=plt.subplots(1,2,figsize=(9.1,4.5),layout='constrained',facecolor='white')
blue='#175b91';red='#ab2538';dark='#333333'
def line(ax,a,b,color=dark,lw=1.8):ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=lw)
def fill(ax,points,color):ax.add_patch(Polygon(points,facecolor=color,edgecolor='none'))
for ax in axes:ax.axis('off');ax.set_aspect('equal');ax.set_facecolor('white')
ax=axes[0]
for sign in [-1,1]:
 fill(ax,[(0,0),(sign,-1),(2*sign,0),(sign,1)],'#edf4ea')
 line(ax,(0,0),(sign,1),blue);line(ax,(0,0),(sign,-1),blue)
 line(ax,(sign,1),(2*sign,0));line(ax,(2*sign,0),(sign,-1))
 ax.text(1.15*sign,0,'Exterior',ha='center',fontsize=10)
 ax.text(1.8*sign,.6,r'$\mathcal{I}^+$',ha='center',fontsize=13)
 ax.text(1.8*sign,-.7,r'$\mathcal{I}^-$',ha='center',fontsize=13)
 ax.text(2.12*sign,0,r'$i^0$',ha='center',fontsize=11)
for sign,name in [(1,'Black hole'),(-1,'White hole')]:
 fill(ax,[(-1,sign),(0,0),(1,sign)],'#e7eff8')
 x=np.linspace(-1,1,121);y=sign+.024*np.sin(np.arange(121)*np.pi/2)
 ax.plot(x,y,color=red,lw=2.5)
 ax.text(0,.58*sign,name,ha='center',va='center',fontsize=11)
 ax.text(0,1.19*sign,r'$r=0$ (spacelike)',ha='center',va='center',color=red,fontsize=10)
ax.text(.67,.32,r'$r_+$',color=blue,fontsize=10)
ax.text(.67,-.44,r'$r_+$',color=blue,fontsize=10)
ax.set_xlim(-2.55,2.55);ax.set_ylim(-1.5,1.55)
ax.set_title('Neutral: Q = 0',fontsize=13)
ax=axes[1]
fill(ax,[(0,-1),(1,0),(0,1)],'#edf4ea')
line(ax,(0,1),(1,0));line(ax,(1,0),(0,-1))
y=np.linspace(-1,1,121);x=.017*np.sin(np.arange(121)*np.pi/2)
ax.plot(x,y,color=red,lw=2.5)
ax.text(-.17,0,r'$r=0$'+'\nTimelike\nsingularity',ha='right',va='center',color=red,fontsize=10)
ax.text(.36,0,'Static\nexterior',ha='center',va='center',fontsize=11)
ax.text(.65,.66,r'$\mathcal{I}^+$',fontsize=13);ax.text(.65,-.72,r'$\mathcal{I}^-$',fontsize=13)
ax.text(1.1,0,r'$i^0$',fontsize=12);ax.text(0,1.15,r'$i^+$',ha='center',fontsize=12);ax.text(0,-1.23,r'$i^-$',ha='center',fontsize=12)
ax.set_xlim(-.9,1.5);ax.set_ylim(-1.45,1.55)
ax.set_title('Overcharged: |Q| > M',fontsize=13)
fig.suptitle('Radial Penrose diagrams; angular three-spheres suppressed',fontsize=13)
fig.savefig(Path.cwd()/'paper-57-causal-neutral.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
