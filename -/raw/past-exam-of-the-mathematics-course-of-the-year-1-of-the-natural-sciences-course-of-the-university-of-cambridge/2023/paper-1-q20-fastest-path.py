"""Generate the PNG in cwd. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7;
dependencies are declared in the repository pyproject.toml.
"""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/nst-2023-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

fig,ax=plt.subplots(figsize=(6.4,5),layout='constrained',facecolor='white')
A=np.array([0,-np.sqrt(3)])
C=np.array([1,0])
B=np.array([2,1])
ax.axhspan(-2.2,0,color='#fff1e7')
ax.axhspan(0,1.6,color='#eaf4fc')
ax.axhline(0,color='black',linewidth=1.4)
ax.plot([A[0],C[0]],[A[1],C[1]],color='#b3472d',linewidth=2.4)
ax.plot([C[0],B[0]],[C[1],B[1]],color='#17679a',linewidth=2.4)
ax.plot([A[0],A[0]],[A[1],0],color='gray',linestyle='--',linewidth=1)
ax.plot([B[0],B[0]],[0,B[1]],color='gray',linestyle='--',linewidth=1)
ax.add_patch(Arc(A,0.8,0.8,theta1=60,theta2=90,color='#b3472d'))
ax.add_patch(Arc(B,0.75,0.75,theta1=225,theta2=270,color='#17679a'))
for p,label,offset in [(A,'$A=(0,-\\sqrt{3})$',(-28,-18)),(C,'$C=(1,0)$',(6,-19)),(B,'$B=(2,1)$',(5,8))]:
    ax.plot(*p,'ko',markersize=4)
    ax.annotate(label,p,xytext=offset,textcoords='offset points',fontsize=10)
ax.text(0.08,-1.05,r'$\theta=30^\circ$',fontsize=10)
ax.text(1.33,0.47,r'$\phi=45^\circ$',fontsize=10)
ax.text(1.35,-1.25,r'speed $c/2$',fontsize=11)
ax.text(-0.35,0.7,r'speed $c/\sqrt{2}$',fontsize=11)
ax.set(xlim=(-0.65,2.7),ylim=(-2.15,1.55),xlabel='horizontal distance',ylabel='height',
       title=r'Question 20: total distance $2+\sqrt{2}$, time $6/c$')
ax.set_aspect('equal')
ax.grid(alpha=0.16)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white')
plt.close(fig)
