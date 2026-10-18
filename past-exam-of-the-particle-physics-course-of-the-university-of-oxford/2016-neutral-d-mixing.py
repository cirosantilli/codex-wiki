from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
plt.rcParams.update({"font.size": 12, "font.family": "DejaVu Sans", "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig,ax=plt.subplots(figsize=(8,4.7));t=np.linspace(0,20,401);r=.1;x=y=.01;gp=np.cos((x-1j*y)*t/2);gm=1j*np.sin((x-1j*y)*t/2)
for d,col,lab in [(0,"#2369a0",r"$\delta=0$"),(np.pi/2,"#bb4f39",r"$\delta=\pi/2$")]:
 exact=abs(r*np.exp(-1j*d)*gp+gm)**2/abs(gp+r*np.exp(-1j*d)*gm)**2
 leading=r*r+r*(y*np.cos(d)-x*np.sin(d))*t+(x*x+y*y)*t*t/4
 ax.plot(t,exact,color=col,lw=2.3,label=lab+", exact ratio");ax.plot(t,leading,color=col,ls="--",lw=1.4,label=lab+", leading small-r series")
ax.axhline(r*r,color="#555555",ls=":",lw=1.8,label="No mixing")
ax.set(xlim=(0,20),ylim=(0,.055),xlabel=r"$\tau=\Gamma t$",ylabel=r"$R=\mathrm{wrong\ sign}/\mathrm{right\ sign}$",title=r"Neutral D mixing: $x=y=0.01,\ r=0.1$")
ax.grid(alpha=.2);ax.legend(loc="upper left",fontsize=10);fig.tight_layout()

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=140, facecolor="white", transparent=False)
plt.close(fig)
