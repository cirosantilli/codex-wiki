"""Original qualitative DEP schematic; Python 3.14/numpy/matplotlib.

Not a solved electric boundary-value problem. Force directions indicate the
high-field tip region; equal-gradient force magnitudes have ratio 8.
Output: PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Rectangle,Circle
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(10,4.3),layout='constrained')
fig.patch.set_facecolor('white')
for ax,sign,title in zip(axes,[1,-1],['Positive DEP: towards strong field','Negative DEP: towards weak field']):
    ax.add_patch(Polygon([(-.7,-.7),(.25,-.2),(.25,.2),(-.7,.7)],facecolor='.75',edgecolor='.25'))
    ax.add_patch(Rectangle((4.25,-1.6),.35,3.2,facecolor='.75',edgecolor='.25'))
    xx=np.linspace(.25,4.25,180)
    for yy in [-1.4,-.9,-.45,0,.45,.9,1.4]:
        curve=yy*((xx-.25)/4)**.55
        ax.plot(xx,curve,color='.7',lw=.8,zorder=0)
    for pos,r,label,length in [(np.array([3.45,0]),.14,'1',.15),
                                (np.array([2.25,.9]),.28,'2',1.2)]:
        ax.add_patch(Circle(pos,r,facecolor='#647f8b',edgecolor='.2'))
        ax.text(*pos,label,color='white',ha='center',va='center',fontsize=10)
        direction=sign*(np.array([.25,0])-pos)
        direction=direction/np.linalg.norm(direction)
        start=pos+direction*(r+.025)
        end=start+direction*length
        ax.annotate('',end,start,arrowprops={'arrowstyle':'->','lw':2,'color':'#b6623e'})
    ax.text(.2,-1.95,'Narrow tip: strong field',fontsize=9,ha='center')
    ax.text(3.7,-1.95,'Broad electrode',fontsize=9,ha='center')
    ax.text(1.95,1.95,r'$R_2/R_1=2,\quad |F_2|/|F_1|=8$',ha='center',fontsize=11)
    ax.set(xlim=(-.9,4.8),ylim=(-2.2,2.2),aspect='equal',title=title)
    ax.axis('off')
fig.savefig('paper-2-dielectrophoresis.png',dpi=150,facecolor='white')
plt.close(fig)
