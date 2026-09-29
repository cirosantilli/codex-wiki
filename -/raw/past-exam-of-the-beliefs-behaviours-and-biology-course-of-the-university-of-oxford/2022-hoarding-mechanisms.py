"""Original schematic. Python 3.14.4, Matplotlib 3.10.7. Writes PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,ax=plt.subplots(figsize=(7.6,4.0),dpi=100,facecolor='white')
fig.subplots_adjust(left=.015,right=.985,bottom=.03,top=.96)
ax.set(xlim=(0,12),ylim=(0,6));ax.axis('off')
def node(x,y,w,text,color='#edf4f8'):
 ax.add_patch(FancyBboxPatch((x-w/2,y-.4),w,.8,boxstyle='round,pad=.04,rounding_size=.1',facecolor=color,edgecolor='#36546b',linewidth=1.3,zorder=3))
 ax.text(x,y,text,ha='center',va='center',zorder=4)
def arrow(a,b):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,linewidth=1.5,color='#526474'))
ax.text(3,5.55,'Shared-process hypothesis',ha='center',fontsize=12.5,weight='bold')
ax.text(9,5.55,'Different-route hypothesis',ha='center',fontsize=12.5,weight='bold')
node(3,4.6,2.65,'Shared maintaining\nprocess')
for x,label in [(1.15,'Discarding\ndifficulty'),(3,'Accumulation'),(4.85,'Impairment')]:
 node(x,2.5,1.65,label)
 arrow((3,4.15),(x,2.95))
for x,label in [(7.1,'Process A'),(9,'Process B'),(10.9,'Process C')]:
 node(x,4.6,1.65,label)
 arrow((x,4.15),(9,2.95))
node(9,2.5,3,'Similar observed\nhoarding outcome')
ax.plot([6,6],[1.6,5.2],color='#c7d2da',lw=1)
ax.text(3,1.35,'Test covariance, course and\nresponses to targeted change',ha='center',va='center',color='#334e68',fontsize=10.5)
ax.text(9,1.35,'Test distinct routes with\nadditional indicators and interventions',ha='center',va='center',color='#334e68',fontsize=10.5)
ax.text(6,.35,'Schematic hypotheses: shared processes and multiple routes may coexist.',ha='center',fontsize=10,color='#4a5964')
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
plt.close(fig)
