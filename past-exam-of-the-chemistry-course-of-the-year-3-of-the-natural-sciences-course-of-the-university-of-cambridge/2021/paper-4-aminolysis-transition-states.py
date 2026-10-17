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
fig,axs=plt.subplots(1,2,figsize=(11,5.4),layout='constrained')
for ax,assisted in zip(axs,[False,True]):
 C=np.array([0.,0.]);N=np.array([-1.,.8]);O=np.array([1.,.8]);bond(ax,C,N);bond(ax,C,O,style='dashed');atom(ax,C,'C',size=12);atom(ax,N,'N(H)R',size=12);atom(ax,O,'O–Ar',size=12)
 bond(ax,C,(0,-.9));bond(ax,(.07,-.1),(.07,-.8),style='dashed');atom(ax,(0,-.9),'O',size=13);bond(ax,C,(-.9,-.6));atom(ax,(-.9,-.6),'OEt',size=11)
 if assisted:
  h1=(-1.,1.65);nb=(0,2.15);h2=(1.,1.65)
  for a,b in [(N,h1),(h1,nb),(nb,h2),(h2,O)]:bond(ax,a,b,style='dashed',color=ORANGE)
  atom(ax,h1,'H');atom(ax,nb,'N(H)R');atom(ax,h2,'H')
 else:
  H=(0.,1.75);bond(ax,N,H,style='dashed',color=ORANGE);bond(ax,H,O,style='dashed',color=ORANGE);atom(ax,H,'H')
 ax.text(0,-1.6,'Dashed: coupled bond changes; not measured distances',ha='center',fontsize=10)
 finish(ax,(-2.2,2.2),(-2,2.8),'Six-centre amine-assisted relay' if assisted else 'Four-centre direct proton relay')
fig.suptitle('Proposed tetrahedral-intermediate breakdown transition states (‡)',fontsize=13)
save(fig,'paper-4-aminolysis-transition-states.png')
