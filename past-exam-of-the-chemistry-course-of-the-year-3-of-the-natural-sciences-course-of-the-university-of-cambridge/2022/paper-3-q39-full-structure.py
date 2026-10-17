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

fig,ax=plt.subplots(figsize=(11,5.6),layout='constrained');ring(ax,p,{0:2})
chain=np.array([p[0],[-1.3,1.6],[-2.1,1.95],[-2.9,1.45],[-3.7,1.95],[-4.5,1.45],[-5.3,1.95]])
for i in range(len(chain)-1):bond(ax,chain[i],chain[i+1],2 if i==4 else 1)
atom(ax,chain[2],'O');bond(ax,chain[3],(-2.9,.65),2);atom(ax,(-2.9,.65),'O')
centre=np.array([-6.1,1.95]);ang=np.deg2rad([0,60,120,180,240,300])
ar=centre+.8*np.column_stack([np.cos(ang),np.sin(ang)]);ring(ax,ar,{0:2,2:2,4:2})
for xy,t in [((-1.32,2.0),'11; F,F'),((-3.05,1.8),'1'),((-3.7,2.28),'9; D'),((-4.5,1.05),'2; A')]:label(ax,xy,t)
for i,t in enumerate(['4','8; E','14/15','12; L','17; J,M','15/14']):
    off=np.array([0,.25]) if i<2 else np.array([.45,0]) if i==2 else np.array([0,-.3]) if i in [3,4] else np.array([-.5,0])
    label(ax,p[i]+off,t)
q=np.array([1.6,-1.7]);bond(ax,p[3],q)
for end,t in [((2.5,-1.15),'OH'),((1.2,-2.65),'CH₃'),((2.6,-2.25),'CH₃')]:bond(ax,q,end);atom(ax,end,t,size=11)
label(ax,(1.9,-1.62),'10');label(ax,(1.1,-3.0),'13; N');label(ax,(3.,-2.65),'16; O')
ax.text(-3.4,-2.65,'Phenyl: ipso 3; ortho 7/B; meta 6/C; para 5/C\nr₃: K + one G/H/I; r₆: other two G/H/I',ha='center',fontsize=10,color=BLUE)
ax.text(-2,-3.5,'C₁₉H₂₄O₃; E cinnamate; no absolute configuration assigned',ha='center',fontsize=11)
finish(ax,(-7.4,3.8),(-3.9,3.25),'Complete derived constitution and assignments')

save(fig,Path(__file__).with_suffix('.png').name,dpi=150)
