"""Original Oxford CP2 2014 solution figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

t=np.linspace(0,10,800);e=np.exp(-t)
fig,ax=plt.subplots(figsize=(8,4.5),layout="constrained")
for vals,col,label,endval in [(.25*(1-e),"#146b9c",r"$I_1$ (coil branch)",.25),(.125*(1+e),"#d76c20",r"$I_2$ (resistor branch)",.125),(.125*(3-e),"#238357",r"$I_0=I_1+I_2$",.375)]:
    ax.plot(t,vals,lw=2.3,color=col,label=label)
    ax.plot(0,vals[0],"o",ms=5,color=col)
    ax.axhline(endval,color=col,ls=":",lw=.8)
ax.text(10.13,.375,r"$3/8$",va="center",color="#238357")
ax.text(10.13,.25,r"$1/4$",va="center",color="#146b9c")
ax.text(10.13,.125,r"$1/8$",va="center",color="#d76c20")
ax.annotate(r"$I_2(0)=I_0(0)=V/(4R)$",xy=(0,.25),xytext=(1,.29),fontsize=10,arrowprops={"arrowstyle":"-","color":".4"})
ax.set(xlim=(-.1,11),ylim=(-.015,.43),xlabel=r"$t/\tau$, with $\tau=L/(2R)$",ylabel=r"$RI/V$",title="Switch-on transient: inductor current is initially zero")
ax.legend(loc="lower right");ax.grid(alpha=.17)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, facecolor="white", metadata={"Software":"Oxford CP2 original Matplotlib figure"})
plt.close(fig)
