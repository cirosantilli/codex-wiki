"""One trans product enantiomer; original coordinates, PNG basename in cwd."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond,atom,ring,wedge,finish,save
fig,ax=plt.subplots(figsize=(5.0,5.0),facecolor='white')
p=[(0,1),(.866,.5),(.866,-.5),(0,-1),(-.866,-.5),(-.866,.5)]
ring(ax,p,{3:2,5:2})
for i,y in [(0,1.85),(3,-1.85)]:bond(ax,p[i],(0,y));atom(ax,(0,y),'Ph')
wedge(ax,p[1],(1.62,.98),True);atom(ax,(1.87,1.10),'Me')
wedge(ax,p[2],(1.62,-.98),False);atom(ax,(1.87,-1.10),'Me')
finish(ax,(-1.45,2.55),(-2.2,2.2),'C: trans methyl groups')
fig.text(.5,.045,'One enantiomer; reverse both stereobonds for its mirror image.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.09,1,1));save(fig,'paper-3-electrocyclic-product.png')
