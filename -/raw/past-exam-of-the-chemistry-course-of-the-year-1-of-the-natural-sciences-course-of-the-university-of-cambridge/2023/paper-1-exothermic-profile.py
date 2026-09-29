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

fig,ax=plt.subplots(figsize=(8,4.6),facecolor='white')
verts=[(0,0),(1,0),(1.6,0),(2.4,5),(3,5),(3.6,5),(4.1,-3),(5,-3),(6,-3)]
codes=[MplPath.MOVETO,MplPath.LINETO,MplPath.CURVE4,MplPath.CURVE4,MplPath.CURVE4,MplPath.CURVE4,MplPath.CURVE4,MplPath.CURVE4,MplPath.LINETO]
ax.add_patch(PathPatch(MplPath(verts,codes),fc='none',ec=BLUE,lw=2))
ax.plot([0,3.1],[0,0],ls=':',color='.5');ax.annotate('',(2.7,5),(2.7,0),arrowprops={'arrowstyle':'<->','color':ORANGE});ax.text(2.58,2.4,r'$E_{a,+}$',ha='right',color=ORANGE,fontsize=13)
for pos,t in [((.2,.5),'Reactants'),((4.9,-2.5),'Products'),((3,5.4),'Transition state')]:ax.text(*pos,t,ha='center',fontsize=12)
ax.annotate('',(6.4,0),(6.4,-3),arrowprops={'arrowstyle':'<->','color':'.25'});ax.text(6.5,-1.5,r'$\Delta E<0$',fontsize=11)
ax.set(xlim=(-.4,7.8),ylim=(-4.2,6.3),xlabel='Reaction coordinate',ylabel='Energy (schematic)');ax.spines[['top','right']].set_visible(False);ax.set_xticks([]);ax.set_yticks([])

fig.tight_layout();save(fig,'paper-1-exothermic-profile.png')
