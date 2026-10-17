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

fig,ax=plt.subplots(figsize=(9,4.1),facecolor='white')
p=[(0,0),(1.4,.7),(2.8,0),(4.2,.7),(5.6,0)]
for a,b in zip(p,p[1:]):bond(ax,a,b)
for idx,ox in [(1,(1.4,1.85)),(2,(2.8,-1.15))]:bond(ax,p[idx],ox,2);atom(ax,ox,'O')
for i,t in [(0,r'$CH_3^a$'),(3,r'$CH_2^b$'),(4,r'$CH_3^c$')]:atom(ax,p[i],t)
for pos,text in [((0,-.65),'a: 2.345; 3H; s'),((4.1,1.45),'b: 2.779; 2H; q'),((5.7,-.65),'c: 1.090; 3H; t')]:ax.text(*pos,text,color=BLUE,ha='center',fontsize=11)
ax.annotate('',(4.2,-1.45),(5.6,-1.45),arrowprops={'arrowstyle':'<->','color':ORANGE,'lw':1.7})
ax.text(4.9,-1.95,r'$J_{bc}=7.2$ Hz',ha='center',color=ORANGE,fontsize=12)
finish(ax,(-1.4,7.0),(-2.3,2.4),'A: proton assignment and scalar coupling')

fig.tight_layout();save(fig,'paper-1-diketone-protons.png')
