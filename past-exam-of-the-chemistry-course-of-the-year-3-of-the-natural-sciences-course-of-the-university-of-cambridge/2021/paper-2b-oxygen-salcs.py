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

fig,axs=plt.subplots(2,2,figsize=(9,6.5));coords={'L':(-1.65,0),'R':(1.65,0),'T':(0,1),'B':(0,-1)}
entries=[(r'$X_g:\ B_{2g}$',{'L':1,'R':-1}),(r'$X_u:\ B_{1u}$',{'L':1,'R':1}),(r'$Y_g:\ B_{3g}$',{'T':1,'B':-1}),(r'$Y_u:\ B_{1u}$',{'T':1,'B':1})]
for ax,(title,signs) in zip(axs.flat,entries):
 ax.set_title(title);ax.set_aspect('equal');ax.axis('off');ax.set(xlim=(-2.1,2.1),ylim=(-1.5,1.5))
 ax.scatter([-0.8,.8],[0,0],s=20,c='0.65');ax.text(-.8,-.27,'C',ha='center',color='0.5',fontsize=9);ax.text(.8,-.27,'C',ha='center',color='0.5',fontsize=9)
 for label,(x,y) in coords.items():
  s=signs.get(label,0);col=BLUE if s>0 else ORANGE if s<0 else '0.88'
  ax.add_patch(Circle((x,y),.23,facecolor=col));ax.text(x,y,'+' if s>0 else '−' if s<0 else '0',ha='center',va='center',color='white' if s else '0.5',fontsize=18)
  ax.text(x,y+.34,'O'+label,ha='center',fontsize=9,color='0.3')
fig.suptitle('Oxygen SALCs: phases of the +z lobes; nonzero amplitudes 1/√2')
fig.tight_layout(rect=(0,0,1,.95))
fig.savefig("paper-2b-oxygen-salcs.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
