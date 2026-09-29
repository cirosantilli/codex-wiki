"""Original analytic teaching diagram; Python 3.14, numpy, matplotlib.
Run from the desired output directory; writes its basename PNG to cwd.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

r=np.linspace(1.0001,10,1200);f=1-1/r
fig,ax=plt.subplots(figsize=(8,4.5),layout="constrained")
for asym,col in [(0,"#326a97"),(.6,"#aa5c31")]:
 local=np.sqrt(asym**2+(1-asym**2)/r);coordinate=f*local
 ax.plot(r,local,color=col,lw=2,label=f"local speed, u/c = {asym:g}")
 ax.plot(r,coordinate,color=col,lw=1.6,ls="--",label=f"coordinate speed, u/c = {asym:g}")
ax.axvline(1,color="#777777",ls=":");ax.set(xlim=(.9,10),ylim=(0,1.03),xlabel="Areal radius / Schwarzschild radius",ylabel="Outward radial speed / c",title="Local rulers and clocks give a different speed from dr/dt")
ax.legend(fontsize=9,loc="center right");ax.grid(alpha=.2)
fig.savefig("paper-1-schwarzschild-speeds.png",dpi=155,facecolor="white")
