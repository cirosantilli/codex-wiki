"""Idealized layer-1 receiver wavelets with traction-positive reflection convention."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

t=np.linspace(-.1,.75,1801)
def w(t):
 a=(np.pi*22*t)**2
 return (1-2*a)*np.exp(-a)
fig,ax=plt.subplots(2,1,figsize=(8,4.7),layout="constrained",sharex=True)
r=-3/19
for a,name,dt,rb in [(ax[0],"P",.25,0),(ax[1],"S",.4166666667,1/9)]:
 a.plot(t,r*w(t)+(1-r*r)*rb*w(t-dt),color="#276792")
 a.axhline(0,color=".65",lw=.7)
 a.axvline(0,color=".65",ls=":")
 a.axvline(dt,color=".65",ls=":")
 a.text(.03,-.13,f"top: {r:+.4f}")
 a.text(dt+.025,.08,f"base: {(1-r*r)*rb:+.4f}")
 a.set(ylabel="Relative amplitude",ylim=(-.19,.16),title=f"{name} reflection: time measured from reservoir-top return")
ax[1].set_xlabel("Relative two-way time (s), illustrative reservoir thickness 250 m")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=100,facecolor="white",transparent=False)
