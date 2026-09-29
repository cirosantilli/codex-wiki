"""Original answer diagram, generated with Python 3.14 and root dependencies."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import atom,bond,ring,wedge,curly,flow,finish,save,chair,BLUE,GREEN,ORANGE

fig,axs=plt.subplots(1,2,figsize=(12,4.7),layout='constrained')
ax=axs[0]
for sign in [-1,1]:
 cc=np.array([sign*1.25,0]);oc=np.array([sign*.55,-sign*.58]);oh=np.array([sign*.55,sign*.58]);hh=np.array([sign*.03,sign*.58])
 bond(ax,cc,oc,2);atom(ax,oc,'O');bond(ax,cc,oh);atom(ax,oh,'O');bond(ax,oh,hh);atom(ax,hh,'H',11)
 bond(ax,cc,[sign*2.35,0]);atom(ax,[sign*2.35,0],'Ar',13)
 ax.plot([hh[0],-sign*.55],[hh[1],hh[1]],ls=':',color=BLUE,lw=2)
ax.text(0,-1.7,'Ar = meta-methylphenyl',ha='center',fontsize=10)
finish(ax,(-3.1,3.1),(-2.05,2.05),'Pure 1: cyclic acid homodimer')
ax=axs[1];left=np.array([[-.6,.55],[-.6,-.55],[-1.55,-1.1],[-2.5,-.55],[-2.5,.55],[-1.55,1.1]])
for sign in [1,-1]:
 pts=left*sign;ring(ax,pts,{0:2,2:2,4:2});atom(ax,pts[0],'N',13)
 nn=np.array([-.05,-.95])*sign;hh=np.array([.34,-.7])*sign;hh2=np.array([-.17,-1.65])*sign
 bond(ax,pts[1],nn);atom(ax,nn,'N',13);bond(ax,nn,hh);atom(ax,hh,'H',10);bond(ax,nn,hh2);atom(ax,hh2,'H',10)
 end=np.array([-3.2,.9])*sign;bond(ax,pts[4],end);atom(ax,end,'Cl',11)
 target=-left[0]*sign;ax.plot([hh[0],target[0]],[hh[1],target[1]],ls=':',color=BLUE,lw=2)
finish(ax,(-3.7,3.7),(-2.05,2.05),'Pure 2: reciprocal amino-NH···pyridine-N')
save(fig,Path(__file__).with_suffix('.png').name)
