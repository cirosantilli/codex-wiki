"""Original ellipse and the single real hyperbolic-parametrization branch."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

a,b=2.,1.
angle=np.linspace(0,2*np.pi,900);hyper=np.linspace(-1.45,1.45,900)
fig,ax=plt.subplots(figsize=(7.1,4.5),layout="constrained")
ax.plot(a*np.cos(angle),b*np.sin(angle),color="#2b749f",lw=2,label=r"$(a\cos\theta,b\sin\theta)$: whole ellipse")
ax.plot(a*np.cosh(hyper),b*np.sinh(hyper),color="#b55a2c",lw=2,label=r"$(a\cosh\theta,b\sinh\theta)$: one branch")
x=np.linspace(-2.7,5,300)
for sign in [-1,1]:ax.plot(x,sign*b/a*x,color="#888888",ls="--",lw=1)
ax.scatter([a],[0],color="#333333",s=22,zorder=4)
ax.annotate("Shared vertex (a, 0)",(a,0),(.2,1.9),arrowprops={"arrowstyle":"->"},fontsize=10)
ax.axhline(0,color="#555555",lw=.7);ax.axvline(0,color="#555555",lw=.7)
ax.set(xlim=(-2.7,5),ylim=(-2.8,2.8),xlabel="x",ylabel="y",title="Example a = 2, b = 1: elimination alone would add a missing branch")
ax.set_aspect("equal");ax.grid(alpha=.16);ax.legend(loc="lower left",fontsize=9)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
