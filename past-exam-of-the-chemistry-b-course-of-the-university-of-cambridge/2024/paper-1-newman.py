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

from matplotlib.patches import Circle,Arc
fig,axs=plt.subplots(1,3,figsize=(13,5.6),facecolor='white')
for a in axs:setup(a,(-2.5,2.5),(-2.5,2.8))
for a,kind,title in zip(axs,['normal','gly','pro'],['Other residues: Cβ limits torsions','Glycine: two small H substituents','Proline: side chain ties N to Cα']):
 a.add_patch(Circle((0,0),.45,fill=False,ec='0.35',lw=1.6));a.scatter([0],[0],c='0.15',s=35,zorder=5)
 # Front amide N has two other substituents, not three tetrahedral arms.
 d.bond(a,(0,0),(0,1.25));txt(a,(0,1.45),"C′prev",11)
 d.bond(a,(0,0),(0,-1.15));txt(a,(.35,-1.2) if kind=='pro' else (0,-1.45),'Cδ' if kind=='pro' else 'H',11)
 for ang,label in [(25,"C′next"),(145,'H'),(230,'H' if kind=='gly' else 'Cβ')]:
  u=np.array([np.cos(np.deg2rad(ang)),np.sin(np.deg2rad(ang))]);d.bond(a,.45*u,1.3*u,color=d.BLUE);txt(a,1.65*u,label,11,d.BLUE)
 if kind=='pro':
  a.plot([0,-.65,1.3*np.cos(np.deg2rad(230))],[-1.15,-1.65,1.3*np.sin(np.deg2rad(230))],color='#ac572a',lw=2);txt(a,(-.65,-1.85),'Cγ',10,'#ac572a')
 a.set_title(title,fontsize=11);txt(a,(0,2.15),'View N → Cα; front N is planar',10)
 txt(a,(0,-2.25),'Broad φ,ψ with steric exclusions' if kind=='normal' else 'Positive and negative φ accessible' if kind=='gly' else 'φ constrained near −60°',10)
fig.text(.5,.025,'Circle: rear Cα; dot: front N. Shown torsions illustrate contacts, not a complete energy map. ψ is seen in a corresponding Cα→C′ projection.',ha='center',fontsize=9)
save(fig,'paper-1-newman.png')
