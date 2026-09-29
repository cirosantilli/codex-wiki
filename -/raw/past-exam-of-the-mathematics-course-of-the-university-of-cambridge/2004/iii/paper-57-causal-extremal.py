"""Original extremal conformal blocks and their maximal-extension gluing.
Python 3.14; Matplotlib and NumPy. Fixed PNG basename to caller CWD.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig,axes=plt.subplots(1,2,figsize=(9.0,5.4),facecolor='white')
future='#175b91';past='#77438e';red='#ab2538';dark='#333333'
def line(ax,a,b,color,lw=2):ax.plot([a[0],b[0]],[a[1],b[1]],color=color,lw=lw)
for ax in axes:
 ax.axis('off');ax.set_aspect('equal');ax.set_facecolor('white');ax.set_xlim(-1.6,1.6);ax.set_ylim(-1.35,1.45)
ax=axes[0]
ax.add_patch(Polygon([(-1,0),(0,1),(1,0),(0,-1)],facecolor='#edf4ea',edgecolor='none'))
line(ax,(-1,0),(0,1),future);line(ax,(-1,0),(0,-1),past)
line(ax,(0,1),(1,0),dark);line(ax,(0,-1),(1,0),dark)
ax.text(0,0,'Exterior E\n'+r'$r>r_h$',ha='center',va='center',fontsize=12)
ax.text(-.77,.60,r'$H^+$',color=future,fontsize=12);ax.text(-.77,-.74,r'$H^-$',color=past,fontsize=12)
ax.text(.65,.64,r'$\mathcal{I}^+$',fontsize=12);ax.text(.65,-.77,r'$\mathcal{I}^-$',fontsize=12)
ax.text(1.11,0,r'$i^0$',fontsize=11);ax.text(0,1.12,r'$i^+$',ha='center',fontsize=11);ax.text(0,-1.24,r'$i^-$',ha='center',fontsize=11)
ax.set_title('Static exterior block',fontsize=12)
ax=axes[1]
ax.add_patch(Polygon([(-1,0),(0,-1),(0,1)],facecolor='#fae9ec',edgecolor='none'))
line(ax,(-1,0),(0,1),future);line(ax,(-1,0),(0,-1),past)
y=np.linspace(-1,1,121);x=.019*np.sin(np.arange(121)*np.pi/2)
ax.plot(x,y,color=red,lw=2.5)
ax.text(-.34,0,'Interior I\n'+r'$0<r<r_h$',ha='center',va='center',fontsize=11)
ax.text(-.77,.60,r'$H^+$',color=future,fontsize=12);ax.text(-.77,-.74,r'$H^-$',color=past,fontsize=12)
ax.text(.14,0,r'$r=0$'+'\nTimelike\nsingularity',ha='left',va='center',color=red,fontsize=11)
ax.set_title('Static interior block',fontsize=12)
for ax in axes:
 ax.plot([-1],[0],marker='o',mfc='white',mec=dark,ms=7,zorder=5)
 ax.annotate('Ideal throat endpoint',xy=(-1,0),xytext=(-1.53,-1.24),fontsize=9,arrowprops={'arrowstyle':'-','color':'#777777'})
fig.suptitle(r'Extremal blocks: $|Q|=M$, $r_h=\sqrt{M}$, $\kappa=0$',fontsize=13,y=.97)
fig.text(.5,.17,'Glue E future horizon to I past horizon, then I future horizon to the next E past horizon.',ha='center',fontsize=9.5)
fig.text(.5,.11,'Repeat upward and downward: this rule specifies the maximal extension.',ha='center',fontsize=10)
fig.text(.5,.05,'There is no trapped inter-horizon block and no regular bifurcation event.',ha='center',fontsize=10)
fig.subplots_adjust(left=.025,right=.975,bottom=.23,top=.875,wspace=.10)
fig.savefig(Path.cwd()/'paper-57-causal-extremal.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
