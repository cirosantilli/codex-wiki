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

def fused(kind):
 th=np.arange(6)*np.pi/3;p=np.column_stack([np.cos(th),np.sin(th),((-1.)**np.arange(6))/np.sqrt(32)])
 ax=[np.array([0.,0.,(-1.)**i]) for i in range(6)];eq=[np.array([2*np.sqrt(2)/3*np.cos(th[i]),2*np.sqrt(2)/3*np.sin(th[i]),-(-1.)**i/3]) for i in range(6)]
 phase=-1 if kind=='trans' else 1;v=eq[0] if kind in ['trans','cis-out'] else ax[0]
 q=p.copy();q[:,2]*=phase
 def basis(a,b,c):
  u=(b-a)/np.linalg.norm(b-a);v=c-a;v-=u*np.dot(u,v);v/=np.linalg.norm(v);return np.stack([u,v,np.cross(u,v)],1)
 target=p[0]+np.linalg.norm(p[1]-p[0])*v;R=basis(p[0],p[1],target)@basis(q[0],q[1],q[5]).T;q=(q-q[0])@R.T+p[0]
 hs=[ax[0],ax[1]] if kind=='trans' else ([eq[0],ax[1]] if kind=='cis-in' else [ax[0],eq[1]])
 return p,q,hs,R,phase
M=np.array([[.85,.3,.1],[-.15,.5,.85]])
def drawfused(a,kind,oxy=False,br=False,alkene=False):
 p,q,hs,R,phase=fused(kind)
 if alkene:
  mid=(q[3]+q[4])/2;normal=np.cross(q[5]-q[2],mid-q[2]);normal/=np.linalg.norm(normal)
  for i in [3,4]:q[i]-=np.dot(q[i]-q[2],normal)*normal
 allp=np.vstack([p,q]);centre=(allp.max(0)+allp.min(0))/2
 def proj(v):return M@(v-centre)*1.35
 for ps,right in [(p,False),(q,True)]:
  for i in range(6):
   if right and i==0:continue
   d.bond(a,proj(ps[i]),proj(ps[(i+1)%6]),2 if right and alkene and i==3 else 1)
 if oxy:
  for i in [3,5]:txt(a,proj(q[i]),'O',14,'#b2472c')
 for i,v in enumerate(hs):
  u=proj(p[i]);h=proj(p[i]+.55*v);d.bond(a,u,h,color=d.BLUE);txt(a,h,'H',11,d.BLUE)
 if br:
  for i in [3,4]:
   v=R@np.array([0,0,phase*(-1.)**i]);u=proj(q[i]);r=proj(q[i]+.62*v);d.bond(a,u,r,color='#97465d');txt(a,r,'Br',11,'#97465d')
 if oxy:
  i=5 if kind=='cis-in' else 2
  j=5 if kind=='cis-in' else 2
  d.bond(a,proj(q[i]),proj(p[j]),style='dotted',color='#b2472c',lw=1)
 return p,q,proj

fig,axs=plt.subplots(2,2,figsize=(11,9),facecolor='white')
for a in axs.flat:setup(a,(-3,3),(-2.4,2.4))
drawfused(axs[0,0],'trans',alkene=True);axs[0,0].set_title('A: trans fusion, one chiral configuration',fontsize=12)
drawfused(axs[0,1],'trans',br=True);axs[0,1].set_title('A: favored trans-diaxial dibromide',fontsize=12)
for a,k,title in [(axs[1,0],'cis-in','B: one folded conformer'),(axs[1,1],'cis-out','B: mirror-related fold')]:drawfused(a,k,alkene=True);a.set_title(title,fontsize=12)
fig.text(.5,.04,'B folds interconvert; anti addition creates an enantiomeric product pair. Blue bonds mark junction H; bromines shown in A are opposite-face axial bonds.',ha='center',fontsize=9)
fig.text(.5,.015,'Idealized conformational sketches. The alkene segment is flattened schematically; these are not experimental coordinates.',ha='center',fontsize=9)
save(fig,'paper-1-decalins.png')
