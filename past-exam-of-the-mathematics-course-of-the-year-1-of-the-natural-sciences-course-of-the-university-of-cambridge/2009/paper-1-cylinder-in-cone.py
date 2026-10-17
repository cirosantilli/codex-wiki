"""Original axial geometry and normalized optima; write PNG into cwd."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(9,4.5),facecolor='white')
ax=axes[0];h=1;slope=.6;x=h/3;r=(h-x)*slope
ax.plot([-slope,0,slope,-slope],[0,h,0,0],color='gray',lw=2)
ax.add_patch(Rectangle((-r,0),2*r,x,facecolor='#247ba0',alpha=.22,edgecolor='#247ba0',lw=2))
ax.axvline(0,color='gray',lw=.7,ls=':')
ax.annotate('',(.8,1),(.8,0),arrowprops={'arrowstyle':'<->'});ax.text(.84,.5,'h',va='center')
ax.annotate('',(.48,x),(.48,0),arrowprops={'arrowstyle':'<->'});ax.text(.5,x/2,'x',va='center')
ax.annotate('',(r,x),(0,x),arrowprops={'arrowstyle':'<->'});ax.text(r/2,x+.04,'r',ha='center')
ax.text(0,-.12,'Axial section; volume optimum',ha='center');ax.set(xlim=(-.8,1),ylim=(-.2,1.15),aspect='equal');ax.axis('off')
u=np.linspace(0,1,500);axes[1].plot(u,u*(1-u)**2/(4/27),label='Volume / maximum volume',lw=2)
axes[1].plot(u,4*u*(1-u),label='Curved area / maximum area',lw=2)
for v in [1/3,.5]:axes[1].axvline(v,color='gray',ls=':',lw=1)
axes[1].set_xticks([0,1/3,.5,1],['0','1/3','1/2','1']);axes[1].set(xlabel='Height fraction x/h',ylabel='Fraction of the respective maximum',ylim=(0,1.12),title='Two objectives, different optima')
axes[1].legend(loc='lower center',fontsize=9);axes[1].grid(alpha=.18)
fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135,facecolor='white');plt.close(fig)
