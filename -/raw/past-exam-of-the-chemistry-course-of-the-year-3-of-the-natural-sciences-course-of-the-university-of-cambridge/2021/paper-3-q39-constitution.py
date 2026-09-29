"""Original solution diagram; Python 3.14, matplotlib 3.10, numpy 2.3.
Run from the mirrored media directory: PNG basename is written to cwd.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from tools.chemistry_diagram import atom,bond,ring,curly,flow,finish,save,wedge,BLUE,ORANGE

fig,ax=plt.subplots(figsize=(9.5,5.5));finish(ax,(-3,4.4),(-2.2,2.3),'Seven-membered lactam · printed spectrum labels')
p=[(-.7,1.3),(.7,1.3),(1.55,.25),(1.1,-1.05),(-.25,-1.5),(-1.5,-.65),(-1.6,.65)]
ring(ax,p)
atom(ax,p[0],'C',13);bond(ax,p[0],(-.7,2.05),2);atom(ax,(-.7,2.05),'O');atom(ax,p[6],'NH',13)
for i,t in [(1,'B'),(2,'E / G'),(3,'F / H'),(4,'A'),(5,'C / D')]:atom(ax,p[i],t,13,color=BLUE)
# Oxygenated carbon sites, each with one explicitly assigned carbon-bound H.
bond(ax,p[1],(1.25,1.95));atom(ax,(1.25,1.95),'OH');bond(ax,p[4],(-.25,-2));atom(ax,(-.25,-2),'OH')
for i,c,dx,dy in [(0,'1',-.38,.15),(1,'3',.3,-.35),(2,'6',.48,0),(3,'5',.45,-.1),(4,'2',-.38,-.15),(5,'4',-.45,-.15)]:ax.text(p[i][0]+dx,p[i][1]+dy,c,fontsize=12,color=ORANGE)
ax.text(3.3,1.2,'Carbon labels',color=ORANGE,ha='center',fontsize=11);ax.text(3.3,.6,'Proton letters',color=BLUE,ha='center',fontsize=11);ax.text(3.3,-.2,'C₆H₁₁NO₃\n2 OH + NH exchange\nin D₂O',ha='center',fontsize=11)
save(fig,Path(__file__).with_suffix('.png').name)
