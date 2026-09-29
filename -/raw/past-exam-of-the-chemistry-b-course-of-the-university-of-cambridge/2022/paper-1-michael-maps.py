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
fig,axes=plt.subplots(1,3,figsize=(15,5.3))
a,b,c=axes
pts=np.array([[-2,0],[-1,.7],[0,0],[1,.7],[2,0]])
for i in range(4):bond(a,pts[i],pts[i+1],2 if i in [0,3] else 1)
for i,p in enumerate(pts):atom(a,p,'P'+str(i+1),11)
x=(0,-1.5);atom(a,x,'X(Me)',12,color=ORANGE)
for j in [0,4]:bond(a,pts[j],x,color=ORANGE,style='dashed')
bond(a,pts[2],(0,1.05),2);atom(a,(0,1.05),'O → OH',10);a.text(-2,-.45,'Ph',ha='center',fontsize=10);a.text(2,-.45,'SEt remains',ha='center',fontsize=9);a.text(1,1.15,'amide',ha='center',fontsize=9);a.text(0,-2.3,'Five open-chain carbons + one nitroethane carbon.\nOrange bonds close the six-membered circuit.',ha='center',fontsize=9);finish(a,(-2.8,2.8),(-2.8,2),'B2(a): ring construction, not ring substitution')
p={'C3':(-1,0),'C2':(-1,1),'C1':(.1,1.5),'C5':(1.1,.7),'C4':(0,-.5),'X':(-.25,-1.55),'Y':(1.1,-.8)}
for u,v in [('C3','C2'),('C2','C1'),('C1','C5'),('C5','C4'),('C4','C3'),('C3','X'),('X','Y'),('Y','C5')]:bond(b,p[u],p[v],color=ORANGE if (u,v) in [('C3','X'),('Y','C5')] else '0.2')
for t,v in p.items():atom(b,v,t,11)
bond(b,p['C1'],(.1,2.2),2);atom(b,(.1,2.2),'O',11);bond(b,p['C3'],(-1.8,-.3));atom(b,(-1.8,-.3),'OR',10);b.text(-.7,-2.05,'X bears Me and CO₂Et',fontsize=9);b.text(0,-2.7,'Bridge paths contain 2, 1 and 2 internal atoms.',ha='center',fontsize=9);finish(b,(-2.3,2.3),(-3,2.5),'B2(b): two successive Michael bonds')
# Connectivity-only drawing of the fused 7,6-ring framework; no copied perspective.
jt=np.array([0,.7]);jb=np.array([0,-.7]);left=np.array([jt,[-.9,1.35],[-1.8,.8],[-2.05,-.2],[-1.55,-1.1],[-.7,-1.35],jb]);right=np.array([jt,[.9,1.3],[1.8,.6],[1.8,-.6],[.9,-1.3],jb])
ring(c,left,{4:2});ring(c,right)
for point,label in [(left[3],'K'),(left[4],'α(Me)'),(left[5],'β'),(right[1],'CO'),(right[2],'Rα'),(jt,'J(Me)')]:atom(c,point,label,9)
c.annotate('',left[5],right[2],arrowprops={'arrowstyle':'->','connectionstyle':'arc3,rad=-.2','lw':1.9,'color':ORANGE});c.text(0,-2.2,'Rα enolate attacks β; the enone is saturated.\nBoth carbonyls remain.',ha='center',fontsize=9);finish(c,(-2.6,2.5),(-2.8,2),'B2(c): new transannular bond')
fig.tight_layout();fig.savefig('paper-1-michael-maps.png',dpi=140,facecolor='white',bbox_inches='tight',pad_inches=.18);plt.close(fig)
