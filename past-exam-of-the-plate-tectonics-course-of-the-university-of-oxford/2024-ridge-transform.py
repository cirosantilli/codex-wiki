"""Original ridge-transform kinematics; PNG written in CWD.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig, ax = plt.subplots(figsize=(9,6.3),facecolor='white')
fig.subplots_adjust(left=.02,right=.98,top=.9,bottom=.12)
ax.add_patch(Polygon([(-5,-3.1),(-2,-3.1),(-2,0),(2,0),(2,3.1),(-5,3.1)],facecolor='#e2edf8',edgecolor='none'))
ax.add_patch(Polygon([(-2,-3.1),(5,-3.1),(5,3.1),(2,3.1),(2,0),(-2,0)],facecolor='#fff0d9',edgecolor='none'))
ax.plot([-5,-2],[0,0],ls='--',lw=2,color='#777777')
ax.plot([2,5],[0,0],ls='--',lw=2,color='#777777')
ax.plot([-2,2],[0,0],lw=4,color='#292929')
for x,y0,y1 in [(-2,-3.1,0),(2,0,3.1)]:
    for dx in [-.055,.055]: ax.plot([x+dx,x+dx],[y0,y1],lw=2,color='#bc4b38')
def arrow(x0,x1,y):
    ax.annotate('',xy=(x1,y),xytext=(x0,y),arrowprops={'arrowstyle':'-|>','lw':2.2,'color':'#283f58','mutation_scale':18})
for y in [-2,2]:
    ridge=-2 if y<0 else 2
    arrow(ridge-.25,ridge-1.5,y)
    arrow(ridge+.25,ridge+1.5,y)
arrow(.85,-.85,.62)
arrow(-.85,.85,-.62)
ax.text(0,1.03,'Upper side moves left',ha='center',fontsize=11)
ax.text(0,-1.15,'Lower side moves right',ha='center',fontsize=11)
ax.text(-3.6,.23,'A: inactive fracture zone',ha='center',fontsize=10)
ax.text(0,.15,'B: active left-lateral transform',ha='center',va='bottom',fontsize=11,weight='bold')
ax.text(-2.18,-1.15,'C: normal faulting\nat spreading ridge',ha='right',fontsize=11)
ax.text(2.2,2.75,'Spreading ridge',ha='left',fontsize=10,color='#9c382b')
ax.text(-4.5,2.8,'Plate 1',fontsize=12,color='#345678')
ax.text(3.4,-2.8,'Plate 2',fontsize=12,color='#815922')
ax.set(xlim=(-5,5),ylim=(-3.25,3.35),aspect='equal')
ax.axis('off')
ax.set_title('Determine slip from divergence at the ridge axes',fontsize=14,pad=14)
fig.text(.5,.025,'Local axes rotated for clarity. Arrows are constructed plate velocities, not source-image pointers.',ha='center',fontsize=9)
fig.savefig(Path.cwd()/'2024-ridge-transform.png',dpi=140,facecolor='white',metadata={'Software':'codex-wiki matplotlib generator'})
plt.close(fig)
