"""Original crystallographic cell construction; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import itertools
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig=plt.figure(figsize=(12.4,5.5),layout='constrained',facecolor='white');a=fig.add_subplot(121)
a.add_patch(Polygon([[0,0],[1,0],[1,1],[0,1]],facecolor='#dbeafe',edgecolor='#2563eb',lw=2,alpha=.7,label='Old conventional basal square'))
a.add_patch(Polygon([[0,0],[.5,.5],[0,1],[-.5,.5]],fill=False,edgecolor='#dc2626',lw=2.5,label='New basal square'))
pts=np.array([(i/2,j/2) for i in range(-2,4) for j in range(-1,4) if (i+j)%2==0]);a.scatter(pts[:,0],pts[:,1],s=55,color='#334155',zorder=4)
for end,label,pos in [((.5,.5),r'$\mathbf{b}_1$',(.36,.15)),((-.5,.5),r'$\mathbf{b}_2$',(-.49,.16))]:
 a.annotate('',xy=end,xytext=(0,0),arrowprops=dict(arrowstyle='->',color='#dc2626',lw=2.5));a.text(*pos,label,color='#b91c1c',fontsize=13)
a.text(.52,1.07,'Old basal edge = a',ha='center',fontsize=11);a.text(-.1,.66,r'$|\mathbf{b}_1|=|\mathbf{b}_2|=a/\sqrt{2}$',ha='center',fontsize=11,bbox=dict(facecolor='white',edgecolor='none',alpha=.85));a.set(xlim=(-.72,1.18),ylim=(-.15,1.21),xlabel=r'Old $x/a$',ylabel=r'Old $y/a$',title='Basal-plane sites after compression');a.set_aspect('equal');a.legend(loc='lower right',fontsize=9)
b=fig.add_subplot(122,projection='3d');vertices=np.array(list(itertools.product([0.,1.],repeat=3)))
for v in vertices:
 for j in range(3):
  if v[j]==0:
   w=v.copy();w[j]=1;b.plot(*np.stack([v,w]).T,color='#64748b',lw=1.7)
b.scatter(*vertices.T,s=58,color='#2563eb',depthshade=False);b.scatter([.5],[.5],[.5],s=105,color='#dc2626',depthshade=False);b.text(.53,.52,.52,'Body centre',fontsize=10);b.set(xlabel=r'$X$',ylabel=r'$Y$',zlabel=r'$Z$',title=r'New cube: all edges $a/\sqrt{2}$',xticks=[0,1],yticks=[0,1],zticks=[0,.5,1]);b.set_box_aspect([1,1,1]);b.view_init(elev=22,azim=-55)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
