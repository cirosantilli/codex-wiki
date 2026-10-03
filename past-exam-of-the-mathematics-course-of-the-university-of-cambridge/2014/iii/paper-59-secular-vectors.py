"""Original exam-solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Writes only the same-basename PNG in the current working directory.
Uses MPLCONFIGDIR supplied by the caller.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white"})
fig,axes=plt.subplots(1,2,figsize=(9,4.4),layout="constrained")
for ax,vp,vm,j in [(axes[0],np.sqrt(3)*np.exp(1j*np.pi/6),np.exp(2j*np.pi/3),1),(axes[1],np.exp(7j*np.pi/6),np.sqrt(3)*np.exp(2j*np.pi/3),2)]:
 def arrow(v,start,col,label):
  ax.annotate("",(v.real+start.real,v.imag+start.imag),(start.real,start.imag),arrowprops={"arrowstyle":"->","color":col,"lw":2})
  ax.plot([],[],c=col,label=label)
 arrow(vp,0j,"#2166ac","upper mode p")
 arrow(vm,vp,"#4d9221","lower mode m (translated)")
 arrow(vp+vm,0j,"#b2182b","resultant")
 ax.plot([0,vm.real],[0,vm.imag],"--",color="#4d9221",alpha=.65)
 ax.axhline(0,c="grey",lw=.7);ax.axvline(0,c="grey",lw=.7)
 ax.set(xlim=(-2.15,2.15),ylim=(-.85,2.15),xlabel="Re z",ylabel="Im z",title=f"Planet {j}: resultant at {60 if j==1 else 150}°")
 ax.grid(alpha=.2);ax.set_aspect("equal");ax.legend(loc="lower right",fontsize=8)
fig.suptitle("Initial complex eccentricities; drawing normalization B = 1, s = 1")
fig.savefig(Path(__file__).stem+".png",dpi=100,facecolor="white",transparent=False)
