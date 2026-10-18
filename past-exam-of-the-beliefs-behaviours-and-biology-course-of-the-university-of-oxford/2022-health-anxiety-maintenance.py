"""Original hypothesized maintenance loop. Python 3.14.4, Matplotlib 3.10.7; output in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,ax=plt.subplots(figsize=(7.6,4.4),dpi=100,facecolor='white')
fig.subplots_adjust(left=.015,right=.985,bottom=.035,top=.97)
ax.set(xlim=(0,12),ylim=(0,7));ax.axis('off')
def node(x,y,w,text,color='#edf4f8'):
 ax.add_patch(FancyBboxPatch((x-w/2,y-.46),w,.92,boxstyle='round,pad=.04,rounding_size=.12',facecolor=color,edgecolor='#36546b',linewidth=1.3,zorder=3))
 ax.text(x,y,text,ha='center',va='center',zorder=4)
def arrow(a,b,rad=0,color='#536674',dashed=False):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,linewidth=1.6,color=color,connectionstyle=f'arc3,rad={rad}',linestyle='--' if dashed else '-'))
node(1.6,5.65,2.5,'Bodily change /\nhealth information')
node(5.6,5.65,2.7,'Threatening\ninterpretation')
node(10,5.65,2.6,'Anxiety and\nbodily monitoring')
node(10,3.25,2.6,'Further noticed\nsensations')
node(5.6,3.25,2.7,'Checking / repeated\nreassurance seeking')
node(5.6,1.25,2.7,'Short-lived relief;\ndoubt persists',color='#fcf1e8')
arrow((2.9,5.65),(4.2,5.65))
arrow((7.0,5.65),(8.65,5.65))
arrow((10,5.14),(10,3.76))
arrow((8.65,3.25),(6.55,5.13),rad=-.08)
arrow((5.6,5.14),(5.6,3.76))
arrow((5.6,2.74),(5.6,1.76))
arrow((4.2,1.25),(4.2,3.25),rad=-.5,color='#aa5c2c',dashed=True)
ax.text(2.05,2.15,'Immediate relief\nreinforces repetition',ha='center',color='#9a5025',fontsize=10.5)
ax.text(8.25,4.65,'Interpreted as\nfurther evidence',ha='center',va='center',fontsize=10,color='#36546b')
ax.text(6,.15,'Proposed maintaining processes, not an inevitable response or a diagnostic rule.',ha='center',fontsize=10,color='#4a5964')
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
plt.close(fig)
