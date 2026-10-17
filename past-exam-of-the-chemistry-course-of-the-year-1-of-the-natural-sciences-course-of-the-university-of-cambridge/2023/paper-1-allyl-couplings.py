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

fig,axs=plt.subplots(2,1,figsize=(10,7.2),facecolor='white',gridspec_kw={'height_ratios':[1.2,1]})
ax=axs[0];p=[(-4,-.7),(-2.8,-.7),(-1.6,-.7),(-.4,-.7),(.8,0),(2.2,0)]
for i in range(5):bond(ax,p[i],p[i+1],2 if i==4 else 1)
bond(ax,p[1],(-2.8,-1.8),2);atom(ax,(-2.8,-1.8),'O')
for idx,t in [(0,r'$CH_3^a$'),(2,'O'),(3,r'$CH_2^b$')]:atom(ax,p[idx],t)
for start,end,t in [(p[4],(.5,1.1),r'$H_c$'),(p[5],(3.1,-.85),r'$H_d$'),(p[5],(3.1,.85),r'$H_e$')]:bond(ax,start,end);atom(ax,end,t)
for pos,t in [((-4,-1.35),'2.081; 3H; s'),((-.5,-1.5),'4.570; 2H; dt'),((.4,1.7),'5.919; 1H; ddt'),((3.1,-1.4),'5.314; 1H; dq'),((3.1,1.4),'5.235; 1H; dq')]:ax.text(*pos,t,ha='center',fontsize=10,color=BLUE)
finish(ax,(-5.0,4.4),(-2.25,2.0),'C: terminal hydrogens d and e are trans and cis to c')
ax=axs[1];nodes={'b':(-2,0),'c':(0,0),'d':(2,1),'e':(2,-1)}
for key,pos in nodes.items():atom(ax,pos,key,size=15,color=BLUE)
for a,b,label,rad in [('b','c','6.0',0),('c','d','17.1 (trans)',0),('c','e','10.5 (cis)',0),('d','e','1.5 (geminal)',0),('b','d','1.5 (long-range)',-.40),('b','e','1.5 (long-range)',.40)]:
 x,y=np.array(nodes[a]),np.array(nodes[b]);v=y-x;u=v/np.linalg.norm(v)
 ax.add_patch(FancyArrowPatch(x+.18*u,y-.18*u,arrowstyle='<->',mutation_scale=12,connectionstyle=f'arc3,rad={rad}',color=ORANGE,lw=1.3))
 mid=(x+y)/2
 if a=='d':mid+=np.array([.9,0])
 elif a=='b' and b!='c':mid+=np.array([-.35,1.1 if b=='d' else -1.1])
 else:mid+=np.array([0,.22 if b!='e' else -.25])
 ax.text(*mid,label,ha='center',va='center',fontsize=10,color=ORANGE,bbox={'fc':'white','ec':'none','pad':1})
finish(ax,(-3,4),(-2.2,2.2),'Pairwise coupling map for the labelled protons above (Hz)')

fig.tight_layout();save(fig,'paper-1-allyl-couplings.png')
