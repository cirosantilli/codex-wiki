"""Original CP2 2013 resit figure; Python 3.14, NumPy and Matplotlib root dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

t=np.linspace(0,22,1800)
fig,ax=plt.subplots(figsize=(8.4,4.5),layout="constrained")
for rho,label,col in [(.5,"Underdamped", "#146b9c"),(2,"Critical damping", "#d76c20"),(3,"Overdamped", "#27835b")]:
    alpha=rho/2
    if alpha<1:
        wd=np.sqrt(1-alpha*alpha);cur=np.exp(-alpha*t)*np.sin(wd*t)/wd
    elif alpha==1:cur=t*np.exp(-t)
    else:
        beta=np.sqrt(alpha*alpha-1);cur=(np.exp((-alpha+beta)*t)-np.exp((-alpha-beta)*t))/(2*beta)
    ax.plot(t,cur,lw=2.2,color=col,label=label+rf", $R\sqrt{{C/L}}={rho:g}$")
ax.axhline(0,color=".6",lw=.8)
ax.set(xlim=(0,22),xlabel=r"$t/\sqrt{LC}$",ylabel=r"$I/[V_0\sqrt{C/L}]$",title="Series RLC voltage step: zero initial charge and current")
ax.legend();ax.grid(alpha=.2)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white",metadata={"Software":"Original CP2 solution figure"})
plt.close(fig)
