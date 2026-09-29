"""Original explanatory diagram; Python 3.14, matplotlib and numpy.
Run from the desired output directory; the PNG is written to that directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save, BLUE, ORANGE
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(1,3,figsize=(12,4.4),layout='constrained')
verts=np.array([[x,y,z] for x in [0,1] for y in [0,1] for z in [0,1]])
proj=lambda v:np.array([1.3*v[0]+.65*v[2],1.3*v[1]+.55*v[2]])
for ax,missing,title in [(axs[0],None,'T8: Cy₈Si₈O₁₂'),(axs[2],7,'T7: Cy₇Si₇O₉(OH)₃')]:
    ps=[proj(v) for v in verts]
    for i in range(8):
        for j in range(i):
            if np.sum(abs(verts[i]-verts[j]))!=1:continue
            if missing in [i,j]:
                other=j if i==missing else i;end=ps[other]+.45*(ps[missing]-ps[other]);bond(ax,ps[other],end);atom(ax,end,'OH',size=10,color=ORANGE)
            else:
                bond(ax,ps[i],ps[j]);ax.scatter(*((ps[i]+ps[j])/2),s=28,c=ORANGE,zorder=4)
    for i,p in enumerate(ps):
        if i==missing:continue
        dist=np.sum(abs(verts[i]-verts[missing])) if missing is not None else 0
        ax.scatter(*p,s=75,c=BLUE if dist!=3 else '#7a3d83',zorder=5)
    finish(ax,(-.35,2.7),(-.45,2.3),title)
th=np.arange(5)*2*np.pi/5+.3;f=np.column_stack([.85*np.cos(th),.6*np.sin(th)]);b=f+np.array([.7,1.1]);ax=axs[1]
for pts in [f,b]:
    ring(ax,pts)
    for j in range(5):ax.scatter(*((pts[j]+pts[(j+1)%5])/2),s=28,c=ORANGE,zorder=4)
for a,z in zip(f,b):bond(ax,a,z);ax.scatter(*((a+z)/2),s=28,c=ORANGE,zorder=4)
for p in np.vstack([f,b]):ax.scatter(*p,s=75,c=BLUE,zorder=5)
finish(ax,(-1.1,2.1),(-1,2.1),'T10: Cy₁₀Si₁₀O₁₅')
fig.suptitle('Silicon vertices (blue); bridging oxygen (orange). One Cy on every Si is omitted.',fontsize=12)
fig.text(.5,.02,'T7: three OH-bearing Si, three further Si, and the unique opposite Si (purple).',ha='center',fontsize=11)
save(fig,'paper-2-silsesquioxanes.png')
