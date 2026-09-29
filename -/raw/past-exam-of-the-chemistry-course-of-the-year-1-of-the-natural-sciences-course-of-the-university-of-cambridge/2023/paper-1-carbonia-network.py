"""Original solution diagram; writes its PNG basename to the current directory."""
from pathlib import Path
import sys
for ancestor in Path(__file__).resolve().parents:
    if (ancestor/'tools'/'chemistry_diagram.py').exists():
        sys.path.insert(0,str(ancestor/'tools'));break
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, PathPatch
from matplotlib.path import Path as MplPath
from chemistry_diagram import bond, atom, curly, wedge, finish, save, BLUE, ORANGE

fig,ax=plt.subplots(figsize=(9,5.7),facecolor='white')
centres=[np.array([0.,0.]),np.array([3.,1.732]),np.array([-3.,1.732])]
shared=[np.array([1.5,.866]),np.array([-1.5,.866])]
for pos in shared:
 for C in [centres[0],centres[1] if pos[0]>0 else centres[2]]:bond(ax,C,pos)
 atom(ax,pos,'O',color=ORANGE)
for j,C in enumerate(centres):
 ends=[C+np.array([-.6,-1.1]),C+np.array([.6,-1.1])] if j==0 else [C+np.array([-.45,1.15]),C+np.array([.45,1.15]),C+np.array([1.3 if j==1 else -1.3,-.75])]
 for i,O in enumerate(ends):
  if i==0:wedge(ax,C,O,True)
  elif i==1:wedge(ax,C,O,False)
  else:bond(ax,C,O)
  atom(ax,O,'O',color=ORANGE);direction=(O-C)/np.linalg.norm(O-C);bond(ax,O+.15*direction,O+.65*direction,style='dashed',color='.5');ax.text(*(O+.9*direction),'C…',fontsize=10,color='.4',ha='center')
 atom(ax,C,'C',color=BLUE)
ax.text(0,-2.55,r'Four O neighbours per C; each O is shared: $O/C=4/2=2$',ha='center',fontsize=11)
finish(ax,(-5.6,5.6),(-3.0,4.3),'Representative nonmolecular CO₂ connectivity; bonds continue beyond the fragment')

fig.tight_layout();save(fig,'paper-1-carbonia-network.png')
