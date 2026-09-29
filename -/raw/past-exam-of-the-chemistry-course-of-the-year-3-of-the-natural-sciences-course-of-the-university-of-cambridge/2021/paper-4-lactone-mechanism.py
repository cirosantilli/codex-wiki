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
fig,axs=plt.subplots(1,3,figsize=(13,4.4),layout='constrained')
for ax,stage in zip(axs,range(3)):
 if stage<2:
  c1=np.array([0.,0.]);cs=[c1,[.4,-.8],[1.3,-.85],[2.,-.15],[1.5,.65]]
  for a,b in zip(cs,cs[1:]):bond(ax,a,b)
  bond(ax,c1,(-.6,.7),2);atom(ax,(-.6,.7),'O');bond(ax,c1,(-.85,-.45));atom(ax,(-.85,-.45),'CN')
  atom(ax,c1,'C1',size=10);atom(ax,cs[-1],'C2⁻' if stage==0 else 'C2H',size=10)
  bond(ax,cs[-1],(1.55,1.5));atom(ax,(1.55,1.5),'OH' if stage==0 else 'O⁻',color=ORANGE)
  bond(ax,cs[-1],(2.5,1.0));atom(ax,(2.5,1.0),'CO₂Et',size=10)
  if stage==0:ax.text(.9,-1.65,'Proton transfer: C2⁻ + OH → C2–H + O⁻',ha='center',fontsize=10)
  else:curly(ax,(1.35,1.5),(.1,.15),.3);ax.text(.9,-1.65,'O attacks acyl cyanide; CN⁻ is expelled',ha='center',fontsize=10)
 else:
  pts=[[-.5,.6],[.5,1.0],[1.3,.5],[1.4,-.5],[.5,-1.0],[-.5,-.5]];ring(ax,pts)
  atom(ax,pts[0],'C1',size=10);atom(ax,pts[1],'O',color=ORANGE);atom(ax,pts[2],'C2H',size=10)
  bond(ax,pts[0],(-1.2,1.2),2);atom(ax,(-1.2,1.2),'O');bond(ax,pts[2],(2.25,.9));atom(ax,(2.25,.9),'CO₂Et',size=10)
  ax.text(.5,-1.65,'Six-membered lactone + regenerated CN⁻',ha='center',fontsize=10)
 finish(ax,(-1.5,3.0),(-2.,2.1),['After retro-Dieckmann cleavage','Alkoxide/acyl-cyanide intermediate','Lactonization product'][stage])
fig.suptitle('C1 = original ring ketone; C2 = original hydroxyl/ester-bearing carbon',fontsize=12)
save(fig,'paper-4-lactone-mechanism.png')
