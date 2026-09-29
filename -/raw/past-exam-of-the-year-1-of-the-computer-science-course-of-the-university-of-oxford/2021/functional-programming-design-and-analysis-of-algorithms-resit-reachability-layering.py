from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Circle,FancyBboxPatch
fig,ax=plt.subplots(figsize=(7.6,3.8),dpi=100,facecolor='white')
ax.set_facecolor('white');ax.set_xlim(-.6,7.3);ax.set_ylim(-1.8,2.0);ax.axis('off')
pos={'u':(.3,.7),'v':(1.5,.7),'w':(3.4,.7),'x':(5.3,.7),'y':(6.5,.7)}
for name,(x,y) in pos.items():
 ax.add_patch(Circle((x,y),.25,facecolor='#e6f0fa',edgecolor='#2166ac',lw=1.5));ax.text(x,y,name,ha='center',va='center',fontsize=13)
for u,v,rad in [('u','v',.35),('v','u',.35),('v','w',0),('w','x',0),('x','y',.35),('y','x',.35)]:
 a=FancyArrowPatch(pos[u],pos[v],arrowstyle='-|>',mutation_scale=14,shrinkA=21,shrinkB=21,connectionstyle=f'arc3,rad={rad}',color='#2166ac',lw=1.5);ax.add_patch(a)
for x,width,lab in [(.9,2.0,'C1 = {u,v}'),(3.4,1.25,'C2 = {w}'),(5.9,2.0,'C3 = {x,y}')]:
 ax.add_patch(FancyBboxPatch((x-width/2,-.1),width,1.65,boxstyle='round,pad=.05',edgecolor='#888888',facecolor='none',linestyle='--'))
 ax.text(x,-.45,lab,ha='center',fontsize=11)
for i,x in enumerate([.9,3.4,5.9],1):
 ax.add_patch(FancyBboxPatch((x-.7,-1.5),1.4,.55,boxstyle='round,pad=.05',facecolor='#fff1e8',edgecolor='#d6604d'))
 ax.text(x,-1.225,f'label {i}',ha='center',va='center',fontsize=12)
for a,b in [((1.65,-1.225),(2.65,-1.225)),((4.15,-1.225),(5.15,-1.225))]:ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=14,color='#d6604d',lw=1.5))
ax.set_title('Equal labels within cycles; ordered components between them',fontsize=12,pad=12)
fig.tight_layout();fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',transparent=False)
