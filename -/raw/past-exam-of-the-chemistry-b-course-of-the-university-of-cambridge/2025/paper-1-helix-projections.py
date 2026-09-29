"""Idealized consecutive side-chain directions in three peptide helices."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import *
fig,axs=plt.subplots(1,3,figsize=(12,4.1),layout='constrained',facecolor='white')
for ax,n,res,title in zip(axs,[3,3.6,4.4],[6,8,9],['3₁₀: i → i+3','α: i → i+4','π: i → i+5']):
 ax.add_patch(plt.Circle((0,0),.55,fill=False,ec='0.7'))
 for j in range(res):
  th=np.pi/2-j*2*np.pi/n;v=np.array([np.cos(th),np.sin(th)]);r=.95+.18*(j//3) if n==3 else 1.05
  ax.annotate('',r*v,.55*v,arrowprops={'arrowstyle':'->','color':plt.cm.viridis(j/(res-1)),'lw':1.6});ax.text(*(v*(r+.17)),str(j+1),ha='center',va='center',fontsize=11)
 ax.text(0,-1.8,f'~{n:g} residues / turn\n~{360/n:.0f}° / residue',ha='center',fontsize=11);finish(ax,(-1.65,1.65),(-2.15,1.65),title)
fig.suptitle('Top views; numbers follow the chain. Axial rise and detailed side-chain conformations are omitted.',fontsize=12)
save(fig,'paper-1-helix-projections.png')
