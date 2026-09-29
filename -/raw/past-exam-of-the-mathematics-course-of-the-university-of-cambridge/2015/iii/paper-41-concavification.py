"""Generate paper-41-concavification.png in the current directory.

Uses the repository's existing numpy and matplotlib dependencies.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

a,b,w0=0.4,1.0,3.0
lo=w0-(b/a-1-np.log(b/a))/(b-a)
hi=w0+(np.log(b/a)-1+a/b)/(b-a)
s=a*np.exp(-a*lo)
x=np.linspace(0,6,900)
F=np.where(x<=w0,-np.exp(-a*x),-np.exp((b-a)*w0-b*x))
envelope=np.where((x>lo)&(x<hi),-np.exp(-a*lo)+s*(x-lo),F)
fig,ax=plt.subplots(figsize=(8,4.2),dpi=100,facecolor="white")
ax.set_facecolor("white")
ax.plot(x,F,color="#285b9d",lw=2,label="Original incentive utility")
ax.plot(x,envelope,color="#cf5c27",lw=2,ls="--",label="Least concave majorant")
ax.scatter([lo,hi],[-np.exp(-a*lo),-np.exp((b-a)*w0-b*hi)],color="#cf5c27",zorder=5)
for xx,label in [(lo,r"$\ell$"),(w0,r"$w_0$"),(hi,r"$h$")]:
 ax.axvline(xx,color="0.8",lw=.8)
 ax.text(xx,-1.02,label,ha="center",va="top")
ax.set_xlim(0,6);ax.set_ylim(-1.08,.02)
ax.set_xlabel("Terminal fund wealth");ax.set_ylabel("Manager utility")
ax.set_title("A common tangent removes the incentive kink")
ax.legend(loc="lower right",frameon=False)
ax.grid(axis="y",alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/"paper-41-concavification.png",facecolor="white",transparent=False)
plt.close(fig)
