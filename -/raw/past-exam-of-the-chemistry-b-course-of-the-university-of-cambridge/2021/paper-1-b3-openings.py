"""Original answer diagram, generated with Python 3.14 and root dependencies."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import atom,bond,ring,wedge,curly,flow,finish,save,chair,BLUE,GREEN,ORANGE

fig,axs=plt.subplots(3,2,figsize=(10,11),layout='constrained')
for j,ax in enumerate(axs[0]):
 pts,aa,eq=chair(ax,(0,0),phase=1 if j==0 else -1,scale=1.25)
 for idx,end,t in [(0,aa[0] if j==0 else eq[0],'Me'),(1,aa[1],'Cl'),(2,aa[2],'H')]:
  bond(ax,pts[idx],end,color=ORANGE if t=='Cl' else '.2');atom(ax,end,t,11)
 if j==1:bond(ax,pts[0],aa[0],color=BLUE);atom(ax,aa[0],'H',11,color=BLUE)
 ax.text(0,-1.7,'Axial Me blocks one beta H' if j==0 else 'Equatorial Me; both beta axial H available',ha='center',fontsize=9)
 finish(ax,(-2.65,2.65),(-2.1,1.8),'trans: minor reactive chair' if j==0 else 'cis: favored reactive chair')
th=np.pi/2-np.arange(6)*np.pi/3;p=np.column_stack([1.1*np.cos(th),1.1*np.sin(th)])
for j,ax in enumerate(axs[1]):
 ring(ax,p);atom(ax,p[0],'NH',12)
 ph=p[1]+[.85,.5];wedge(ax,p[1],ph,False);atom(ax,ph,'Ph',11)
 for idx,label,front,delta in [(3,'OH' if j==0 else r'N$_3$',True,[.45,-.8]),(4,r'N$_3$' if j==0 else 'OH',False,[-.9,-.45])]:
  end=p[idx]+delta;wedge(ax,p[idx],end,front);atom(ax,end,label,12)
 for ix,num in [(1,2),(3,4),(4,5)]:ax.text(p[ix,0]*.8,p[ix,1]*.8,str(num),fontsize=9,color=BLUE)
 finish(ax,(-2.5,2.5),(-2.35,1.9),'B3(c): Product 1, attack C5' if j==0 else 'B3(c): Product 2, attack C4')
for j,ax in enumerate(axs[2]):
 ring(ax,p)
 if j==0:
  for ix,label,front in [(1,r'N$_3$',False),(2,'OH',True),(4,r'N$_3$',False),(5,'OH',True)]:
   end=p[ix]*1.85;wedge(ax,p[ix],end,front);atom(ax,end,label,12)
 else:
  for ix in [1,4]:wedge(ax,p[ix],[0,0],False)
  atom(ax,[0,0],'S',15,color=ORANGE)
  for ix in [2,5]:
   end=p[ix]*1.85;wedge(ax,p[ix],end,True);atom(ax,end,'OH',12)
 for ix in [0,1,2,3,4,5]:ax.text(p[ix,0]*.78,p[ix,1]*.78,str(ix+1),fontsize=9,color=BLUE)
 finish(ax,(-2.55,2.55),(-2.3,2.3),'B3(d): A, successive double opening' if j==0 else 'B3(d): B, sulfur bridge on back face')
fig.suptitle('Numbering is local to the indicated question; wedges = up, hashes = down',fontsize=12)
save(fig,Path(__file__).with_suffix('.png').name)
