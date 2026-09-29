"""Original bond-stretch coordinate sketches; Python 3.14.4, matplotlib/numpy as pyproject.toml."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axes=plt.subplots(1,3,figsize=(8.5,3),layout='constrained')
xy=np.array([[0,0],[0,.95],[-.8,-.55],[.8,-.55]])
for ax,title,arrows in zip(axes,['A₁: predominantly C=O','A₁: symmetric C–H','B₁: antisymmetric C–H'],[
 [[0,-.38],[0,.5],[0,0],[0,0]],[[0,.18],[0,0],[-.8,-.55],[.8,-.55]],[[-.18,0],[0,0],[.8,.55],[.8,-.55]]]):
 for j in range(1,4):ax.plot(*xy[[0,j]].T,color='0.5',lw=2)
 for p,name,v in zip(xy,['C','O','H','H'],arrows):
  ax.scatter(*p,s=170,color='white',edgecolors='black',zorder=3);ax.text(p[0]+.13,p[1]+.03,name,fontsize=11)
  if any(v):ax.annotate('',p+np.array(v)*.58,p+np.array(v)*.08,arrowprops=dict(arrowstyle='->',color='#1262a6',lw=2))
 ax.text(-1.15,.85,'z ↑\nx →',fontsize=10);ax.set_title(title,fontsize=11);ax.set_aspect('equal');ax.set_xlim(-1.3,1.3);ax.set_ylim(-1.05,1.45);ax.axis('off')
fig.suptitle('Formaldehyde in the xz plane: stretching-coordinate symmetry patterns',fontsize=12)
fig.savefig(Path(Path(__file__).stem + '.png'),dpi=115,facecolor='white');plt.close(fig)
