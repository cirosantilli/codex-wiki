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

fig=plt.figure(figsize=(14,10),facecolor='white');gs=fig.add_gridspec(2,2);aa=fig.add_subplot(gs[0,0]);at=fig.add_subplot(gs[0,1]);cg=fig.add_subplot(gs[1,:])
setup(aa,(-3.2,3.2),(-2.3,2.3),'C·E: complementary cyclic amide pair')
# Two local lactam edges, closed ring paths shown around their backs.
for sign in [-1,1]:
 x=1.05*sign;ps=[(x,.6),(x,-.6),(2.05*sign,-1.0),(2.65*sign,-.3),(2.65*sign,.8),(2.0*sign,1.2)];d.ring(aa,ps,{2:2,4:2} if sign>0 else {})
 if sign<0:
  txt(aa,ps[0],'C');txt(aa,ps[1],'N–H');d.bond(aa,ps[0],(-.25,.9),2);txt(aa,(-.1,.95),'O');d.bond(aa,ps[1],(.1,-.95),style='dotted',color=d.BLUE)
 else:
  txt(aa,ps[0],'N–H');txt(aa,ps[1],'C');d.bond(aa,ps[1],(.25,-.9),2);txt(aa,(.1,-.95),'O');d.bond(aa,ps[0],(.1,.9),style='dotted',color=d.BLUE)
 txt(aa,(2.2*sign,-1.65),'C' if sign<0 else 'E',13)
# Explicit conventional base ring connectivities, rotated to expose WC edges.
def purine(a,c,label):
 x,y=c;ps=[np.array([x+np.cos(t),y+np.sin(t)]) for t in np.arange(6)*np.pi/3]
 # left-facing hexagon WC edge: C6 top-left (idx2), N1 left (3), C2 bottom-left(4), N3 bottom-right(5), C4 right(0), C5 top-right(1).
 d.ring(a,ps,{0:2,2:2,4:2} if label=='A' else {0:2,4:2})
 for i,s in [(3,'N1' if label=='A' else 'N1–H'),(5,'N3')]:txt(a,ps[i],s,10)
 q=[ps[0],ps[1],np.array([x+1.55,y+1.1]),np.array([x+2,y+.25]),np.array([x+1.5,y-.6])];[d.bond(a,q[i],q[(i+1)%5],2 if i==2 else 1) for i in range(1,5)];txt(a,q[2],'N7',10);txt(a,q[4],'N9',10);d.bond(a,q[4],q[4]+np.array([.6,-.65]));txt(a,q[4]+np.array([.8,-.9]),'sugar',9)
 txt(a,(x+.5,y-1.5),label,12);return ps,q

def pyrimidine(a,c,kind):
 x,y=c;ps=[np.array([x+np.cos(t),y+np.sin(t)]) for t in np.arange(6)*np.pi/3];d.ring(a,ps,{2:2} if kind=='T' else {0:2,2:2})
 # right edge: idx1 C4, idx0 N3, idx5 C2; idx4 N1 sugar.
 txt(a,ps[0],'N3–H' if kind=='T' else 'N3',10);txt(a,ps[4],'N1',10);d.bond(a,ps[4],ps[4]+np.array([-.5,-.65]));txt(a,ps[4]+np.array([-.7,-.85]),'sugar',9)
 for i,s in [(1,'O4' if kind=='T' else 'N4H₂'),(5,'O2')]:
  q=ps[i]+np.array([.3,.65 if i==1 else -.65]);d.bond(a,ps[i],q,2 if s.startswith('O') else 1);txt(a,q,s,10)
 if kind=='T':d.bond(a,ps[2],ps[2]+np.array([-.7,.5]));txt(a,ps[2]+np.array([-.9,.65]),'Me',10)
 txt(a,(x-.4,y-1.65),kind,13);return ps
setup(at,(-4.5,4.2),(-2.8,3),'A·T: two Watson–Crick hydrogen bonds')
pa,qa=purine(at,(1,0),'A');pt=pyrimidine(at,(-2,0),'T')
d.bond(at,pa[2],pa[2]+np.array([-.4,.65]));txt(at,pa[2]+np.array([-.4,.75]),'N6H₂',10)
d.bond(at,(-1.2,1.1),(.0,1.5),style='dotted',color=d.BLUE);d.bond(at,(-1,0),(0,0),style='dotted',color=d.BLUE);None
txt(at,(-.4,2.7),'MAJOR: N7 / N6 and O4 / Me',10,d.BLUE);txt(at,(-.4,-2.5),'MINOR: N3 / C2–H and O2',10,d.BLUE)
setup(cg,(-6.3,6.7),(-2.8,3),'C·G: three base-pair bonds; arginine recognizes the exposed guanine edge')
pg,qg=purine(cg,(1,0),'G');pc=pyrimidine(cg,(-2,0),'C')
d.bond(cg,pg[2],pg[2]+np.array([-.4,.65]),2);txt(cg,pg[2]+np.array([-.4,.75]),'O6',10)
d.bond(cg,pg[4],pg[4]+np.array([-.3,-.65]));txt(cg,pg[4]+np.array([-.35,-.8]),'N2H₂',10)
for p,q in [((-1.2,1.2),(.1,1.5)),((-1,0),(0,0)),((-1.2,-1.2),(.1,-1.5))]:d.bond(cg,p,q,style='dotted',color=d.BLUE)
None;txt(cg,(-.5,2.75),'MAJOR GROOVE',11,d.BLUE);txt(cg,(-.5,-2.45),'MINOR GROOVE',11,d.BLUE)
# Arginine in the major groove supplies two donors, one to each acceptor; neither WC bond is replaced.
txt(cg,(4.75,2.85),'Arg guanidinium',12,'#9c4c24');txt(cg,(3.6,2.35),'NH₂',11,'#9c4c24');txt(cg,(4,1.05),'NH₂⁺',11,'#9c4c24');txt(cg,(4.7,1.7),'C',11,'#9c4c24');txt(cg,(5.7,1.7),'NH–R',11,'#9c4c24');d.bond(cg,(3.8,2.2),(4.5,1.85),color='#9c4c24');d.bond(cg,(4.2,1.2),(4.55,1.55),2,color='#9c4c24');d.bond(cg,(4.9,1.7),(5.4,1.7),color='#9c4c24')
d.bond(cg,(3.2,2.35),(.3,1.65),style='dotted',color='#9c4c24');d.bond(cg,(3.55,1.05),qg[2],style='dotted',color='#9c4c24')
fig.text(.5,.012,'Dotted lines are hydrogen bonds. Base atom numbering distinguishes Watson–Crick partners from groove-exposed sites; sugars are indicated by attachment bonds.',ha='center',fontsize=9)
save(fig,'paper-1-recognition.png')
