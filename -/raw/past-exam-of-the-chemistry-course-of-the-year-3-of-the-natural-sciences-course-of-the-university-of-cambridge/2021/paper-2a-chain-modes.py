#!/usr/bin/env python3
"""Original explanatory schematic; Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})

fig,axs=plt.subplots(4,1,figsize=(9,6.3),sharex=True)
xs=np.array([0,1,3,4.]);vectors=[(1,1,1,1),(-1,-1,1,1),(-1,1,-1,1),(-1,1,1,-1)]
names=[r'$t:\ \Sigma_u^+$, translation',r'$r:\ \Sigma_g^+$, relative translation',r'$s:\ \Sigma_g^+$, in-phase stretch',r'$a:\ \Sigma_u^+$, opposite stretches']
for ax,v,name in zip(axs,vectors,names):
 ax.plot([0,1],[0,0],c='0.65',lw=2);ax.plot([3,4],[0,0],c='0.65',lw=2)
 ax.scatter(xs,np.zeros(4),s=85,c='#356a9e',zorder=3)
 for i,(x,d) in enumerate(zip(xs,v),1):
  ax.annotate('',(x+.36*d,.28),(x,.28),arrowprops={'arrowstyle':'->','color':'#bb4c21','lw':2})
  ax.text(x,-.33,str(i),ha='center',fontsize=10)
 ax.text(-.6,.82,name,va='center',fontsize=11)
 ax.set(xlim=(-1.4,4.6),ylim=(-.5,1.1));ax.axis('off')
fig.suptitle('Symmetry coordinates: arrow amplitudes are ±1/2')
fig.tight_layout(rect=(0,0,1,.94))
fig.savefig("paper-2a-chain-modes.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
