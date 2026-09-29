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

fig,axs=plt.subplots(1,3,figsize=(13,4.6),facecolor='white')
ax=axs[0];C=(0,0);O=(0,1.15);bond(ax,C,O,2);atom(ax,O,'O');bond(ax,C,(-1.15,-.3));atom(ax,(-1.15,-.3),'Me');bond(ax,C,(1.15,-.3));atom(ax,(1.15,-.3),'OMe');atom(ax,(-1,-1.2),r'$EtO^-$');curly(ax,(-.75,-1.05),(-.08,-.12),-.25);curly(ax,(.06,.5),(.12,1.02),-.45);finish(ax,(-2,2),(-2.1,1.8),'1. Addition to the acyl carbon')
ax=axs[1];C=(0,0)
for pos,label in [((0,1.15),r'$O^-$'),((-1.2,0),'Me'),((1.2,0),'OMe'),((0,-1.15),'OEt')]:bond(ax,C,pos);atom(ax,pos,label)
curly(ax,(.18,1.03),(.12,.5),.4);curly(ax,(.55,.04),(1.03,.14),-.5);finish(ax,(-2,2),(-2.1,1.8),'2. Tetrahedral intermediate collapses')
ax=axs[2];C=(-.4,.3)
for pos,label,order in [((-.4,1.45),'O',2),((-1.5,0),'Me',1),((.7,0),'OEt',1)]:bond(ax,C,pos,order);atom(ax,pos,label)
atom(ax,(1.25,1.1),r'$+\ MeO^-$',size=12);ax.text(-.2,-1.0,r'$MeO^-+EtOH\rightleftharpoons MeOH+EtO^-$',ha='center',fontsize=11);finish(ax,(-2.3,2.1),(-2.1,1.8),'3. Ester product and proton exchange')

fig.tight_layout();save(fig,'paper-1-acyl-exchange.png')
