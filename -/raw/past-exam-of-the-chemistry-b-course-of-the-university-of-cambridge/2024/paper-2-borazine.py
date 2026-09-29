"""Original inferred borazine product connectivities; output to cwd, no source-image inputs."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
fig,axs=plt.subplots(1,3,figsize=(13,5.5),facecolor='white')
pts=[np.array([np.cos(t),np.sin(t)]) for t in np.arange(6)*np.pi/3+np.pi/2]
blue='#266aa0';red='#b65f35'
for a in axs:a.axis('off');a.set(xlim=(-2.05,2.05),ylim=(-2.45,2.15),aspect='equal')
def text(a,p,s,fs=12,c='k'):a.text(*p,s,ha='center',va='center',fontsize=fs,color=c,bbox=dict(fc='white',ec='none',pad=.7),zorder=4)
def bond(a,p,q,c='#333',style='-',lw=1.5):a.plot([p[0],q[0]],[p[1],q[1]],color=c,ls=style,lw=lw,zorder=1)
def ring(a,sub,cols=None):
 for i,p in enumerate(pts):
  bond(a,p,pts[(i+1)%6],(cols or ['#333']*6)[i],lw=2)
  text(a,p,('B' if i%2==0 else 'N')+str(i//2+1),11)
  if sub[i]:
   q=p*1.45;bond(a,p,q);text(a,q,sub[i],11)
a=axs[0];a.set_title('A: B-methyl addition',fontsize=12,weight='bold');ring(a,['', 'Me','Me','Me','Me','Me'])
for dx,label in [(-.5,'Meᵃ'),(.5,'Meᵇ')]:
 q=pts[0]+np.array([dx,.6]);bond(a,pts[0],q);text(a,q,label,11)
text(a,(.05,-.07),'Cr(CO)₃',11,blue)
for i in range(1,6):bond(a,pts[i]*.85,(.05,-.07),blue,':',.8)
text(a,(0,-1.8),'[ring–Cr(CO)₃]⁻ · [MgBr]⁺',11)
text(a,(0,-2.18),'η⁵ attachment excludes tetrahedral B1',9)
a=axs[1];a.set_title('B: N→AlBr₃ adduct',fontsize=12,weight='bold')
# N1 is vertex1: its two adjacent edges are long, next pair short, last pair intermediate.
cols=[red,red,blue,'#777','#777',blue];ring(a,['Me','Me','Me','Me','Me','Me'],cols)
p=pts[1];q=p+np.array([-.75,-.35]);bond(a,p,q,red);text(a,q,'AlBr₃',11,red)
text(a,(0,-1.65),'Red: long adjacent pair',10,red);text(a,(0,-1.97),'Blue: short compensating pair',10,blue);text(a,(0,-2.29),'Gray: third pair; ring may pucker',10,'#555')
a=axs[2];a.set_title('C: Pt(II) boryl bromide',fontsize=12,weight='bold');ring(a,['','H','Br','H','Br','H'])
p=pts[0];q=p+np.array([0,.55]);bond(a,p,q);text(a,q,'Pt',12)
for vec,s in [(np.array([0,.45]),'Br'),(np.array([-.95,0]),'PCy₃'),(np.array([.95,0]),'PCy₃')]:
 r=q+vec;bond(a,q,r);text(a,r,s,11)
text(a,(0,-1.75),'Pt–B trans to Pt–Br',10);text(a,(0,-2.1),'Two phosphines trans; ring intact',10)
fig.text(.5,.025,'Connectivities and bond classes are inferred models, not experimental coordinates. A and B have distinct local symmetry; C is a σ-bound borazinyl complex.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.06,1,1));fig.savefig('paper-2-borazine.png',dpi=170,facecolor='white',bbox_inches='tight',pad_inches=.15);plt.close(fig)
