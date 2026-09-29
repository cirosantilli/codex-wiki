"""Original explanatory chemistry drawing; Python 3.14 / Matplotlib 3.10.7 / NumPy 2.3.5."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import atom,bond,ring,curly,flow,finish,save
BLUE='#245c9f'
def label(ax,p,text,size=10):
    ax.text(*p,text,ha='center',va='center',fontsize=size,color=BLUE)

fig,axes=plt.subplots(1,3,figsize=(12,4),layout='constrained')
ax=axes[0]
for xy,t in [((0,0),'Cr⁰(CO)₄'),((0,1.1),'N-pyridyl'),((1.6,0),'C(OEt)(Ar)'),((1.6,1.1),'Caryl–D')]:atom(ax,xy,t,size=11)
bond(ax,(0,.2),(0,.8));bond(ax,(.4,0),(1.1,0),2);curly(ax,(1.7,.9),(1.7,.2),rad=-.4)
finish(ax,(-1,2.6),(-1.1,1.8),'N coordination after CO loss')
ax=axes[1]
atom(ax,(0,0),'Crᴵᴵ(CO)₄(N)',size=11);atom(ax,(1.6,.7),'Caryl',size=11);atom(ax,(1.6,-.7),'C(D)(OEt)(Ar)',size=11)
bond(ax,(.35,.1),(1.1,.6));bond(ax,(.35,-.1),(1.1,-.6));curly(ax,(1.5,.5),(1.5,-.5),rad=-.35)
finish(ax,(-1,2.8),(-1.5,1.8),'Oxidative hydrogen migration')
ax=axes[2]
atom(ax,(0,0),'Caryl',size=11);atom(ax,(1.5,0),'C(D)(OEt)(Ar)',size=11);bond(ax,(.35,0),(1.,0))
ax.text(.8,-1,'D retained at former carbene carbon;\nfour other D remain on arene.',ha='center',fontsize=9,color=BLUE)
finish(ax,(-.9,3),(-1.5,1.8),'C–C reductive elimination')

save(fig,Path(__file__).with_suffix('.png').name,dpi=150)
