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

fig,ax=plt.subplots(figsize=(9,3.8),facecolor='white')
p=[(0,0),(1.4,.7),(2.8,0),(4.2,.7),(5.6,0)]
for a,b in zip(p,p[1:]):bond(ax,a,b)
for idx,ox in [(1,(1.4,1.85)),(2,(2.8,-1.15))]:bond(ax,p[idx],ox,2);atom(ax,ox,'O')
for i,t in [(0,r'$CH_3$'),(3,r'$CH_2$'),(4,r'$CH_3$')]:atom(ax,p[i],t)
for pos,text in [((0,-.6),'23.7'),((4.2,1.25),'29.2'),((5.6,-.6),'7.0')]:ax.text(*pos,text,color=BLUE,ha='center',fontsize=12)
ax.annotate('',(1.4,-1.75),(2.8,-1.75),arrowprops={'arrowstyle':'|-|','color':BLUE})
ax.text(2.1,-2.15,'197.5 and 199.8: ordering unresolved',ha='center',color=BLUE,fontsize=11)
finish(ax,(-.8,6.4),(-2.5,2.35),'A: carbon shifts in ppm')

fig.tight_layout();save(fig,'paper-1-diketone-carbons.png')
