"""Compute and draw the complete C2 tensor-square crystal; output PNG to CWD."""
from pathlib import Path
from collections import deque
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

bf={(1,0):1,(2,1):2,(1,2):3}
be={(i,b):a for (i,a),b in bf.items()}
def f(i,p):
 a,b=p
 if int((i,a) in bf)>int((i,b) in be):
  v=bf.get((i,a));return None if v is None else (v,b)
 v=bf.get((i,b));return None if v is None else (a,v)
def component(high):
 distance={high:0};queue=deque([high]);edges=[]
 while queue:
  p=queue.popleft()
  for i in (1,2):
   q=f(i,p)
   if q is None:continue
   edges.append((p,q,i))
   if q not in distance:distance[q]=distance[p]+1;queue.append(q)
 return distance,edges
letters=['1','2',r'\bar2',r'\bar1']
fig,axs=plt.subplots(1,3,figsize=(10.6,6.6),gridspec_kw={'width_ratios':[1.35,1,.8]},facecolor='white')
for ax,high,title,number in zip(axs,[(0,0),(0,1),(0,3)],[r'$B(2\omega_1)$',r'$B(\omega_2)$',r'$B(0)$'],[10,5,1]):
 distance,edges=component(high);assert len(distance)==number
 pos={}
 for level in sorted(set(distance.values())):
  row=sorted(p for p,d in distance.items() if d==level)
  for j,p in enumerate(row):pos[p]=((j-(len(row)-1)/2)*1.75,-level)
 for p,q,i in edges:
  start,end=pos[p],pos[q];color={1:'#2563eb',2:'#c2410c'}[i]
  ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=13,linewidth=1.8,color=color,shrinkA=18,shrinkB=18))
  mx,my=(start[0]+end[0])/2,(start[1]+end[1])/2
  ax.text(mx+.14,my,str(i),ha='left',va='center',fontsize=12,color=color,bbox={'facecolor':'white','edgecolor':'none','pad':1})
 for (a,b),(x,y) in pos.items():
  ax.text(x,y,r'$'+letters[a]+r'\otimes'+letters[b]+'$',ha='center',va='center',fontsize=14,bbox={'boxstyle':'round,pad=.22','facecolor':'#f8fafc','edgecolor':'#9ca3af'})
 ax.set_title(title+f'\n{number} '+('vertex' if number==1 else 'vertices'),fontsize=15,pad=15)
 ax.set_xlim(-1.7,1.7);ax.set_ylim(-6.65,.5);ax.axis('off')
fig.suptitle('Tensor-square crystal: lowering arrows labelled by simple-root color',fontsize=13,y=.99)
fig.tight_layout(rect=(0,0,1,.94),pad=1.5)
fig.savefig(Path.cwd()/f'{Path(__file__).stem}.png',dpi=160,facecolor='white',transparent=False)
plt.close(fig)
