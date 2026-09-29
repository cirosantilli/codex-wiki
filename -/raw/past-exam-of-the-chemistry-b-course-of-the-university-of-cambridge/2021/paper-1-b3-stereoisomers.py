"""Original answer diagram, generated with Python 3.14 and root dependencies."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import atom,bond,ring,wedge,curly,flow,finish,save,chair,BLUE,GREEN,ORANGE

fig,axs=plt.subplots(4,2,figsize=(9.7,12),layout='constrained')
for j,ax in enumerate(axs[0]):
 th=np.arange(6)*np.pi/3;p=np.column_stack([np.cos(th),np.sin(th)]);ring(ax,p)
 ex=[2,0];bond(ax,p[0],ex,2);bond(ax,ex,[2.7,.65]);atom(ax,[2.7,.65],'Ph');bond(ax,ex,[2.7,-.65]);atom(ax,[2.7,-.65],'H',11)
 wedge(ax,p[3],[-2,.55],j==0);atom(ax,[-2,.55],r'CH$_2$Ph',11)
 wedge(ax,p[3],[-2,-.55],j!=0);atom(ax,[-2,-.55],'H',11)
 finish(ax,(-2.8,3.15),(-1.75,1.75),'Alkylidenecyclohexane: '+('one handedness' if j==0 else 'mirror image'))
# Perspective model with perpendicular spiro ring planes.
project=lambda x:np.array([.87*x[0]+.36*x[1]-.14*x[2],.14*x[0]-.38*x[1]+.82*x[2]])
for j,ax in enumerate(axs[1]):
 o=np.zeros(3);a=np.array([-2,0,0]);b=np.array([2,0,0])
 ra=[o,[-1,1,0],a,[-1,-1,0]];rb=[o,[1,0,1],b,[1,0,-1]]
 ring(ax,[project(x) for x in ra],color=BLUE);ring(ax,[project(x) for x in rb],color=GREEN)
 # Remote Ph/H pairs distinguish the handedness.
 for center,ph,hh in [(a,[-2.7,0,.9],[-2.7,0,-.9]),(b,[2.7,.9*(-1 if j else 1),0],[2.7,-.9*(-1 if j else 1),0])]:
  bond(ax,project(center),project(ph));atom(ax,project(ph),'Ph',11)
  bond(ax,project(center),project(hh));atom(ax,project(hh),'H',10)
 ax.text(0,-1.55,'perpendicular ring planes',ha='center',fontsize=9)
 finish(ax,(-3.15,3.15),(-1.9,1.9),'Spiro framework: '+('one handedness' if j==0 else 'mirror image'))
for row,(pf,cf) in enumerate([(True,True),(True,False)],start=2):
 for j,ax in enumerate(axs[row]):
  p=np.array([[0,-.8],[1,-.25],[.62,.95],[-.62,.95],[-1,-.25]])
  ring(ax,p);atom(ax,p[0],'P')
  pfront=pf if j==0 else not pf;cfront=cf if j==0 else not cf
  wedge(ax,p[0],[0,-1.8],pfront);atom(ax,[0,-1.8],'Ph')
  wedge(ax,p[1],[2,-.2],cfront);atom(ax,[2,-.2],'COOH',10)
  wedge(ax,p[1],[1.55,.65],not cfront);atom(ax,[1.55,.65],'H',10)
  ax.text(-1.8,-1.45,'P has a lone pair',fontsize=9)
  finish(ax,(-2.35,2.75),(-2.1,1.65),'Phospholane pair '+('I' if row==2 else 'II')+(': member' if j==0 else ': mirror'))
fig.suptitle('Each row is one enantiomeric pair; all individual structures are chiral',fontsize=13)
save(fig,Path(__file__).with_suffix('.png').name)
