"""Three-state progression diagram. Python 3.14, matplotlib 3.10.7.

Output is the PNG basename in the current working directory. MPLCONFIGDIR is
supplied by the caller; this generator does not alter it or copy media files.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
fig,ax=plt.subplots(figsize=(7.8,3.2),dpi=100,facecolor='white')
ax.set(xlim=(0,7.8),ylim=(0,3.2));ax.axis('off')
places={1:(1.2,2.35),2:(6.6,2.35),3:(3.9,.65)}
for i,text in [(1,'1: mild'),(2,'2: severe'),(3,'3: death')]:
 x,y=places[i]
 ax.add_patch(FancyBboxPatch((x-.8,y-.35),1.6,.7,boxstyle='round,pad=0.08',facecolor='#eef3fa' if i!=3 else '#f3eeee',edgecolor='#263238',linewidth=1.5))
 ax.text(x,y,text,ha='center',va='center',fontsize=13)
for start,end,label,xy in [((2.1,2.35),(5.7,2.35),'$q_{12}$',(3.9,2.58)),((1.45,1.97),(3.08,.89),'$q_{13}$',(1.98,1.32)),((6.34,1.97),(4.72,.89),'$q_{23}$',(5.85,1.32))]:
 ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=17,linewidth=1.7,color='#263238'));ax.text(*xy,label,fontsize=15,ha='center',va='center')
ax.text(3.9,.06,'Death is absorbing; progression cannot reverse.',ha='center',va='bottom',fontsize=10,color='#444444')
fig.subplots_adjust(left=.01,right=.99,bottom=.025,top=.99)
fig.savefig('paper-32-multistate.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
