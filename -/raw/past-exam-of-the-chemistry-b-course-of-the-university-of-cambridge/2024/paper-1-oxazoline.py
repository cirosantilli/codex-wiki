"""Original solution diagram; Python 3.14, numpy, matplotlib. Output PNG goes to cwd."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'tools'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import chemistry_diagram as d
plt.rcParams.update({'font.size':11})
def txt(a,p,s,size=12,color='0.15'):d.atom(a,p,s,size=size,color=color)
def setup(a,x=(-3,3),y=(-2.5,2.5),title=None):d.finish(a,x,y,title)
def save(fig,name):
 fig.tight_layout();fig.savefig(name,dpi=165,facecolor='white',bbox_inches='tight',pad_inches=.15);plt.close(fig)

fig,axs=plt.subplots(1,3,figsize=(14,5),facecolor='white')
def ox(a,c=(0,0),scale=1):
 ps=[np.array(c)+scale*np.array(v) for v in [(0,0),(.7,-.6),(.45,-1.5),(-.45,-1.5),(-.7,-.6)]]
 d.ring(a,ps,{4:2});txt(a,ps[1],'O');txt(a,ps[4],'N');return ps
for a in axs:setup(a,(-3,3),(-3,3))
a=axs[0];a.set_title('O-triflylated cyclic carbamate',fontsize=12);ps=ox(a,(0,0));txt(a,ps[4],'NH⁺');txt(a,(0,1),'O–Tf');d.bond(a,(0,0),(0,.8));txt(a,(0,2),'Electrophilic carbon at ring C2',11)
a=axs[1];a.set_title('Para-ethoxy oxazoline',fontsize=12)
ps=[np.array([1.1*np.cos(t),1.1*np.sin(t)]) for t in np.arange(6)*np.pi/3]
d.ring(a,ps,{0:2,2:2,4:2});d.bond(a,ps[3],(-2.1,0));txt(a,(-2.35,0),'EtO');d.bond(a,ps[0],(2.0,.15));ox(a,(2.0,.15),.7)
a=axs[2];a.set_title('Bromodiphenyl ether product',fontsize=12)
ps=[np.array([-1.15+.65*np.cos(t),.65*np.sin(t)]) for t in np.arange(6)*np.pi/3];qs=[p+np.array([2.3,0]) for p in ps]
d.ring(a,ps,{0:2,2:2,4:2});d.ring(a,qs,{0:2,2:2,4:2});txt(a,(0,0),'O');d.bond(a,ps[0],(-.18,0));d.bond(a,(.18,0),qs[3]);d.bond(a,ps[3],(-2.35,0));txt(a,(-2.6,0),'Br');d.bond(a,qs[0],(2.35,.1));ox(a,(2.35,.1),.5)
fig.text(.5,.025,'Aryl attachment is at oxazoline C2. The two ring oxygens in the ether product have different roles.',ha='center',fontsize=10)
save(fig,'paper-1-oxazoline.png')
