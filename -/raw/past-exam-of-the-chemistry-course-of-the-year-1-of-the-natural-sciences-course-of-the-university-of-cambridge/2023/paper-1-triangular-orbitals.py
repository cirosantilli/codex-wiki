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

fig,axs=plt.subplots(1,2,figsize=(10,5),facecolor='white')
for ax,third in zip(axs,[False,True]):
 for x in [.5,2]:ax.plot([x-.35,x+.35],[2,2],color='black',lw=1.5)
 ax.plot([.9,1.6],[-.3,-.3],color='black',lw=1.5);ax.text(1.25,-.15,'↑↓',ha='center',fontsize=18)
 if third:ax.text(.5,2.15,'↑',ha='center',fontsize=18)
 ax.text(2.6,2,r"$e':\ \alpha-\beta$",va='center',fontsize=12);ax.text(2.05,-.3,r"$a_1':\ \alpha+2\beta$",va='center',fontsize=12)
 pts=np.array([[.5,-2.2],[2,-2.2],[1.25,-.9]])
 for i in range(3):bond(ax,pts[i],pts[(i+1)%3])
 for pt in pts:ax.add_patch(Circle(pt,.23,fc=BLUE,alpha=.3));atom(ax,pt,'+',size=13)
 ax.text(1.25,-2.8,'Fully bonding combination: same phase on all three sites',ha='center',fontsize=9)
 finish(ax,(-.4,5),(-3.1,3.1),'Three electrons: upper degeneracy occupied' if third else 'H₃⁺: two-electron closed shell')
fig.text(.5,.01,'A third electron occupies e′ and permits a Jahn–Teller distortion; this diagram alone does not prove dissociation.',ha='center',fontsize=10)

fig.tight_layout();save(fig,'paper-1-triangular-orbitals.png')
