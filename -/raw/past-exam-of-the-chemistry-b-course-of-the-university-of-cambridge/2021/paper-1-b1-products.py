"""Original answer diagram, generated with Python 3.14 and root dependencies."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import atom,bond,ring,wedge,curly,flow,finish,save,chair,BLUE,GREEN,ORANGE

fig,axs=plt.subplots(1,2,figsize=(11,4.2),layout='constrained')
ax=axs[0];th=np.deg2rad([90,30,-30,-90,-150,150]);p=np.column_stack([np.cos(th),np.sin(th)])
ring(ax,p,{0:2,2:2,4:2})
for i,t in [(0,'OMe'),(3,'OMe'),(1,'R'),(4,'R')]:
 q=1.6*p[i];bond(ax,p[i],q);atom(ax,q,t,12)
for i in [2,5]:atom(ax,1.4*p[i],'H',11)
ax.text(0,-2.25,r'R = C(CH$_3$)$_2$CH$_2$CH$_3$',ha='center',fontsize=12)
finish(ax,(-2.6,2.6),(-2.65,2.3),'B1(a): symmetric 2,5-disubstitution')
ax=axs[1];cen=np.array([0.,0.]);lc=np.array([-1.2,0]);rc=np.array([1.2,0])
bond(ax,lc,cen);bond(ax,cen,rc);bond(ax,lc,[-1.2,.9],2);atom(ax,[-1.2,.9],'O');bond(ax,rc,[1.2,-.9],2);atom(ax,[1.2,-.9],'O')
bond(ax,lc,[-2.35,0]);atom(ax,[-2.35,0],'EtO');bond(ax,rc,[2.6,0]);atom(ax,[2.6,0],r'CH$_2$OtBu',11)
bond(ax,cen,[0,1.3]);atom(ax,[0,1.3],r'CH$_2$CH$_2$Ar',12)
bond(ax,cen,[0,-1.3]);atom(ax,[0,-1.3],r'CH$_2$CH$_2$CH=CH$_2$',11)
ax.text(0,-2.15,'Ar = 2,5-dimethoxyphenyl',ha='center',fontsize=10)
finish(ax,(-3.25,3.6),(-2.65,2.3),'B1(b): two carbon alkylations at one site')
save(fig,Path(__file__).with_suffix('.png').name)
