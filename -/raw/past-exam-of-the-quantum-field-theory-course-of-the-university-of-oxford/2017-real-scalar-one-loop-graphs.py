"""Original diagrams for the real cubic/quartic theory; Python 3.14/matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle
plt.rcParams.update({'font.size':12})
fig,axs=plt.subplots(3,3,figsize=(12,10),layout='constrained',facecolor='white')
color='#174e67';quartic='#9b3e37'
def line(ax,a,b,rad=0):
 ax.add_patch(FancyArrowPatch(a,b,connectionstyle=f'arc3,rad={rad}',arrowstyle='-',lw=2,color=color,shrinkA=0,shrinkB=0))
def vertex(ax,p,n=3):ax.plot(*p,marker='o' if n==3 else 's',ms=7,color=color if n==3 else quartic,zorder=4)
def loop(ax,p):ax.add_patch(Circle((p[0],p[1]+.27),.27,fill=False,color=color,lw=2))
def label(ax,text):ax.text(0,-.38,text,ha='center',va='top',fontsize=12)
def bubble(ax,leftn,rightn):
 a=(-.43,.45);b=(.43,.45)
 line(ax,a,b,.62);line(ax,a,b,-.62)
 for p,n,sgn in [(a,leftn,-1),(b,rightn,1)]:
  if n==3:line(ax,p,(sgn*1.02,.45))
  else:
   line(ax,p,(sgn*1.02,.10));line(ax,p,(sgn*1.02,.80))
  vertex(ax,p,n)
def triangle(ax,mixed=False):
 pts=[(-.48,.08),(.48,.08),(0,.82)]
 for a,b in zip(pts,pts[1:]+pts[:1]):line(ax,a,b)
 for p,e in zip(pts[:2],[(-1.03,-.13),(1.03,-.13)]):line(ax,p,e);vertex(ax,p)
 if mixed:
  line(ax,pts[2],(-.42,1.12));line(ax,pts[2],(.42,1.12));vertex(ax,pts[2],4)
 else:line(ax,pts[2],(0,1.15));vertex(ax,pts[2])
ax=axs[0,0];p=(0,.35);line(ax,(-1,.35),p);line(ax,p,(1,.35));loop(ax,p);vertex(ax,p,4);label(ax,r'2-point: quartic tadpole; $S=2$')
ax=axs[0,1];bubble(ax,3,3);label(ax,r'2-point: cubic bubble; $S=2$')
ax=axs[0,2];a=(-.35,.30);b=(.52,.30)
line(ax,a,(-1,.0));line(ax,a,(-1,.65));line(ax,a,b);loop(ax,b);vertex(ax,a);vertex(ax,b);label(ax,'2-point: attached tadpole; S = 2\nConnected; one-particle reducible')
ax=axs[1,0];triangle(ax);label(ax,'3-point: cubic triangle\nS = 1; one labelled graph')
ax=axs[1,1];bubble(ax,3,4);label(ax,'3-point: mixed bubble\nS = 2; three attachments')
ax=axs[1,2];ax.text(0,.75,'Vertex key',ha='center',weight='bold');vertex(ax,(-.55,.35),3);ax.text(-.33,.35,r'Cubic: $-i\kappa$',va='center');vertex(ax,(-.55,-.02),4);ax.text(-.33,-.02,r'Quartic: $-i\lambda$',va='center');ax.text(0,-.38,'S divides each graph.\nExternal legs are labelled.\nMultiply by the stated attachment count.',ha='center',va='top',fontsize=11)
ax=axs[2,0];bubble(ax,4,4);label(ax,'4-point: quartic bubble\nS = 2; three channels')
ax=axs[2,1];triangle(ax,True);label(ax,'4-point: mixed triangle\nS = 1; six attachments')
ax=axs[2,2];pts=[(-.45,.12),(.45,.12),(.45,.85),(-.45,.85)]
for a,b in zip(pts,pts[1:]+pts[:1]):line(ax,a,b)
for p,e in zip(pts,[(-.98,-.12),(.98,-.12),(.98,1.10),(-.98,1.10)]):line(ax,p,e);vertex(ax,p)
label(ax,'4-point: cubic box\nS = 1; three cyclic orders')
for ax in axs.flat:ax.set(xlim=(-1.25,1.25),ylim=(-.95,1.30));ax.set_aspect('equal');ax.axis('off');ax.set_facecolor('white')
fig.suptitle('Real scalar theory: all one-loop families needed for the 2-, 3- and 4-point functions',fontsize=16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'})
plt.close(fig)
