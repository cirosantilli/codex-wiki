"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3. Run from mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,3.5))
for ax in axs:ax.set(xlim=(-1.5,2.7),ylim=(-1.5,1.5),aspect='equal');ax.axis('off')
ax=axs[0];P={'I':(-1.3,0),'O':(0,0),'L':(2,1),'R':(2,-1)}
for a,b in [('I','O'),('O','L'),('O','R'),('L','R')]:ax.plot(*zip(P[a],P[b]),color='#344f61',lw=2)
for n,(x,y) in P.items():ax.plot(x,y,'ko',ms=4);ax.text(x,y+.14,n,ha='center')
ax.text(-.7,-.25,'x',ha='center');ax.text(.65,.65,'B = y + Rc',ha='center',fontsize=9);ax.text(.65,-.8,'C = z + Rc',ha='center',fontsize=9);ax.text(2.13,0,'Rg');ax.set_title('One groove added')
ax=axs[1];P={'I':(-1.3,0),'C':(.7,0),'L':(2,1),'R':(2,-1)}
for a,b in [('I','C'),('C','L'),('C','R')]:ax.plot(*zip(P[a],P[b]),color='#197e80',lw=2)
for n,(x,y) in P.items():ax.plot(x,y,'ko',ms=4);ax.text(x,y+.14,n,ha='center')
ax.text(-.4,-.25,'x + BC/S',ha='center');ax.text(1.1,.75,'B Rg/S',ha='center');ax.text(1.1,-.85,'C Rg/S',ha='center');ax.text(.6,-1.35,'S = B + C + Rg',ha='center');ax.set_title('Equivalent frontier star');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
