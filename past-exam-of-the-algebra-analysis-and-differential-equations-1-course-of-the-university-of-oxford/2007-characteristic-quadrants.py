"""Original characteristic projections. Python3.14, NumPy, Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(6,5),facecolor="white")
ax.fill_between([0,4],0,4,color="#eef7fb");ax.fill_between([-4,0],-4,0,color="#eef7fb")
for s in [-2,-1,-.5,.5,1,2]:
 r=np.linspace(.03,4,400);x=np.sign(s)*r;y=x*x/s;mask=np.abs(y)<=4
 ax.plot(x[mask],y[mask],color="#2166ac",lw=1.4)
 ax.scatter([s],[s],color="#b2182b",s=25,zorder=4)
ax.plot([-4,4],[-4,4],ls="--",color="#b2182b",alpha=.5,label="initial line y=x")
ax.axhline(0,color=".5",lw=.8);ax.axvline(0,color=".5",lw=.8)
ax.text(1.75,.4,r"$xy>0$",fontsize=13);ax.text(-2.7,-.6,r"$xy>0$",fontsize=13)
ax.text(-3.7,2.7,"not reached",fontsize=11,color=".4");ax.text(2,-3,"not reached",fontsize=11,color=".4")
ax.set(xlim=(-4,4),ylim=(-4,4),aspect="equal",xlabel="x",ylabel="y",
       title=r"Projected characteristics $y=x^2/s$, with $x/s>0$")
ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper right",fontsize=9)
fig.tight_layout();fig.savefig("2007-characteristic-quadrants.png",dpi=150,facecolor="white")
