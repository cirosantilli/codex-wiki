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
fig,axs=plt.subplots(1,3,figsize=(13,5),layout='constrained')
patterns=[(np.array([[1,1],[-2,2]]),[np.array([.5,0]),np.array([0,1.5])],'Observed: p(√2 × 2√2)R45°'),(np.array([[1,0],[0,2]]),[np.array([.5,0])],'Alternative: p(1 × 2)'),(np.array([[1,1],[-1,1]]),[np.array([.5,0])],'Alternative: p(√2 × √2)R45°')]
for ax,(B,basis,title) in zip(axs,patterns):
 for x in range(-2,5):
  for y in range(-1,5):ax.scatter(x,y,c='.8',s=22)
 for i in range(-7,8):
  for j in range(-7,8):
   for b in basis:
    p=b+i*B[0]+j*B[1]
    if -2.2<p[0]<4.2 and -1.2<p[1]<4.2:ax.scatter(*p,c=ORANGE,s=55,zorder=4)
 origin=np.array([0.,0.]);poly=np.array([origin,B[0],B[0]+B[1],B[1]]);ax.add_patch(Polygon(poly,fill=False,ec=BLUE,lw=1.8))
 for j,v in enumerate(B):flow(ax,origin,v,'b'+str(j+1))
 ax.set(xlim=(-2.3,4.3),ylim=(-1.3,4.4),xticks=range(-2,5),yticks=range(-1,5),xlabel='x / a',ylabel='y / a',title=title);ax.set_aspect('equal');ax.grid(alpha=.15)
fig.suptitle('Grey points: Pd; orange points: CO at bridge positions. All coverages = ½.',fontsize=12)
save(fig,'paper-4-overlayers.png')
