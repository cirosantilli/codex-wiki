"""Original explanatory figure; output basename to the current directory.

Tested with the repository Python 3.14 / NumPy / Matplotlib environment.
"""
from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.chemistry_diagram import bond, atom, wedge, ring, flow, finish, save
OUT=Path(__file__).stem+'.png'

fig,ax=plt.subplots(figsize=(7,5.2))
pts=[np.array(x) for x in [(0,1),(.866,.5),(.866,-.5),(0,-1),(-.866,-.5),(-.866,.5)]]
ring(ax,pts,{4:2})
for i,p in enumerate(pts):ax.text(*(p*.78),str(i+1),fontsize=11,color='#245c9f',ha='center',va='center')
for i,q,t,front in [(0,(.28,2),'CO2CH2CH=CH2',True),(0,(-.9,1.75),'OH',False),(1,(2,.95),'C(O)N-morpholine',True),(3,(0,-2),'OH',True)]:
 wedge(ax,pts[i],q,front);atom(ax,q,t,size=12)
ax.text(0,-2.7,'One enantiomer shown; the product is racemic.\nSolid wedges share one face; hashed OH is on the opposite face.',ha='center',fontsize=10)
finish(ax,(-2.6,3.6),(-3.1,2.6),'C: ring-opened endo cycloadduct')
fig.tight_layout();save(fig,OUT)
