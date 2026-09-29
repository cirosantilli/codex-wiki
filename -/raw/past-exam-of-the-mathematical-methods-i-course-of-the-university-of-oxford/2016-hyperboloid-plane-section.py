"""Original illustration for the 2016 Oxford Mathematical Methods I solution.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

theta=np.linspace(0,2*np.pi,151);z=np.linspace(-2.1,2.1,49);Th,Z=np.meshgrid(theta,z)
X=np.sqrt(5+4*Z*Z)*np.cos(Th);Y=np.sqrt(1+.8*Z*Z)*np.sin(Th)
fig=plt.figure(figsize=(10.7,5.6),layout='constrained');ax=fig.add_subplot(121,projection='3d');right=fig.add_subplot(122)
ax.plot_wireframe(X,Y,Z,rstride=5,cstride=12,color='#37739c',alpha=.38,lw=.65)
u=np.sqrt(5)*np.cos(theta);w=np.sqrt(45/13)*np.sin(theta)
ax.plot(u,7*w/9,-8*w/(9*np.sqrt(2)),color='#b34325',lw=3)
px,py=np.meshgrid(np.linspace(-2.7,2.7,2),np.linspace(-1.75,1.75,2));ax.plot_surface(px,py,-8*py/(7*np.sqrt(2)),color='#edb16d',alpha=.17,shade=False)
ax.set(xlabel='$X$',ylabel='$Y$',zlabel='$Z$',title='Principal coordinates: hyperboloid and cutting plane',xlim=(-5,5),ylim=(-2.5,2.5),zlim=(-2.2,2.2));ax.set_box_aspect((1.4,1,1.1));ax.view_init(elev=21,azim=-55)
right.plot(u,w,color='#b34325',lw=2.4);right.axhline(0,color='.6',lw=.8);right.axvline(0,color='.6',lw=.8)
right.annotate(r'$\sqrt{5}$',(np.sqrt(5),0),(1.6,-.65),arrowprops={'arrowstyle':'->'},fontsize=12)
right.annotate(r'$\sqrt{45/13}$',(0,np.sqrt(45/13)),(.5,2.15),arrowprops={'arrowstyle':'->'},fontsize=12)
right.set(xlabel=r'$u$ along $(1,0,1)/\sqrt{2}$',ylabel=r'$w$ along $(1,-4,-1)/(3\sqrt{2})$',title='Intrinsic orthonormal coordinates in the plane',xlim=(-2.7,2.7),ylim=(-2.7,2.7));right.set_aspect('equal');right.grid(alpha=.2)
fig.suptitle(r'$Q_1=-5$: connected one-sheet surface; oblique section is an ellipse',fontsize=13)
fig.savefig(Path.cwd()/'2016-hyperboloid-plane-section.png',dpi=140,transparent=False)
plt.close(fig)
