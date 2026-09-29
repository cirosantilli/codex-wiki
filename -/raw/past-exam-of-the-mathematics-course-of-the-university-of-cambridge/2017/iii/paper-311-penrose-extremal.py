"""Original extremal conformal blocks and complete repeated gluing rule.
Python 3.14 / Matplotlib 3.10.7 / NumPy 2.3.5. Outputs same-base PNG to CWD.
Separate blocks deliberately avoid inventing a degenerate bifurcation point.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from pathlib import Path
import numpy as np
plt.rcParams.update({'font.size':12,'font.family':'DejaVu Sans'})
fig,axes=plt.subplots(1,2,figsize=(10.6,6.2),dpi=100,facecolor='white')
future='#2166ac';past='#7b3294';singular='#ad1d25'
for ax in axes:
 ax.axis('off');ax.set_aspect('equal');ax.set_facecolor('white');ax.set_xlim(-1.6,1.6);ax.set_ylim(-1.45,1.60)
def edge(ax,a,b,col):ax.plot([a[0],b[0]],[a[1],b[1]],color=col,lw=2.4)
ax=axes[0]
ax.add_patch(Polygon([(-1,0),(0,-1),(1,0),(0,1)],facecolor='#eef5ec',edgecolor='none'))
edge(ax,(-1,0),(0,1),future);edge(ax,(-1,0),(0,-1),past)
edge(ax,(0,1),(1,0),'#333333');edge(ax,(0,-1),(1,0),'#333333')
ax.text(0,0,'Exterior\n'+r'$r>R$',ha='center',va='center',fontsize=14)
ax.text(-.73,.69,r'$H^+$',ha='center',color=future,fontsize=14)
ax.text(-.73,-.75,r'$H^-$',ha='center',color=past,fontsize=14)
ax.text(.71,.69,r'$\mathcal{I}^+$',ha='center',fontsize=14)
ax.text(.71,-.75,r'$\mathcal{I}^-$',ha='center',fontsize=14)
ax.text(1.16,0,r'$i^0$',ha='center',va='center',fontsize=14)
ax.text(0,1.15,r'$i^+$',ha='center',fontsize=14);ax.text(0,-1.23,r'$i^-$',ha='center',fontsize=14)
ax.set_title('Exterior block',fontsize=14,pad=10)
ax=axes[1]
ax.add_patch(Polygon([(-1,0),(0,-1),(0,1)],facecolor='#ffeded',edgecolor='none'))
edge(ax,(-1,0),(0,1),future);edge(ax,(-1,0),(0,-1),past)
y=np.linspace(-1,1,61);x=.028*np.sin(np.arange(61)*np.pi/2)
ax.plot(x,y,color=singular,lw=2.6)
ax.text(-.38,0,'Interior\n'+r'$0<r<R$',ha='center',va='center',fontsize=13)
ax.text(-.73,.69,r'$H^+$',ha='center',color=future,fontsize=14)
ax.text(-.73,-.75,r'$H^-$',ha='center',color=past,fontsize=14)
ax.text(.18,0,r'$r=0$'+'\nTimelike\nsingularity',ha='left',va='center',color=singular,fontsize=12)
ax.set_title('Interior block',fontsize=14,pad=10)
for ax in axes:
 ax.plot([-1],[0],marker='o',markerfacecolor='white',markeredgecolor='#333333',markersize=7,zorder=4)
 ax.annotate('Ideal throat endpoint\n(not a spacetime point)',xy=(-1,0),xytext=(-1.40,-1.40),fontsize=10,ha='left',arrowprops={'arrowstyle':'-','color':'#555555'})
 ax.annotate('Future',xy=(1.2,1.05),xytext=(1.2,.45),fontsize=11,ha='center',arrowprops={'arrowstyle':'->','lw':1.5})
fig.suptitle(r'Extremal causal blocks: $R=r_0/\sqrt{2}$, $\kappa=0$',fontsize=16,y=.965)
fig.text(.5,.205,r'Glue exterior $H^+$ to interior $H^-$; then interior $H^+$ to the next exterior $H^-$.',ha='center',fontsize=12)
fig.text(.5,.15,'Repeat in both directions to obtain the maximal analytic extension.',ha='center',fontsize=12)
fig.text(.5,.09,'No inter-horizon diamond; no bifurcation surface. These are blocks, not one global embedding.',ha='center',fontsize=10.5)
fig.subplots_adjust(left=.03,right=.97,bottom=.28,top=.855,wspace=.12)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=100,facecolor='white',transparent=False)
plt.close(fig)
