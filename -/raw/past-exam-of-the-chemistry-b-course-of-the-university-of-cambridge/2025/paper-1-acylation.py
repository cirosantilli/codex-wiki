"""Original product and acylation electron-flow drawing; output to cwd."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import *
fig,axs=plt.subplots(1,2,figsize=(12,5),layout='constrained',facecolor='white')
a=axs[0];r=[(0,1),(.866,.5),(.866,-.5),(0,-1),(-.866,-.5),(-.866,.5)];ring(a,r,{0:2,2:2,4:2});chain=[r[4],(-1.75,-.6),(-2.1,.15),(-1.75,.85),r[5]]
for u,v in zip(chain,chain[1:]):bond(a,u,v)
atom(a,(-1.75,-.6),'O');bond(a,r[1],(1.8,1));bond(a,(1.8,1),(1.9,1.85),2);atom(a,(1.9,1.85),'O');bond(a,(1.8,1),(2.8,.55));atom(a,(2.8,.55),'CH₂Cl')
bond(a,r[2],(1.65,-1));atom(a,(1.65,-1),'NH');bond(a,(1.65,-1),(2.3,-1.55));bond(a,(2.3,-1.55),(3.15,-1.15),2);atom(a,(3.15,-1.15),'O');bond(a,(2.3,-1.55),(2.45,-2.35));atom(a,(2.45,-2.35),'CH₃')
a.text(.55,.8,'5',fontsize=11,color=BLUE);a.text(.55,-.3,'6',fontsize=11,color=BLUE);finish(a,(-2.7,3.8),(-2.8,2.3),'B: chloroacetyl group at C5')
a=axs[1]
# Acylium formation and aromatic attack are schematic, rather than a copied substrate illustration.
atom(a,(.15,1.5),'ClCH₂');bond(a,(.8,1.5),(1.65,1.5));atom(a,(1.7,1.5),'C');bond(a,(1.7,1.5),(1.7,2.2),2);atom(a,(1.7,2.2),'O');bond(a,(1.8,1.5),(2.6,1.5));atom(a,(2.65,1.5),'Cl');atom(a,(3.6,1.5),'GaCl₃')
curly(a,(2.25,1.5),(2.65,1.55),-.6);curly(a,(2.8,1.5),(3.15,1.5),.35);a.text(1.6,2.6,'Lewis-acid activation / chloride abstraction',ha='center',fontsize=10)
flow(a,(1.5,.85),(1.5,.4));atom(a,(1.5,.1),'ClCH₂–C⁺=O')
ar=np.array([[0,-1.1],[.65,-1.45],[.65,-2.2],[0,-2.55],[-.65,-2.2],[-.65,-1.45]])+np.array([.4,0]);ring(a,ar,{0:2,2:2,4:2});curly(a,(.75,-1.25),(1.6,-.08),.25)
a.text(2.15,-1.25,'π attack → arenium ion',fontsize=10);a.text(2.15,-1.8,'Base removes H⁺;',fontsize=10);a.text(2.15,-2.25,'π system is restored.',fontsize=10)
finish(a,(-.6,5.2),(-2.9,2.95),'Electron-pair movement')
save(fig,'paper-1-acylation.png')
