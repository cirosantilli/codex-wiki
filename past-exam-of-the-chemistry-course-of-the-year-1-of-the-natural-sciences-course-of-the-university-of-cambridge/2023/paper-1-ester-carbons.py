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

fig,axs=plt.subplots(2,1,figsize=(9,6.2),facecolor='white')
for ax,isB in zip(axs,[True,False]):
 p=[(-.4,0),(.8,0),(2,0),(3.2,0),(4.4,.65),(5.6,0)]
 for i in range(5):bond(ax,p[i],p[i+1],2 if i==(3 if isB else 4) else 1)
 carbonyl=2 if isB else 1;ox=(p[carbonyl][0],1.25);bond(ax,p[carbonyl],ox,2);atom(ax,ox,'O')
 texts=['Me','O','','CH','CH',r'$CH_3$'] if isB else [r'$CH_3$','','O',r'$CH_2$','CH',r'$CH_2$']
 for pos,t in zip(p,texts):
  if t:atom(ax,pos,t)
 assignments={0:'51.3',2:'166.9',3:'122.5',4:'144.6',5:'17.9'} if isB else {0:'20.9',1:'170.6',3:'65.1',4:'132.3',5:'118.1'}
 for i,t in assignments.items():ax.text(p[i][0],p[i][1]-.72,t,ha='center',color=BLUE,fontsize=11)
 finish(ax,(-1.0,6.3),(-1.15,1.75),'B: spectrum 4' if isB else 'C: spectrum 3')

fig.tight_layout();save(fig,'paper-1-ester-carbons.png')
