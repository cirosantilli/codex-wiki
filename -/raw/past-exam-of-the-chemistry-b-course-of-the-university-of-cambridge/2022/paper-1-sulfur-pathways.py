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
fig,axes=plt.subplots(2,2,figsize=(12,9))
a,b,c,e=axes.flat
q=(-.8,0);l=(.8,0);su=(0,1.1);ring(a,[q,l,su]);atom(a,q,'Q',13);atom(a,l,'L',13);atom(a,su,'S⁺Ph',13);a.text(-1.8,-.8,'protected OH:\nβ-H loss + Q–S cleavage\n→ ring alkene',ha='center',fontsize=10,color=BLUE);a.text(1.8,-.8,'free terminal OH:\nO attacks Q, Q–S cleaves\n→ five-membered spiro ether',ha='center',fontsize=10,color=GREEN);a.text(0,-2,'The L–SPh bond survives either opening.',ha='center',fontsize=10);finish(a,(-3.2,3.2),(-2.5,1.8),'B3(b): common bridged thiiranium ion')
p={'S⁺':(0,1),'A':(-.8,0),'C':(0,-1),'B':(.8,0),'X':(-1.8,1.4),'Y':(-2.1,.2),'NH':(-1.7,-1.1)}
for u,v in [('S⁺','A'),('A','C'),('C','B'),('B','S⁺'),('S⁺','X'),('X','Y'),('Y','NH'),('NH','C')]:bond(b,p[u],p[v],2 if (u,v)==('X','Y') else 1,color=BLUE if u in ['A','B'] or v in ['A','B'] else '0.2')
for t,v in p.items():atom(b,v,t,11)
b.text(-1.9,1.8,'X bears CO₂Me',fontsize=9);b.text(1.65,0,'A ≡ B\n(two CH₂ paths)',ha='center',fontsize=10,color=BLUE);b.text(0,-2,'I⁻ opens either S–CH₂ bond → opposite configurations.',ha='center',fontsize=10);finish(b,(-2.7,3),(-2.5,2),'B3(c): equivalent paths erase the stereocentre')
# Five-membered intermediate fused to the six-membered carbocycle.
c2=np.array([-.75,0]);c3=np.array([.75,0]);so=np.array([-1.15,1]);cn=np.array([0,1.6]);sn=np.array([1.15,1]);ring(c,[c2,so,cn,sn,c3]);six=[c2,c3,(1.1,-1),(.55,-1.85),(-.55,-1.85),(-1.1,-1)];ring(c,six)
for v,t in [(c2,'C₂'),(c3,'C₃'),(so,'Sₒ'),(cn,'C'),(sn,'Sₙ')]:atom(c,v,t,12,color=BLUE if t=='Sₒ' else ORANGE if t=='Sₙ' else '0.12')
bond(c,cn,(0,2.4),2);atom(c,(0,2.4),'N⁻',12);c.text(0,-2.5,'C₂–Sₒ–C(=N⁻)–Sₙ–C₃ is the five-membered ring.',ha='center',fontsize=10);finish(c,(-3,3),(-3,2.9),'B3(d): fused 6,5 cyclic intermediate')
e.text(0,1.7,'CN transfer and reclosure',ha='center',fontsize=13)
e.text(0,.8,'N⁻ reforms C≡N; C–Sₙ breaks.',ha='center',fontsize=11)
e.text(0,.15,'C₂–Sₒ–C≡N     +     C₃–Sₙ⁻',ha='center',fontsize=13)
e.text(0,-.6,'Sₙ⁻ attacks C₂ from the back.',ha='center',fontsize=11)
e.text(0,-1.3,'New thiirane Sₙ  +  ⁻Sₒ–C≡N',ha='center',fontsize=13)
e.text(0,-2.1,'Both ring carbons invert; the remote OH stays fixed.',ha='center',fontsize=10,color=ORANGE);finish(e,(-3,3),(-3,2.9))
fig.tight_layout();fig.savefig('paper-1-sulfur-pathways.png',dpi=140,facecolor='white',bbox_inches='tight',pad_inches=.18);plt.close(fig)
