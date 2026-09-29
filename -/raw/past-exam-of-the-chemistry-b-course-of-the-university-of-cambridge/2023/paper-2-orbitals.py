"""Original donation/backbonding phase schematic. Python 3.14; PNG to cwd."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse,Circle
from tools.chemistry_diagram import bond,atom,ring,save
fig,axs=plt.subplots(2,2,figsize=(12,8),facecolor='white');blue='#245c9f';orange='#b45309'
def lobe(a,x,y,phase,w=.7,h=.42,color=blue):
    a.add_patch(Ellipse((x,y),w,h,facecolor=color,edgecolor=color,alpha=.22,zorder=1));a.text(x,y,phase,ha='center',va='center',color=color,fontsize=13,zorder=3)
for row in range(2):
 for col in range(2):
    a=axs[row,col];a.axis('off');a.set_aspect('equal');a.set(xlim=(-1.2,5.7),ylim=(-1.85,2.05))
    a.set_title(('Alkene' if row==0 else 'Aryne: ring plane')+(' — donation' if col==0 else ' — backbonding'),fontsize=13)
    atom(a,(0,0),'M',size=16)
    if row:
        pts=[(3,.7),(4.15,1.2),(5.3,.7),(5.3,-.7),(4.15,-1.2),(3,-.7)];ring(a,pts,color='0.55');a.add_patch(Circle((4.15,0),.65,fill=False,ec='0.6',lw=1.1))
    else:bond(a,(3,.7),(3,-.7),order=2)
    for y in [.7,-.7]:atom(a,(3,y),'C',size=12)
    if col==0:
        lobe(a,.65,0,'+',w=1.15,h=.85);lobe(a,-.55,0,'−',w=.5,h=.5)
        for y in [.7,-.7]:lobe(a,2.48,y,'+',color=orange);lobe(a,3.52,y,'−',color=orange)
        a.annotate('',(.8,1.55),(2.7,1.55),arrowprops={'arrowstyle':'->','color':orange,'lw':1.8})
        a.text(1.65,1.75,'filled π → vacant acceptor',ha='center',fontsize=10)
    else:
        for x,y,ph in [(.5,.5,'+'),(.5,-.5,'−'),(-.5,.5,'−'),(-.5,-.5,'+')]:lobe(a,x,y,ph,w=.72,h=.6)
        for y,p,q in [(.7,'+','−'),(-.7,'−','+')]:lobe(a,2.48,y,p,color=orange);lobe(a,3.52,y,q,color=orange)
        a.annotate('',(2.7,1.55),(.8,1.55),arrowprops={'arrowstyle':'->','color':blue,'lw':1.8})
        a.text(1.7,1.75,'filled metal d → vacant π*',ha='center',fontsize=10)
    if row:a.text(2.2,-1.63,'Aromatic p orbitals are perpendicular to the drawing plane.',ha='center',fontsize=9)
    else:a.text(2.2,-1.63,'The pictured plane contains C–C and the interacting π lobes.',ha='center',fontsize=9)
fig.text(.5,.014,'Phases (+/−) are orbital signs, not charges. Shapes are qualitative; each panel isolates one bonding channel.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.04,1,1));save(fig,'paper-2-orbitals.png',dpi=150)
