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

p=np.array([[-.7,.7],[.7,.7],[1.25,-.1],[.6,-1],[-.6,-1],[-1.25,-.1]])

fig,ax=plt.subplots(figsize=(9,5.2),layout='constrained');ring(ax,p,{0:2})
for i,t in enumerate(['r₁: 4','r₂: 8; E','r₃: 14/15','r₄: 12; L','r₅: 17; J,M','r₆: 15/14']):
    off=np.array([0,.27]) if i<2 else np.array([.6,0]) if i==2 else np.array([0,-.28]) if i in [3,4] else np.array([-.6,0])
    label(ax,p[i]+off,t)
for i,end,t in [(0,(-1.5,1.6),'CH₂O–cinnamate'),(3,(1.4,-1.9),'C(OH)(CH₃)₂')]:bond(ax,p[i],end);atom(ax,end,t,size=11)
ax.text(0,-2.65,'r₃ CH₂: K + one of G/H/I;  r₆ CH₂: other two of G/H/I\n14 ↔ 15 and overlapped G/H/I remain unresolved',ha='center',fontsize=10,color=BLUE)
finish(ax,(-3.7,3.7),(-3.15,2.15),'Cyclohexene carbon numbers and proton letters')

save(fig,Path(__file__).with_suffix('.png').name,dpi=150)
