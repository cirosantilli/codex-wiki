"""Original schematic chain segments; generate PNG basename into cwd."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond,atom,finish,save
fig,axes=plt.subplots(3,1,figsize=(8.8,6.0),facecolor='white')
rows=[('A: polyvinyl chloride',['Cl']*4),('B: illustrative chloride/acetate sequence',['Cl','OAc','Cl','Cl']),('C: formal hydrolysis target',['Cl','OH','Cl','Cl'])]
for ax,(title,groups) in zip(axes,rows):
    points=[(-3.5+i,.05 if i%2==0 else .50) for i in range(8)]
    for i,p in enumerate(points):
        if i:bond(ax,points[i-1],p)
        atom(ax,p,'CH2' if i%2==0 else 'CH',size=10)
        if i%2:
            end=(p[0],1.18);bond(ax,p,end);atom(ax,end,groups[i//2],size=11,color='#245c9f')
    bond(ax,(-4.15,-.20),points[0]);atom(ax,(-4.48,-.27),'...',size=12)
    bond(ax,points[-1],(4.10,.20));atom(ax,(4.40,.14),'...',size=12)
    finish(ax,(-4.9,4.9),(-.45,1.68),title)
fig.text(.5,.035,'OAc = O-C(=O)-CH3; rows B/C show a possible local sequence, not periodic blocks.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.08,1,1));save(fig,'paper-3-vinyl-copolymers.png')
