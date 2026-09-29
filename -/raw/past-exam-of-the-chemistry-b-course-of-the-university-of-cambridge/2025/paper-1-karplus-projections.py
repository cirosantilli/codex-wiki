"""Illustrative, not fitted, H-C-C-H torsions in Newman projections."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Arc
from tools.chemistry_diagram import *
fig,axs=plt.subplots(1,4,figsize=(13,3.5),layout='constrained',facecolor='white')
for ax,phi,title in zip(axs,[30,150,0,120],['A: cis, puckered','A: trans, puckered','B: cis, flatter ring','B: trans, flatter ring']):
 ax.add_patch(Circle((0,0),.33,fc='white',ec='0.4',lw=1.4));a0=np.pi/2;a1=a0+np.deg2rad(phi)
 for base,isfront in [(a0,True),(a1,False)]:
  for j in range(3):
   th=base+2*np.pi*j/3;end=np.array([np.cos(th),np.sin(th)])
   start=np.zeros(2) if isfront else .33*end;bond(ax,start,.9*end,color=BLUE if isfront else ORANGE,lw=1.7 if isfront else 1.2)
   atom(ax,1.08*end,'H' if j==0 else 'R',color=BLUE if isfront else ORANGE,size=12)
 ax.plot(0,0,'o',color=BLUE,ms=4);ax.add_patch(Arc((0,0),1.0,1.0,theta1=90,theta2=90+max(phi,3),color='0.5',lw=1.1))
 ax.text(0,-1.55,f'φ ≈ {phi}°',ha='center',fontsize=12);finish(ax,(-1.45,1.45),(-1.8,1.55),title)
fig.suptitle('Illustrative dominant-conformer angles: the exact values are not inferred from the supplied couplings.',fontsize=11)
save(fig,'paper-1-karplus-projections.png')
