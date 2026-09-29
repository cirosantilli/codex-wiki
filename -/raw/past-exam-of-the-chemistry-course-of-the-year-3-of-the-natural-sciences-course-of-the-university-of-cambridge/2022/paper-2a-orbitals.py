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

fig,axs=plt.subplots(1,2,figsize=(10,5.8))
def line(a,x,y,occ,lab=''):
 a.plot([x-.26,x+.26],[y,y],color='#245c9f',lw=2)
 if occ:a.text(x,y+.08,'↑↓' if occ==2 else '↑',ha='center',fontsize=15)
 if lab:a.text(x+.4,y,lab,va='center',fontsize=12)
a=axs[0]
for y,xs,occ,lab in [(0,[1.1],2,r'$\alpha+2\beta$'),(2,[.65,1.55],2,r'$\alpha$'),(4,[1.1],0,r'$\alpha-2\beta$')]:
 for x in xs:line(a,x,y,occ)
 a.text(2.1,y,lab,va='center',fontsize=13)
a.text(1.3,-.85,'Six π electrons; β < 0',ha='center',fontsize=12)
a.set(xlim=(-.3,4.2),ylim=(-1.25,5));a.axis('off');a.set_title('Four-site square dianion',fontsize=14)
a=axs[1]
rows=[(0,1,2,r'$2\sigma_g$ (2s)'),(.8,1,2,r'$2\sigma_u^*$ (2s)'),(2.1,1,2,r'$3\sigma_g$ (2p along bond)'),(3.1,2,2,r'$1\pi_u$'),(4.2,2,1,r'$1\pi_g^*$'),(5.4,1,0,r'$3\sigma_u^*$')]
for y,n,occ,lab in rows:
 for x in ([.75,1.65] if n==2 else [1.2]):line(a,x,y,occ)
 a.text(2.1,y,lab,va='center',fontsize=12)
a.text(1.8,-.7,'12 valence electrons; S = 1',ha='center',fontsize=12)
a.set(xlim=(-.1,5.1),ylim=(-1,6));a.axis('off');a.set_title('O₂ valence orbitals',fontsize=14)
fig.tight_layout();save(fig,'paper-2a-orbitals.png')
