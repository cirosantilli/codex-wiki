"""Original Oxford CP2 2014 solution figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

fig,ax=plt.subplots(figsize=(7,4),layout="constrained")
u=np.linspace(0,1,200);v=np.linspace(1,4.5,400)
ax.plot(u,u,color="#146b9c",lw=2.5,label=r"Inside: $B\propto r$")
ax.plot(v,1/v,color="#d76c20",lw=2.5,label=r"Outside: $B\propto 1/r$")
ax.axvline(1,color=".5",ls=":");ax.plot(1,1,"ko",ms=5)
ax.set(xlim=(0,4.5),ylim=(0,1.15),xlabel=r"$r/a$",ylabel=r"$B/[\mu_0 I/(2\pi a)]$",title="Uniform current density in a long circular wire")
ax.legend();ax.grid(alpha=.2)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, facecolor="white", metadata={"Software":"Oxford CP2 original Matplotlib figure"})
plt.close(fig)
