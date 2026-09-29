"""Original solution diagram; Python 3.14, matplotlib 3.10, numpy 2.3.
Run from the mirrored media directory: PNG basename is written to cwd.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import atom,bond,ring,curly,flow,finish,save,wedge,BLUE,ORANGE

fig,axs=plt.subplots(1,2,figsize=(10,4.7));fig.subplots_adjust(top=.83,bottom=.10,wspace=.16)
ax=axs[0];finish(ax,(-2.2,2.5),(-1.9,2),'Conrotatory opening gives the E,E diene')
p=[(-1.1,.8),(-.5,0),(.5,0),(1.1,.8)]
for i in range(3):bond(ax,p[i],p[i+1],2 if i in [0,2] else 1)
for a,b in [(p[0],(-1.9,.9)),(p[3],(1.9,.9)),(p[1],(-.7,-1))]:bond(ax,a,b);atom(ax,b,'Me')
ax.text(.1,-1.65,'s-cis conformer shown; both terminal methyls are outward.',ha='center',fontsize=10)
ax=axs[1];finish(ax,(-2.2,2.5),(-1.9,2),'Para-like endo major-product model')
p=[(-1,.5),(-1,-.5),(0,-1),(1,-.5),(1,.5),(0,1)];ring(ax,p,{0:2});bond(ax,p[0],(-1.8,1));atom(ax,(-1.8,1),'Me')
for i,end in [(2,(0,-1.75)),(5,(0,1.75))]:wedge(ax,p[i],end,True);atom(ax,end,'Me ↑',11)
wedge(ax,p[3],(2,-.9),False);atom(ax,(2,-.9),'CO₂Me ↓',11)
fig.text(.5,.035,'Terminal methyls cis; ester trans to both. Reflection gives the companion enantiomer.',ha='center',fontsize=11,color=BLUE)
save(fig,Path(__file__).with_suffix('.png').name)
