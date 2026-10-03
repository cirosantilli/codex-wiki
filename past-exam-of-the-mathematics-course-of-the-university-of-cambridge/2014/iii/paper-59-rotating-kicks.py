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
fig,axes=plt.subplots(1,3,figsize=(10.8,4.2),layout="constrained")
s=np.linspace(0,2*np.pi,1200)
for ax,tit,th in zip(axes,["Forward tangential kick: θ = 0","Backward tangential kick: θ = π","Outward radial kick: θ = π/2"],[0,np.pi,np.pi/2]):
 x=2*np.cos(th)*(1-np.cos(s))+np.sin(th)*np.sin(s)
 y=np.cos(th)*(4*np.sin(s)-3*s)+2*np.sin(th)*(np.cos(s)-1)
 # Put along-orbit displacement horizontally, radial displacement vertically.
 ax.plot(y,x,lw=2,color="#2166ac")
 for ind in [70,320,750]:
  ax.annotate("",(y[ind+25],x[ind+25]),(y[ind],x[ind]),arrowprops={"arrowstyle":"->","color":"#b2182b"})
 ax.scatter([0],[0],color="black",s=24,zorder=3,label="source")
 ax.axhline(0,c="grey",lw=.6);ax.axvline(0,c="grey",lw=.6)
 ax.set(title=tit,xlabel="Along orbit y/(γa)",ylabel="Outward x/(γa)")
 ax.grid(alpha=.2);ax.legend(loc="best")
 ax.set_aspect("equal",adjustable="box")
fig.suptitle("Source rotating frame: one orbital period, leading order in γ")
fig.savefig(Path(__file__).stem+".png",dpi=100,facecolor="white",transparent=False)
