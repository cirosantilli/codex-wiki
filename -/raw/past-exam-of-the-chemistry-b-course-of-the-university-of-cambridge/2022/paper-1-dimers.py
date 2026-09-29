"""Original solution diagram; Python 3.14, numpy and matplotlib.
The PNG output basename is relative to the current working directory.
"""
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import bond, wedge, atom, ring, curly, flow, finish, save, BLUE, ORANGE, GREEN
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,3,figsize=(13,4.8));a,b,c=axes
O1=np.array([-1.2,0]);H1=np.array([-.35,0]);O2=np.array([.85,0]);bond(a,O1,H1);bond(a,O1,(-1.6,-.8));atom(a,O1,'O',15,color=BLUE);atom(a,H1,'H',13);atom(a,(-1.6,-.8),'H',13);bond(a,H1,O2,style='dotted',color=ORANGE,lw=2);atom(a,O2,'O',15,color=BLUE)
for h in [(1.45,.6),(1.45,-.6)]:bond(a,O2,h);atom(a,h,'H',13)
a.text(0,1.25,'donor O–H ··· O acceptor',ha='center',fontsize=11);a.text(0,-1.65,'localized hydrogen bond\nplus other interaction components',ha='center',fontsize=10);finish(a,(-2.2,2.2),(-2.3,2),'Water dimer')
project=lambda v:np.array([v[0]+.40*v[1],.28*v[1]+.80*v[2]])
def benz(ax,centre,plane='xy',colour='0.2'):
 th=np.arange(6)*np.pi/3
 xyz=np.column_stack([np.cos(th),np.sin(th),np.zeros(6)]) if plane=='xy' else np.column_stack([np.sin(th),np.zeros(6),np.cos(th)])
 xyz=xyz+np.array(centre);pp=np.array([project(x) for x in xyz]);ring(ax,pp,{0:2,2:2,4:2},color=colour);return xyz
benz(b,(0,0,0));benz(b,(0,0,2.8),'xz');bond(b,(0,.5),(0,1.0),style='dotted',color=ORANGE);b.text(0,-1.1,'edge-to-face electrostatics\nand dispersion',ha='center',fontsize=10);finish(b,(-2.2,2.2),(-1.6,3.5),'T-shaped benzene dimer')
x=benz(c,(-.4,0,0));y=benz(c,(.4,0,2));
for i in [0,2,4]:bond(c,project(x[i]),project(y[i]),style='dotted',color=ORANGE,lw=1)
c.text(0,-1.1,'slipped parallel pi surfaces:\ndistributed contacts',ha='center',fontsize=10);finish(c,(-2.2,2.2),(-1.6,3.5),'Parallel-displaced benzene dimer')
fig.tight_layout();fig.savefig('paper-1-dimers.png',dpi=140,facecolor='white',bbox_inches='tight',pad_inches=.18);plt.close(fig)
