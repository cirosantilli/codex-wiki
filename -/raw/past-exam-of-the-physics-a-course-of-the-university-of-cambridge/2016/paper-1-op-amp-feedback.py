"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3; writes basename PNG to cwd, normally the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Polygon,Circle
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(10,3.6))
def wire(ax,p,q):ax.plot([p[0],q[0]],[p[1],q[1]],color='#344e5e',lw=1.3)
def rh(ax,x,y,w,t):
 ax.add_patch(Rectangle((x,y-.12),w,.24,facecolor='white',edgecolor='#344e5e'));ax.text(x+w/2,y+.25,t,ha='center',fontsize=9)
def rv(ax,x,y,h,t):
 ax.add_patch(Rectangle((x-.12,y),.24,h,facecolor='white',edgecolor='#344e5e'));ax.text(x-.23,y+h/2,t,ha='right',va='center',fontsize=9)
def ground(ax,x,y):
 for j,w in enumerate([.35,.22,.1]):wire(ax,(x-w/2,y-.1*j),(x+w/2,y-.1*j))
for ax in axs:
 ax.set(xlim=(-.3,5.8),ylim=(-.2,4.2),aspect='equal');ax.axis('off');ax.add_patch(Polygon([(2,1),(2,3),(4,2)],facecolor='#e4eef3',edgecolor='#344e5e'));wire(ax,(4,2),(5.4,2));ax.text(5.45,2,'Vo',va='center')
ax=axs[0];ax.text(2.12,2.5,'−',va='center');ax.text(2.12,1.5,'+',va='center');wire(ax,(0,2.5),(.55,2.5));rh(ax,.55,2.5,.65,'Ri');wire(ax,(1.2,2.5),(2,2.5));ax.text(-.08,2.5,'Vi',ha='right',va='center');wire(ax,(1.6,2.5),(1.6,3.6));wire(ax,(1.6,3.6),(2.55,3.6));rh(ax,2.55,3.6,.8,'Rf');wire(ax,(3.35,3.6),(4.6,3.6));wire(ax,(4.6,3.6),(4.6,2));wire(ax,(2,1.5),(1.6,1.5));wire(ax,(1.6,1.5),(1.6,.6));ground(ax,1.6,.6);ax.scatter([1.6,4.6],[2.5,2],s=10,color='#344e5e');ax.set_title('Inverting amplifier')
ax=axs[1];ax.text(2.12,2.5,'+',va='center');ax.text(2.12,1.5,'−',va='center');wire(ax,(0,2.5),(2,2.5));ax.text(-.08,2.5,'Vi',ha='right',va='center');wire(ax,(2,1.5),(.6,1.5));wire(ax,(.6,1.5),(.6,1.3));rv(ax,.6,.6,.7,'Rg');wire(ax,(.6,.6),(.6,.25));ground(ax,.6,.25);wire(ax,(1.6,1.5),(1.6,.7));wire(ax,(1.6,.7),(2.55,.7));rh(ax,2.55,.7,.8,'Rf');wire(ax,(3.35,.7),(4.6,.7));wire(ax,(4.6,.7),(4.6,2));ax.scatter([1.6,4.6],[1.5,2],s=10,color='#344e5e');ax.set_title('Noninverting amplifier');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
