"""Original chemistry solution figure; Python 3.14, numpy and matplotlib.
Run from the desired output directory. No source figures or media paths are used.
"""
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tools'))
import chemistry_diagram as d
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig, axes=plt.subplots(1,3,figsize=(12,4.2))
for ax,subs,title in zip(axes,[{0:'Cl',1:'NO₂',3:'SO₂Me'},{0:'OH',1:'Me',2:'Br',3:'Br',4:'Me',5:'Br'},{0:'OH',1:'Me',2:'Br',4:'Me'}],['B1(a): nitration product','B1(c)(i): intermediate H','B1(c)(ii): retained bromine']):
 th=np.pi/2-np.arange(6)*np.pi/3; pts=np.column_stack((np.cos(th),np.sin(th)))
 d.ring(ax,pts,{0:2,2:2,4:2})
 for i in range(6):
  ax.text(*(pts[i]*.69),str(i+1),color=d.BLUE,ha='center',fontsize=9)
  if i in subs:
   q=pts[i]*1.65;d.bond(ax,pts[i],q);d.atom(ax,q,subs[i])
 d.finish(ax,(-2.25,2.25),(-2.1,2.15),title)
fig.tight_layout();d.save(fig,'paper-1-aromatic-products.png')
