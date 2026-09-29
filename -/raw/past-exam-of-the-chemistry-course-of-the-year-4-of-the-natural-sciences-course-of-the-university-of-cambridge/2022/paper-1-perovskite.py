"""Original explanatory figure; output basename to the current directory.

Tested with the repository Python 3.14 / NumPy / Matplotlib environment.
"""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import bond, atom, wedge, ring, flow, finish, save
OUT=Path(__file__).stem+'.png'

from itertools import product
fig=plt.figure(figsize=(6.2,5.1));ax=fig.add_subplot(projection='3d')
corners=np.array(list(product([0,1],repeat=3)),float)
for a in corners:
 for b in corners:
  if np.sum(np.abs(a-b))==1 and tuple(a)<tuple(b):ax.plot(*np.array([a,b]).T,color='.7',lw=.8)
center=np.array([.5,.5,.5]);nit=[]
for i in range(3):
 for v in [0,1]:
  a=center.copy();a[i]=v;nit.append(a);ax.plot(*np.array([center,a]).T,color='#b65e21',lw=2)
nit=np.array(nit)
ax.scatter(*corners.T,s=110,color='#617da3',label='La: corners',depthshade=False)
ax.scatter(*center[:,None],s=180,color='#b65e21',label='Re: body center',depthshade=False)
ax.scatter(*nit.T,s=100,color='#35996b',label='N: face centers',depthshade=False)
ax.set_box_aspect((1,1,1));ax.view_init(elev=19,azim=29);ax.set_axis_off()
ax.legend(loc='upper left',fontsize=9);ax.set_title('Ideal ABN3 perovskite cell\nB-centered octahedron highlighted')
fig.tight_layout();save(fig,OUT)
