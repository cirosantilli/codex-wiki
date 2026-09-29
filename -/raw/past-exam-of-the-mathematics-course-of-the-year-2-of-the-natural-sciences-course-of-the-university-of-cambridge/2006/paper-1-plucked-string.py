"""Original initial tent and Fourier-mode snapshots for a midpoint-plucked string."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,1,1201)
tent=2*np.minimum(x,1-x)
odd=np.arange(1,800,2)
coefficients=8/np.pi**2*np.sin(odd*np.pi/2)/odd**2
space=np.sin(np.pi*np.outer(x,odd))
fig,(initial,evolution)=plt.subplots(1,2,figsize=(9.2,4.2),layout="constrained")
initial.plot(x,tent,color="#245b9f",lw=2.2)
initial.plot([0,.5,1],[0,1,0],"o",color="#245b9f",ms=4)
initial.annotate(r"height $k$ at $L/2$",xy=(.5,1),xytext=(.52,1.11),fontsize=10)
initial.set(xlim=(0,1),ylim=(-.05,1.25),xlabel=r"$x/L$",ylabel=r"$u/k$",
            title="Initial displacement")
evolution.plot(x,tent,color=".6",ls=":",lw=1.1,label="initial reference")
for time,color in [(.25,"#245b9f"),(.5,"#65784a"),(1,"#b0522b")]:
    displacement=space@(coefficients*np.cos(odd*np.pi*time))
    evolution.plot(x,displacement,color=color,lw=1.8,label=f"ct/L = {time:g}")
evolution.set(xlim=(0,1),ylim=(-1.2,1.35),xlabel=r"$x/L$",ylabel=r"$u/k$",
              title="Later modal superpositions")
evolution.axhline(0,color=".6",lw=.7)
evolution.legend(loc="upper right",fontsize=9)
for ax in [initial,evolution]:ax.grid(alpha=.14)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
