"""Original solution diagram; writes its PNG basename to the current directory."""
from pathlib import Path
import sys
for ancestor in Path(__file__).resolve().parents:
    if (ancestor/'tools'/'chemistry_diagram.py').exists():
        sys.path.insert(0,str(ancestor/'tools'));break
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, PathPatch
from matplotlib.path import Path as MplPath
from chemistry_diagram import bond, atom, curly, wedge, finish, save, BLUE, ORANGE

fig,ax=plt.subplots(figsize=(12,8),facecolor='white')
ax.set(xlim=(-1,14),ylim=(-25,7));ax.axis('off')
def level(x,y,label='',occ=0,w=.8,color='black'):
 ax.plot([x-w/2,x+w/2],[y,y],color=color,lw=1.4)
 if occ:ax.text(x,y+.12,'↑↓' if occ==2 else '↑',ha='center',fontsize=15)
 if label:ax.text(x+.65,y,label,va='center',fontsize=11,color=color)
ax.annotate('',(-.5,6),(-.5,-24),arrowprops={'arrowstyle':'->'});ax.text(-.85,-8,'Common qualitative energy reference',rotation=90,va='center',fontsize=11)
for x in [1,5]:level(x,-12,'1s',1)
level(3,-16,r'$1\sigma_g$ HOMO',2);level(3,4.8,r'$1\sigma_u^*$ LUMO')
for x in [1.4,4.6]:
 for y in [-16,4.8]:ax.plot([x,2.5 if x<3 else 3.5],[-12,y],ls=':',lw=.9,color='.65')
ax.text(3,6.2,'H₂: minimal 1s basis',ha='center',fontsize=13,weight='bold')
for x in [8,12]:
 level(x,-5,'2s',1);level(x,-1,'2p',0)
 for d in [-.35,.35]:level(x+d,-1,w=.2)
 level(x,-23,'1s core',2)
level(10,-7,r'$2\sigma_g$ HOMO',2);level(10,-3.8,r'$2\sigma_u$ LUMO',0,color=BLUE)
for x in [9.7,10.3]:level(x,-2,w=.4)
ax.text(10.8,-2,r'$1\pi_u(2p)$',va='center',fontsize=10)
level(10,1.6,r'$3\sigma_g(2p)$');level(10,5.1,r'$3\sigma_u(2p)$')
for x in [9.7,10.3]:level(x,3.4,w=.4)
ax.text(10.8,3.4,r'$1\pi_g(2p)$',va='center',fontsize=10)
level(10,-22,r'$1\sigma_u$ core',2);level(10,-24,r'$1\sigma_g$ core',2)
for x in [8.45,11.55]:
 for ya,yb in [(-5,-7),(-5,-3.8),(-1,-2),(-1,1.6),(-1,3.4),(-1,5.1),(-23,-24),(-23,-22)]:ax.plot([x,9.4 if x<10 else 10.6],[ya,yb],ls=':',color='.7',lw=.7)
ax.text(10,6.2,'Li₂: core + 2s/2p valence basis',ha='center',fontsize=13,weight='bold')
ax.text(7,-17.7,'Same-symmetry s–p mixing shifts the Li σ levels.\nThe Li 2σu acceptor is not a pure 2s combination.',ha='center',fontsize=10,color=BLUE)
ax.text(7,-20,'Core region compressed; gaps and the drawn 2p separations are schematic.',ha='center',fontsize=10)

fig.tight_layout();save(fig,'paper-1-diatomic-orbitals.png')
