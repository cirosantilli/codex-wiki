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
fig,axs=plt.subplots(1,3,figsize=(12,4.5),layout='constrained')
th=np.deg2rad(np.arange(6)*60+150);pts=np.column_stack([1.2*np.cos(th),1.2*np.sin(th)])
for ax,stage in zip(axs,range(3)):
 # Atom labels preserve the sequence C1,N2,C3,C4(OH),C5,C6 throughout.
 edges=[(0,1,2),(1,2,1),(2,3,1),(3,4,1),(4,5,2)] if stage==0 else [(0,1,1),(1,2,2),(3,4,2),(4,5,1),(5,0,1)] if stage==1 else [(0,1,1),(1,2,1),(3,4,1),(4,5,1),(5,0,1),(4,2,1)]
 for i,j,o in edges:bond(ax,pts[i],pts[j],o)
 labels=['CH₂-1','N⁺-2' if stage<2 else 'N-2','C3','C4','C5','CH₂-6']
 for p,l in zip(pts,labels):atom(ax,p,l,size=11)
 op=pts[3]+np.array([-.35,-.8]);bond(ax,pts[3],op,2 if stage==2 else 1);atom(ax,op,'O' if stage==2 else 'OH',color=ORANGE,size=12)
 if stage==0:
  for a,b,rad in [(pts[2]*.85,(pts[3]+pts[4])/2,.2),((pts[4]+pts[5])/2,(pts[5]+pts[0])/2,.3),((pts[0]+pts[1])/2,(pts[1]+pts[2])/2,.3)]:curly(ax,a,b,rad)
 if stage==1:curly(ax,(pts[3]+pts[4])/2,(pts[2]+pts[4])/2,.3)
 ax.text(0,-2.15,['Break C3–C4; form C1–C6','Enol C5 attacks iminium C3','New N2–C1–C6–C5–C3 ring'][stage],ha='center',fontsize=10)
 finish(ax,(-2.1,2.1),(-2.5,1.8),['N-methylene iminium array','After [3,3] rearrangement','After Mannich closure'][stage])
fig.suptitle('Only the numbered reacting array is shown; the unchanged rigid framework is omitted.',fontsize=12)
save(fig,'paper-4-aza-cope-mannich.png')
