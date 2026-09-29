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

angles=np.pi/2+2*np.pi*np.arange(5)/5
xy=np.column_stack([np.cos(angles),np.sin(angles)])
fig,axs=plt.subplots(2,5,figsize=(12,5.2))
for n,ax in enumerate(axs.flat):
 ax.plot(np.r_[xy[:,0],xy[0,0]],np.r_[xy[:,1],xy[0,1]],c='0.78',lw=1.3)
 for j,(x,y) in enumerate(xy):ax.text(1.23*x,1.23*y,str(j),ha='center',va='center',fontsize=9,color='0.4')
 x,y=xy[n%5];ax.add_patch(Circle((x,y),.13,facecolor='white',edgecolor=ORANGE,lw=1.8,zorder=4))
 if n%2:ax.plot([x-.065,x+.065],[y-.065,y+.065],c=ORANGE,zorder=5);ax.plot([x-.065,x+.065],[y+.065,y-.065],c=ORANGE,zorder=5)
 else:ax.scatter([x],[y],s=18,c=ORANGE,zorder=5)
 ax.set_title(r'$S_5^{'+str(n)+'}$',fontsize=13);ax.set(xlim=(-1.55,1.55),ylim=(-1.5,1.5));ax.set_aspect('equal');ax.axis('off')
fig.suptitle('Counterclockwise positions; dot = out of plane, cross = into plane')
fig.text(.5,.025,r'$S_5^5=\sigma_h$ reverses the arrow; $S_5^{10}=E$ restores it.',ha='center',fontsize=12)
fig.tight_layout(rect=(0,.07,1,.93))
fig.savefig("paper-2b-s5-powers.png", dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
