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

fig,axs=plt.subplots(1,2,figsize=(12,5.8),facecolor='white')
a=axs[0];setup(a,(-2.6,4.3),(-2.3,2.7),'Extended-enone product: terminal sulfur addition')
ps=[np.array([np.cos(t),np.sin(t)]) for t in np.arange(6)*np.pi/3+np.pi/2]
d.ring(a,ps,{4:2});d.bond(a,ps[0],(0,1.9),2);txt(a,(0,2.1),'O');# ring C3 is bottom-right vertex4 for this orientation
c3=ps[4];q=c3+np.array([1,.55]);r=q+np.array([1,-.55]);d.bond(a,c3,q);d.bond(a,q,r);d.bond(a,r,r+np.array([.7,.4]));txt(a,r+np.array([1,.55]),'SPh')
# Here C1=vertex0, C2=vertex5, C3=vertex4; retained C2=C3 is edge4.
for i,label in [(0,'C1'),(5,'C2'),(4,'C3')]:a.text(ps[i][0]-.22,ps[i][1]-.25,label,fontsize=9,color=d.BLUE)
txt(a,(.6,-1.8),'Ring enone retained; side chain is –CH₂CH₂SPh',10)
a=axs[1];setup(a,(-1,8),(-2.5,2.7),'Activated-allene product: central sulfur addition')
for p,s in [((.5,0),'Ph₂P(O)'),((3,0),'CH₂'),((4.8,0),'C'),((6.5,0),'CH₂'),((4.8,1.2),'SPh')]:txt(a,p,s,14)
d.bond(a,(1.45,0),(2.5,0));d.bond(a,(3.5,0),(4.5,0));d.bond(a,(5.05,0),(5.95,0),2);d.bond(a,(4.8,.2),(4.8,1));txt(a,(3.3,-1.4),'Intermediate: negative charge on the P-bearing carbon',10)
txt(a,(3.3,-1.95),'Protonation makes CH₂; terminal alkene has no E/Z pair',10)
save(fig,'paper-1-thiol-additions.png')
