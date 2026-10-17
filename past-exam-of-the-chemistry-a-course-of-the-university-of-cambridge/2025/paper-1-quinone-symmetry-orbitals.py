"""Original eight normalized symmetry-orbital phase maps; Python 3.14.4, matplotlib/numpy."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
r=np.sqrt(2)
U=np.array([[1/r,0,0,0,0,0,0,1/r],[0,1/r,0,0,0,0,1/r,0],[0,0,.5,.5,.5,.5,0,0],
 [1/r,0,0,0,0,0,0,-1/r],[0,1/r,0,0,0,0,-1/r,0],[0,0,.5,.5,-.5,-.5,0,0],
 [0,0,.5,-.5,.5,-.5,0,0],[0,0,.5,-.5,-.5,.5,0,0]])
assert np.allclose(U@U.T,np.eye(8))
xy=np.array([[0,1.8],[0,1],[-.87,.5],[.87,.5],[-.87,-.5],[.87,-.5],[0,-1],[0,-1.8]])
edges=[(0,1),(1,2),(1,3),(2,4),(3,5),(4,6),(5,6),(6,7)]
fig,axes=plt.subplots(2,4,figsize=(9.4,7.3),layout='constrained')
for ax,v,label in zip(axes.flat,U,['B₁u: O+','B₁u: C+','B₁u: R+','B₃g: O−','B₃g: C−','B₃g: R−','B₂g: X','Aᵤ: Y']):
 for i,j in edges:ax.plot(*xy[[i,j]].T,color='.72',lw=1.4,zorder=1)
 for i,(p,a) in enumerate(zip(xy,v)):
  ax.scatter(*p,s=75 if a==0 else 380*abs(a),color='white' if a==0 else ('#1368a8' if a>0 else '#de792c'),edgecolors='.3',zorder=3)
  if a:ax.text(*p,'+' if a>0 else '−',ha='center',va='center',color='white',fontsize=12,zorder=4)
  ax.text(p[0]+(.15 if p[0]>=0 else -.15),p[1]+.08,str(i+1),ha='left' if p[0]>=0 else 'right',fontsize=9)
 ax.set_title(label,fontsize=12);ax.set_aspect('equal');ax.set_xlim(-1.3,1.3);ax.set_ylim(-2.05,2.08);ax.axis('off')
fig.suptitle('p-Quinone symmetry orbitals: phases of the +z lobes (not molecular orbitals)',fontsize=13)
fig.savefig(Path(Path(__file__).stem + '.png'),dpi=110,facecolor='white');plt.close(fig)
