#!/usr/bin/env python3
"""Original solution figure. Python 3.14; numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({"font.size":11,"axes.spines.top":False,"axes.spines.right":False})
BLUE="#276ba2"
ORANGE="#c7602b"

fig,ax=plt.subplots(figsize=(9,4.5));ax.axis('off');ax.set(xlim=(-.7,3.7),ylim=(-1.3,1.5))
upper=[1,-1,1,-1];labels=['Carbon on +y','Carbon on +x','Carbon on −y','Carbon on −x']
for j in range(4):
 ax.text(j,1.25,labels[j],ha='center',fontsize=10)
 for row,sign,index in [(.55,upper[j],2*j+1),(-.55,-upper[j],2*j+2)]:
  color=BLUE if sign>0 else ORANGE
  ax.add_patch(Circle((j,row),.22,color=color,alpha=.85));ax.text(j,row,'+' if sign>0 else '−',ha='center',va='center',color='white',fontsize=22)
  ax.text(j,row-.37,r'$h_'+str(index)+'$',ha='center',fontsize=12)
 ax.plot([j,j],[-.2,.2],c='0.75',lw=1)
ax.text(-.65,.55,'Above\nring',ha='left',va='center',fontsize=10)
ax.text(-.65,-.55,'Below\nring',ha='left',va='center',fontsize=10)
ax.set_title(r'$B_{2u}$ hydrogen SALC: every amplitude has magnitude $1/\sqrt{8}$',pad=20)
fig.tight_layout()
fig.savefig("paper-2b-cyclobutane-salc.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
