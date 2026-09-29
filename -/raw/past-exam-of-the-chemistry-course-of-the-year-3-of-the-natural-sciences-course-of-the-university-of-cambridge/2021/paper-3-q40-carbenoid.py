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

fig,ax=plt.subplots(figsize=(10,5.5));finish(ax,(-3,8),(-2.2,3.4),'Diazomalonate → copper carbenoid → intramolecular cyclopropane')
atom(ax,(-.7,2.6),'tBuO₂C–C(N₂)–CO₂allyl',14);flow(ax,(1.6,2.6),(3.5,2.6),'Cu(I), −N₂')
atom(ax,(5.5,2.6),'Cu=C(CO₂tBu)(CO₂allyl)',14)
flow(ax,(5.5,2.1),(5.5,1.25),'tethered C=C capture')
p=[(4,-.5),(5,.3),(6,-.2),(6,-1.2),(5,-1.7)];ring(ax,p);ring(ax,[p[0],p[4],(4,-1.9)])
atom(ax,p[2],'O');bond(ax,p[1],(5,1),2);atom(ax,(5,1),'O');bond(ax,p[0],(2.9,-.5));atom(ax,(2.3,-.5),'CO₂tBu',12)
ax.text(-.5,-.6,'Two new C–C bonds share\nthe diazo-derived carbon.',ha='center',fontsize=12,color=BLUE)
save(fig,Path(__file__).with_suffix('.png').name)
