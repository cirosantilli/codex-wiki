"""Original answer diagram, generated with Python 3.14 and root dependencies."""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import atom,bond,ring,wedge,curly,flow,finish,save,chair,BLUE,GREEN,ORANGE

fig,axs=plt.subplots(1,3,figsize=(12,4.7),layout='constrained')
p=np.array([[0,1],[1,.5],[1,-.5],[0,-1],[-1,-.5],[-1,.5]])
ax=axs[0];ring(ax,p);bond(ax,p[0],[0,2],2);atom(ax,[0,2],'O')
cc=[2,.95];ch=[2.7,0];ss=[2,-.95]
for a,b in [(p[1],cc),(cc,ch),(ch,ss),(ss,p[2])]:bond(ax,a,b)
bond(ax,cc,[2.4,1.8],2);atom(ax,[2.4,1.8],'O');atom(ax,ss,'S')
ax.text(.72,.25,'C2',color=BLUE,fontsize=9);ax.text(.72,-.4,'C3',color=BLUE,fontsize=9)
finish(ax,(-1.7,3.25),(-1.7,2.7),'B2(b): fused diketone')
ax=axs[1];ring(ax,p);bond(ax,p[0],[0,2],2);atom(ax,[0,2],r'N$^+$',12);ax.text(0,2.45,'pyrrolidine N',ha='center',fontsize=9)
chain=[[1.85,.85],[2.65,.5],[3.35,.85]]
bond(ax,p[1],chain[0]);bond(ax,chain[0],chain[1]);bond(ax,chain[1],chain[2],2);atom(ax,chain[2],r'CH$_2$',10)
bond(ax,chain[1],[2.65,-.5]);atom(ax,[2.65,-.5],r'CO$_2$Et',10)
ax.text(1.2,-1.45,r'Br$^-$ counterion',ha='center',fontsize=11,color=ORANGE)
finish(ax,(-1.5,3.95),(-1.9,2.9),'B2(c): B, iminium bromide')
ax=axs[2];q=np.array([[0,.6],[1,0],[1,-1],[0,-1.6],[-1,-1],[-1,0]])
ring(ax,q)
bridge=[q[1],[1.25,1],[0,1.75],[-1.25,1],q[5]]
for a,b in zip(bridge,bridge[1:]):bond(ax,a,b,color=BLUE)
bond(ax,bridge[2],[0,2.65]);atom(ax,[0,2.65],r'CO$_2$Et',11)
bond(ax,q[0],[0,1.15],2);atom(ax,[0,1.15],r'N$^+$',11);ax.text(0,.15,'pyrrolidine N',ha='center',fontsize=8)
for i in [1,5]:ax.text(q[i,0]*1.18,q[i,1]-.12,'C'+str(i+1),fontsize=9)
finish(ax,(-1.9,1.9),(-2.0,3.2),'C: new three-carbon bridge')
save(fig,Path(__file__).with_suffix('.png').name)
