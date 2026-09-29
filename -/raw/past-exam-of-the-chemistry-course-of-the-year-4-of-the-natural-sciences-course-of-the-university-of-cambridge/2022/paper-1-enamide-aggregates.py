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

fig,axs=plt.subplots(1,3,figsize=(12.4,4.5))
ax=axs[0];ax.text(0,.9,r'$\mathrm{Ph_2P(O)-CH_2-C(tBu)=NLi}$',ha='center',fontsize=13)
flow(ax,(0,.55),(0,-.15),'H migration')
ax.text(0,-.5,r'$\mathrm{Ph_2P(O)-CH=C(tBu)-NHLi}$',ha='center',fontsize=13)
ax.text(0,-1.1,'CH at 4.82 ppm; NH at 3.25 ppm',ha='center',fontsize=9)
finish(ax,(-2,2),(-1.6,1.4),'Organic ligand')
ax=axs[1]
# Alternating Li/O vertices of a cube projected obliquely.
verts={}
for x in [0,1]:
 for y in [0,1]:
  for z in [0,1]:verts[x,y,z]=np.array([1.3*x+.5*z,1.3*y+.4*z])
for k,p in verts.items():
 for j in range(3):
  if k[j]==0:
   kk=list(k);kk[j]=1;bond(ax,p,verts[tuple(kk)],lw=1.2)
for k,p in verts.items():atom(ax,p,'Li' if sum(k)%2==0 else 'O',size=11)
ax.text(.9,-.7,'Each Li also binds one enamide N\n(all Li sites equivalent in this model)',ha='center',fontsize=9)
finish(ax,(-.5,2.6),(-1.2,2.4),'B: plausible Li4O4 core')
ax=axs[2];LiA=(-.9,0);LiB=(.9,0);O1=(0,.8);O2=(0,-.8)
for p in [LiA,LiB]:
 for q in [O1,O2]:bond(ax,p,q)
for p,t in [(LiA,'Li A'),(LiB,'Li B'),(O1,'O 1'),(O2,'O 2')]:atom(ax,p,t,size=11)
for p,q,t in [(LiA,(-1.7,.7),'N L1'),(LiA,(-1.7,-.7),'N L2'),(LiB,(1.7,.7),'N T1'),(LiB,(1.7,-.7),'N T2')]:bond(ax,p,q);atom(ax,q,t,size=10)
bond(ax,(1.85,.5),(2.05,0));bond(ax,(2.05,0),(1.85,-.5))
ax.text(0,-1.3,'L = enamide; T = one chelating TMEDA',ha='center',fontsize=9)
finish(ax,(-2.3,2.4),(-1.7,1.6),'C: two different O2N2 donor sets')
fig.tight_layout();save(fig,OUT)
