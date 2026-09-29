"""Original solution figure. Tested with Python 3.14, numpy and matplotlib.
The PNG basename is written to the current working directory for Make's _media target.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, flow, finish, save

from matplotlib.patches import Circle,Ellipse
# Basis vectors refer to globally oriented pz and py atomic functions.
react=[(r'$\pi_{O,z}$: A₁',[0,0,1,1,0,0]),(r'$\pi_{O,y}$: B₂',[0,0,0,0,1,1]),(r'$\pi_{O,z}^*$: B₁',[0,0,1,-1,0,0]),(r'$\pi_{O,y}^*$: A₂',[0,0,0,0,1,-1]),(r'$\pi_C$: A₁',[1,1,0,0,0,0]),(r'$\pi_C^*$: B₁',[1,-1,0,0,0,0])]
prod=[(r'$\sigma_+$: A₁',[1,1,-1,-1,0,0]),(r'$n_+$: B₂',[0,0,0,0,1,1]),(r'$\sigma_-$: B₁',[1,-1,-1,1,0,0]),(r'$n_-$: A₂',[0,0,0,0,1,-1]),(r'$\sigma_+^*$: A₁',[1,1,1,1,0,0]),(r'$\sigma_-^*$: B₁',[1,-1,1,-1,0,0])]
fig,axs=plt.subplots(6,2,figsize=(9,12))
pos=[np.array([-.9,0]),np.array([.9,0]),np.array([-.9,1.4]),np.array([.9,1.4])]
for col,data in enumerate([react,prod]):
 for row,(title,vec) in enumerate(data):
  a=axs[row,col];bond(a,pos[0],pos[1]);bond(a,pos[2],pos[3])
  if col:
   bond(a,pos[0],pos[2]);bond(a,pos[1],pos[3])
  for i,p in enumerate(pos):
   a.text(p[0],p[1],'C' if i<2 else 'O',ha='center',va='center',fontsize=9,zorder=8,bbox={'fc':'white','ec':'none','pad':.5})
  for i,v in enumerate(vec[:4]):
   if v:
    for side in [-1,1]:
     q=pos[i]+np.array([0,.24*side]);a.add_patch(Ellipse(q,.23,.4,fc='#245c9f' if side*v>0 else '#b45309',alpha=.8,zorder=3))
  for i,v in enumerate(vec[4:]):
   if v:
    p=pos[i+2];a.add_patch(Circle(p+np.array([.19,.12]),.19,fc='#245c9f' if v>0 else '#b45309',alpha=.8,zorder=4));a.add_patch(Circle(p-np.array([.19,.12]),.19,fc='#b45309' if v>0 else '#245c9f',alpha=.5,zorder=3))
  a.text(1.5,.65,title,ha='left',fontsize=12);a.set(xlim=(-1.45,3.8),ylim=(-.6,2));a.set_aspect('equal');a.axis('off')
axs[0,0].set_title('Separated-fragment active orbitals',fontsize=13);axs[0,1].set_title('Product symmetry combinations',fontsize=13)
fig.text(.5,.025,'Blue/orange indicate phase, not charge. In-plane lobes: global pz; oblique paired circles: global py.\nProduct C–O orbitals are phase cartoons, not computed orbital contours; common normalization is omitted.',ha='center',fontsize=9)
fig.subplots_adjust(hspace=.12,wspace=.2,left=.02,right=.97,top=.965,bottom=.06);save(fig,'paper-2a-active-orbitals.png')
