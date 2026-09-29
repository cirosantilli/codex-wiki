"""Draw the shared feedback streams; write the PNG to the current directory."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams.update({'font.size': 13, 'font.family': 'DejaVu Sans'})
fig, axes = plt.subplots(1, 2, figsize=(13, 5.6), dpi=100, facecolor='white', gridspec_kw={'width_ratios':[1.15,1]})
ax=axes[0]
ax.set(xlim=(-.4,6.8),ylim=(0,5.7))
ax.axis('off')
ax.set_title('One shared list and its feedback',fontsize=17)
nodes={'h':(.7,3),'two':(2.8,4.2),'three':(2.8,3),'five':(2.8,1.8),'inner':(4.3,2.4),'outer':(5.9,3.5)}
labels={'h':'h = 1 : tail','two':'map × 2','three':'map × 3','five':'map × 5','inner':'merge','outer':'merge'}
for key,(x,y)in nodes.items():
    ax.text(x,y,labels[key],ha='center',va='center',bbox={'boxstyle':'round,pad=.45','facecolor':'#e8f0fa','edgecolor':'#365b85'},zorder=3)
for u,v in [('h','two'),('h','three'),('h','five'),('two','outer'),('three','inner'),('five','inner'),('inner','outer')]:
    ax.add_patch(FancyArrowPatch(nodes[u],nodes[v],arrowstyle='-|>',mutation_scale=15,shrinkA=38,shrinkB=32,color='#365b85',lw=1.5))
ax.plot([5.9,5.9,.7,.7],[3.8,5.0,5.0,3.4],color='#365b85',lw=1.5)
ax.annotate('',(.7,3.37),(.7,3.8),arrowprops={'arrowstyle':'-|>','color':'#365b85','lw':1.5})
ax.text(3.3,5.12,'merged tail feeds back',ha='center',fontsize=12,color='#365b85')
ax.text(3.1,.65,'All three maps reuse h; none recomputes a separate copy.',ha='center',fontsize=11)
ax=axes[1]
ax.set(xlim=(0,6),ylim=(0,5.7))
ax.axis('off')
ax.set_title('Frontier after six outputs',fontsize=17)
ax.text(3,4.8,'h = [1, 2, 3, 4, 5, 6, …]',ha='center',fontsize=16)
rows=[(2,'2, 4, 6',8,4,'#176e4b'),(3,'3, 6',9,3,'#65469a'),(5,'5',10,2,'#a25416')]
for i,(factor,consumed,pending,base,color)in enumerate(rows):
    y=3.65-i
    ax.text(.2,y,f'× {factor}',weight='bold',color=color)
    ax.text(1.1,y,f'consumed {consumed}',color=color,fontsize=12)
    ax.text(1.1,y-.35,f'next {pending} = {factor} × h[{base}]',color=color,fontsize=12)
ax.text(3,.45,'h[k] means the kth cell, counting from 1.\nPending candidates need not yet be evaluated.',ha='center',fontsize=11)
fig.subplots_adjust(left=.025,right=.98,bottom=.02,top=.88,wspace=.18)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white')
plt.close(fig)
