"""Oxford 2015 geometric modelling Q3: incremental hull stages.

Run from any directory; writes geometric-modelling-2015-hull.png there.
Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
"""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.mkdtemp(prefix='gmod-hull-mpl-'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import proj3d
import numpy as np

P = {k:np.array(v,float) for k,v in dict(A=(0,-1,0),B=(0,1,0),C=(-1,0,-1),D=(0,0,1),E=(1,0,0)).items()}
initial = ['ACB','ABD','ADC','BCD']
final = ['ADC','BCD','ACE','CBE','BDE','DAE']
fig = plt.figure(figsize=(11,4),layout='constrained')
axes = [fig.add_subplot(1,3,i+1,projection='3d') for i in range(3)]
for i,ax in enumerate(axes):
    faces = final if i==2 else initial
    colors = ['#9dc9e7' if f in ['ADC','BCD'] else ('#f09c8d' if i==1 else '#b4d7ed') for f in faces]
    poly = Poly3DCollection([[P[k] for k in f] for f in faces],facecolors=colors,edgecolors='#26485c',alpha=.55,lw=1.2)
    ax.add_collection3d(poly)
    for label,p in P.items():
        if i==0 and label=='E':continue
        ax.scatter(*p,color='#123e67',s=16,depthshade=False)
    ax.set(xlim=(-1.25,1.25),ylim=(-1.25,1.25),zlim=(-1.25,1.25),xlabel='x',ylabel='y',zlabel='z')
    ax.set_box_aspect((1,1,1))
    ax.view_init(elev=22,azim=42)
    ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1]);ax.set_zticks([-1,0,1])
    ax.tick_params(labelsize=8,pad=0)
    for label,p in P.items():
        if i==0 and label=='E':continue
        px,py,_=proj3d.proj_transform(*p,ax.get_proj())
        ax.annotate(label,(px,py),xytext=(5,5),textcoords='offset points',fontsize=11,
                    color='#142a39',zorder=100)
axes[0].set_title('Initial tetrahedron ABCD',fontsize=11)
axes[1].set_title('Visible cap: ACB and ABD',fontsize=11)
axes[2].set_title('Final hull: retain 2, add 4 faces',fontsize=11)
horizon=[P[k] for k in 'ACBDA']
axes[1].plot(*np.array(horizon).T,color='#963899',lw=3)
for k in 'ACBD':
    axes[1].plot(*np.array([P[k],P['E']]).T,'--',color='#963899',lw=1)
fig.savefig('geometric-modelling-2015-hull.png',dpi=125,facecolor='white',transparent=False)
plt.close(fig)
