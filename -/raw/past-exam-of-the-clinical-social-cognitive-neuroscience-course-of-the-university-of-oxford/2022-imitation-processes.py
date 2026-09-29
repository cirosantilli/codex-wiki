"""Original functional diagram of psychological requirements for imitation.

Python 3.14.4 / Matplotlib 3.10.7, using existing pyproject dependencies.
No experimental data, anatomical modules or quantitatively fitted model.
Writes its same-basename opaque PNG to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig,ax=plt.subplots(figsize=(9.2,4.2),dpi=100,facecolor='white')
fig.subplots_adjust(left=.02,right=.98,bottom=.03,top=.88)
ax.set(xlim=(0,10),ylim=(0,4));ax.axis('off')
def box(x,y,w,h,title,sub,color='#edf3f8'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.04',facecolor=color,edgecolor='#42627a',lw=1.1))
 ax.text(x+w/2,y+h*.70,title,ha='center',va='center',weight='bold',fontsize=10)
 ax.text(x+w/2,y+h*.32,sub,ha='center',va='center',fontsize=9,linespacing=1.4)
def arrow(a,b,rad=0):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=12,color='#42627a',lw=1.3,connectionstyle=f'arc3,rad={rad}'))
items=[('Perceive','Attend to an action\nand its context'),('Represent','Select means, goal\nor sequence'),('Transform','Map another body\nto one’s own action'),('Execute','Plan, monitor\nand correct')]
for i,(t,sub) in enumerate(items):
 x=.15+2.5*i;box(x,2.12,2.15,1.15,t,sub)
 if i<3:arrow((x+2.18,2.70),(x+2.43,2.70))
arrow((8.68,2.08),(3.72,2.08),rad=-.19)
ax.text(6.18,1.50,'Feedback, attention and control can alter several stages',ha='center',fontsize=9)
for x,t,sub in [(.3,'Outcome control','Same result does not\nprove copied means'),(3.7,'Spatial control','Location compatibility is\nnot action matching'),(7.1,'Performance control','Retention and motor ability\ncan limit expression')]:
 box(x,.22,2.6,.94,t,sub,color='#faf1df')
fig.suptitle('Imitation is a coordinated task, not one undifferentiated ability',fontsize=13,y=.97)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False,dpi=100,metadata={'Software':'Matplotlib','Description':'Original functional schematic of imitation task requirements'})
plt.close(fig)
