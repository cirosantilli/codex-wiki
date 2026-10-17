"""Original solution diagram; Python 3.14, numpy and matplotlib.
Write the PNG basename to the current working directory (Make supplies _media).
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, ring, wedge, flow, finish, save

fig,axs=plt.subplots(2,3,figsize=(11.5,7))
a=axs[0,0];pts=[(-1,-.7),(1,-.7),(0,1.2),(0,-.1)]
for i in range(4):
 for j in range(i):bond(a,pts[i],pts[j],style='dashed' if set([i,j])==set([0,2]) else 'solid')
for p in pts:atom(a,p,'P')
finish(a,(-2,2),(-1.8,2),'Tetrahedral P₄: six P–P bonds')
for a,R,title in [(axs[0,1],'Me','Trimethylphosphine oxide'),(axs[0,2],'OMe','Trimethyl phosphate')]:
 P=(0,0);atom(a,P,'P');bond(a,P,(0,1.3),2);atom(a,(0,1.3),'O')
 for p,front in [((-1.25,-.55),None),((.15,-1.3),True),((1.25,-.55),False)]:
  if front is None:bond(a,P,p)
  else:wedge(a,P,p,front)
  atom(a,p,R)
 a.text(0,-1.8,'Tetrahedral at P; P=O is formal notation',ha='center',fontsize=8.5)
 finish(a,(-2,2),(-2,2),title)
a=axs[1,0];th=np.arange(6)*np.pi/3;pts=np.c_[1.02*np.cos(th),1.02*np.sin(th)];ring(a,pts)
for i,p in enumerate(pts):
 atom(a,p,'B' if i%2==0 else 'O')
 if i%2==0:
  q=1.72*p;bond(a,p,q);atom(a,q,r'$O^-$')
a.text(0,-1.9,r'$[B_3O_6]^{3-}$: planar model',ha='center',fontsize=11)
finish(a,(-2.2,2.2),(-2.15,2),'Three trigonal BO₃ units')
a=axs[1,1];pts=[(-1,-.55),(-1.3,.35),(-.45,.85),(.65,.5),(1.05,-.4),(.25,-.9)];ring(a,pts)
for i,p in enumerate(pts):
 atom(a,p,r'$P^+$' if i%2==0 else 'O')
 if i%2==0:
  p=np.array(p);v=p/(np.linalg.norm(p) or 1);normal=np.array([-v[1],v[0]])
  for v2,text,front in [(v+.55*normal,r'$O^-$',True),(v-.55*normal,r'$O^-$',False)]:
   q=p+.73*v2;wedge(a,p,q,front);atom(a,q,text,size=11)
a.text(0,-2,r'$[P_3O_9]^{3-}$: polar single-bond contributor',ha='center',fontsize=10)
finish(a,(-2.3,2.3),(-2.25,2),'Three tetrahedral PO₄ units')
a=axs[1,2];atom(a,(0,0),'Mo',size=15)
for p,t in [((-.85,.75),'O'),((.35,1.15),'O'),((1.05,.35),'O'),((-.85,-.65),'CO'),((.35,-1.2),'CO'),((1.05,-.6),'CO')]:bond(a,(0,0),p);atom(a,p,t,size=12)
a.plot([-.85,.35,1.05],[.75,1.15,.35],ls=':',color='#245c9f',lw=2);a.text(-1.1,1.5,'one O from each P',fontsize=9);a.text(0,-1.85,'O₃ face opposite CO₃ face',ha='center',fontsize=10)
finish(a,(-2,2),(-2.2,2),'fac-[Mo(CO)₃(P₃O₉)]³⁻')
fig.tight_layout(pad=1.5);save(fig,'paper-2-main-group.png')
