"""Original solution diagram. Python 3.14 / matplotlib 3.10 / numpy 2.3.
Run from the mirrored media directory; output is written to cwd.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import bond,atom,ring,curly,flow,finish,save,BLUE,ORANGE

fig,axs=plt.subplots(1,4,figsize=(11,5));fig.subplots_adjust(left=.04,right=.99,bottom=.16,top=.87,wspace=.4)
for ax,name in zip(axs,['N₂','O₂','Li₂','Be₂']):
 ax.set(xlim=(-1.1,1.2),ylim=(-.5,7));ax.set_title(name,fontsize=16);ax.axis('off');ax.annotate('',(-1,6.8),(-1,-.1),arrowprops={'arrowstyle':'->','color':'0.4'})
 if name=='N₂':levels=[(0,1,2,'σ2s'),(1,1,2,'σ*2s'),(2.8,2,4,'π2p'),(3.8,1,2,'σ2p'),(5.2,2,0,'π*2p'),(6.2,1,0,'σ*2p')]
 elif name=='O₂':levels=[(0,1,2,'σ2s'),(1,1,2,'σ*2s'),(2.8,1,2,'σ2p'),(3.8,2,4,'π2p'),(5.2,2,2,'π*2p'),(6.2,1,0,'σ*2p')]
 else:levels=[(0,1,2,'σ2s'),(1.2,1,0 if name=='Li₂' else 2,'σ*2s'),(3.5,2,0,'π2p'),(4.5,1,0,'σ2p'),(5.5,2,0,'π*2p'),(6.4,1,0,'σ*2p')]
 for y,d,n,label in levels:
  xs=[0] if d==1 else [-.38,.38]
  for i,x in enumerate(xs):
   ax.plot([x-.23,x+.23],[y,y],color=BLUE,lw=1.6)
   occ=min(2,n) if d==1 else (2 if n==4 else (1 if n==2 else 0))
   if occ:ax.text(x,y+.1,'↑↓' if occ==2 else '↑',ha='center',fontsize=16)
  ax.text(.82,y,label,fontsize=9,va='center',rotation=0)
fig.suptitle('Qualitative valence MO occupancies · 1s cores omitted',fontsize=14)
fig.text(.5,.06,'Vertical spacing is schematic. Li₂/Be₂ empty 2p energies are qualitative; O₂ has two π* SOMOs.',ha='center',fontsize=10)
save(fig,Path(__file__).with_suffix('.png').name)
