"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

from itertools import combinations
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
fig=plt.figure(figsize=(8,3.8));ax=fig.add_subplot(121);angles=np.arange(5)*2*np.pi/5+np.pi/2;v=np.c_[np.cos(angles),np.sin(angles)]
for j in range(5):ax.add_patch(Polygon([[0,0],v[j],v[(j+1)%5]],facecolor=plt.cm.Set2(j/5),edgecolor='#49545b'))
ax.set(xlim=(-1.3,1.3),ylim=(-1.5,1.4),aspect='equal');ax.axis('off');ax.set_title('Decahedral cross-section');ax.text(0,-1.25,'Five fcc-like sectors; strain closes\nthe ideal 7.36° angular deficit',ha='center',fontsize=9)
ax=fig.add_subplot(122,projection='3d');phi=(1+np.sqrt(5))/2;verts=[]
for i in [-1,1]:
 for j in [-1,1]:verts.extend([(0,i,j*phi),(i,j*phi,0),(j*phi,0,i)])
verts=np.array(verts);faces=[c for c in combinations(range(12),3) if all(abs(np.linalg.norm(verts[i]-verts[j])-2)<1e-9 for i,j in combinations(c,2))]
assert len(faces)==20
polys=[verts[list(c)] for c in faces];ax.add_collection3d(Poly3DCollection(polys,facecolors=[plt.cm.Set2(i/20) for i in range(20)],edgecolor='#4b565e',linewidth=.6));ax.set(xlim=(-2,2),ylim=(-2,2),zlim=(-2,2));ax.set_box_aspect([1,1,1]);ax.set_axis_off();ax.set_title('Icosahedron: 20 outer facets');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
