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

fig,axes=plt.subplots(1,2,figsize=(10.5,4.8),layout='constrained')
ax=axes[0];p=np.array([[-1.5,0],[-.5,0],[.2,-.75],[1.2,-.75]])
for i in range(3):bond(ax,p[i],p[i+1],2 if i in [0,2] else 1)
for i,pt in enumerate(p):
    label(ax,pt+[0,.23],str(i+1));q=pt+[0,.8] if i in [0,1] else pt+[0,-.8]
    bond(ax,pt,q);atom(ax,q,'Ph',size=10)
bond(ax,p[0],[-2.3,-.7]);atom(ax,[-2.8,-.9],'Rh(COD)L',size=10)
bond(ax,p[3],[1.9,0]);atom(ax,[2.3,.2],'Ar',size=11)
ax.text(-.15,-2.1,'Two successive syn insertions at Rh end',ha='center',fontsize=10)
finish(ax,(-3.6,2.8),(-2.5,1.6),'Dienyl chain after two insertions')
ax=axes[1];p=np.array([[-.9,.6],[.6,.6],[.6,-.6],[-.9,-.6]])
ring(ax,p,{1:2});bond(ax,p[3],p[0],color='#1b7837',lw=3)
for i,pt in enumerate(p):
    label(ax,pt+[-.12,-.13],str(i+1));q=pt+np.array([-.6 if i in [0,3] else .6,.6 if i<2 else -.6])
    bond(ax,pt,q);atom(ax,q,'Ph',size=10)
bond(ax,p[3],[-.9,-1.5]);atom(ax,[-.9,-1.7],'Ar',size=10);atom(ax,(0,1.5),'Rh(COD)',size=11)
for pt in p[:3]:bond(ax,(0,1.25),pt,style='dotted',lw=1.2)
ax.text(0,-2.15,'−L; conrotatory C₁–C₄ closure; η³ binding',ha='center',fontsize=10)
finish(ax,(-2.2,2.3),(-2.5,2.1),'Cyclobutenyl chain trapping')

save(fig,Path(__file__).with_suffix('.png').name,dpi=150)
