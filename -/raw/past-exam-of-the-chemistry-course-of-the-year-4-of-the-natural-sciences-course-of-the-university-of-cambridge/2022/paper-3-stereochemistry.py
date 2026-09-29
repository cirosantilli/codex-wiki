"""Original solution diagram. Python 3.14, NumPy and Matplotlib.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, wedge, save
plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig,axes=plt.subplots(1,2,figsize=(11,4.1))
ax=axes[0];ax.set_aspect('equal');ax.set_axis_off()
p=np.array([[0,2],[0,1],[1,.5],[1,-.5],[2,-1],[3,-.5],[3,.5],[4,1],[4,2]])
for a,b in zip(p[:-1],p[1:]):bond(ax,a,b)
for i in [0,8]:atom(ax,p[i],r'CH$_2$OH')
for a,b in [(p[1],(-.7,.6)),(p[7],(4.7,.6))]:bond(ax,a,b);atom(ax,b,'Me')
for i,ox,front in [(1,(.15,.1),False),(6,(3.85,.1),True)]:
 for v in [p[i],p[i+1]]:wedge(ax,v,ox,front=front)
 atom(ax,ox,'O')
for i,end in [(3,(.3,-1.05)),(5,(3.7,-1.05))]:wedge(ax,p[i],end,front=False);atom(ax,end,'OR')
ax.text(2,-1.65,r'$R=\mathrm{CH_2CO_2tBu}$',ha='center');ax.set(xlim=(-1,5),ylim=(-2,2.6));ax.set_title('37(a): diepoxide product')
ax=axes[1];ax.set_aspect('equal');ax.set_axis_off()
ax.add_patch(plt.Circle((0,0),.22,color='white',ec='black'))
bond(ax,(0,0),(-1,0));bond(ax,(0,0),(1,0));atom(ax,(-1.4,0),'TMS side');atom(ax,(1.6,0),'aldol side')
bond(ax,(0,0),(0,-1));bond(ax,(0,0),(0,1));atom(ax,(0,-1.3),'O');atom(ax,(0,1.35),r'N(iPr)$_2$')
ax.text(0,-2.05,r'View aryl $\rightarrow$ carbonyl: $S_a$ model',ha='center');ax.text(0,-2.55,r'New alcohol: $R$',ha='center')
ax.set(xlim=(-2.5,2.7),ylim=(-2.9,2));ax.set_title('37(b): specified axial projection')
fig.tight_layout();save(fig,'paper-3-stereochemistry.png')
