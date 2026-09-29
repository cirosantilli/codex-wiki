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

fig,ax=plt.subplots(figsize=(10,5.7),layout='constrained')
p=np.array([[0,0],[1,0],[1.8,.6],[2.6,0],[3.4,.6],[4.2,0],[5,.6]])
for i in range(6):bond(ax,p[i],p[i+1],2 if i==4 else 1)
atom(ax,p[0],'ring');atom(ax,p[2],'O')
bond(ax,p[3],(2.6,-.85),2);atom(ax,(2.6,-.85),'O')
for xy,t in [((1,-.35),'F,F; 11'),((2.35,.35),'1'),((3.4,1.0),'D; 9'),((4.25,-.38),'A; 2'),((5.05,.18),'3')]:label(ax,xy,t)
centre=np.array([5.8,.6]);ang=np.deg2rad([180,120,60,0,-60,-120])
pts=centre+.8*np.column_stack([np.cos(ang),np.sin(ang)])
ring(ax,pts,{0:2,2:2,4:2})
for i,t in [(1,'B; 7'),(5,'B; 7'),(2,'C; 6'),(4,'C; 6'),(3,'C; 5')]:label(ax,centre+1.2*(pts[i]-centre)/.8,t)
ax.text(3.1,-1.45,'E cinnamate ester; A–D coupling = 16.2 Hz',ha='center',fontsize=11)
central=np.array([3.,-2.8])
for end in [(1.65,-2.8),(3.,-1.95),(4.2,-2.25),(4.2,-3.45)]:bond(ax,central,end)
atom(ax,(1.65,-2.8),'ring');atom(ax,(3.,-1.95),'OH')
for xy,t in [((4.2,-2.25),'CH₃ (N; 13)'),((4.2,-3.45),'CH₃ (O; 16)')]:atom(ax,xy,t,size=11,ha='left')
label(ax,(3.,-3.15),'10')
ax.text(3.1,-4.05,'Blue: proton letter; carbon signal number',ha='center',fontsize=10,color=BLUE)
finish(ax,(-.4,7.2),(-4.45,2.05),'Two derived side chains')

save(fig,Path(__file__).with_suffix('.png').name,dpi=150)
