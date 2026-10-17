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

fig,ax=plt.subplots(figsize=(8,4.7),layout='constrained')
xyz=np.array([[-1,0,0],[0,0,0],[.7,1,0],[.2,2,.5],[-1.2,2,-.5],[-1.7,1,0]])
project=lambda v:np.array([v[0]+.45*v[1],.5*v[1]+.8*v[2]])
p=np.array([project(v) for v in xyz]);ring(ax,p,{0:2})
for i,t in enumerate(['r₁','r₂','r₃','r₄','r₅','r₆']):label(ax,p[i]+[0,-.17],t)
u=p[0]+[-.6,-.5];bond(ax,p[0],u);atom(ax,u,'R¹',size=11)
q=p[3]+[1.,0];bond(ax,p[3],q);atom(ax,q,'C(OH)(CH₃)₂',size=11,ha='left')
h=p[3]+[0,.8];bond(ax,p[3],h);atom(ax,h,'H (L)')
label(ax,(2.1,.8),'pseudoequatorial substituent')
ax.text(.1,-1.05,'R¹ = CH₂O–cinnamate. Alkene end approximately planar.\nOne conformer illustrated; absolute configuration unassigned.',ha='center',fontsize=10)
finish(ax,(-3.8,4),(-1.45,2.8),'Cyclohexene half-chair')

save(fig,Path(__file__).with_suffix('.png').name,dpi=150)
