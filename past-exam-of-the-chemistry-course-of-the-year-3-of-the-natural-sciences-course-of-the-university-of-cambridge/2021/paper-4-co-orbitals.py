"""Original explanatory diagram; Python 3.14 with numpy and matplotlib.
The PNG basename is written to the current working directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Polygon
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save, BLUE, ORANGE
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained')
ax=axs[0];bond(ax,(0,0),(1.6,0));ax.add_patch(Ellipse((-.55,0),1.2,.75,fc='#dceafa',ec=BLUE));atom(ax,(0,0),'C');atom(ax,(1.6,0),'O');ax.text(-.7,0,'+',ha='center',va='center');ax.text(.4,-.9,'occupied 5σ; large carbon-end donor lobe',ha='center',fontsize=10)
finish(ax,(-1.5,2.6),(-1.3,1.2),'CO HOMO (schematic)')
ax=axs[1];bond(ax,(0,0),(1.6,0))
for x,size,signs in [(0,.8,['+','−']),(1.6,.5,['−','+'])]:
 for y,s in zip([.52,-.52],signs):
  ax.add_patch(Ellipse((x,y),size,.9,fc='#dceafa' if s=='+' else '#fff0dd',ec=BLUE));ax.text(x,y,s,ha='center',va='center')
atom(ax,(0,0),'C');atom(ax,(1.6,0),'O');ax.text(.65,-1.3,'empty 2π*; second component perpendicular',ha='center',fontsize=10)
finish(ax,(-.8,2.5),(-1.6,1.3),'CO LUMO pair (one component)')
save(fig,'paper-4-co-orbitals.png')
