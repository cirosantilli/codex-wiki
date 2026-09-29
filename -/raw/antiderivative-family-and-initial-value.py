"""Original antiderivative family diagram; output matching PNG to CWD."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size":12,"figure.facecolor":"white"})
fig,(left,right)=plt.subplots(1,2,figsize=(10.6,4.8),layout="constrained")
x=np.linspace(-2,2,501)
for C,colour in [(-2,"#7d3c98"),(0,"#2855a6"),(2,"#087e8b")]:
    left.plot(x,x**3/3+C,color=colour,lw=1.8,label=rf"$C={C}$")
selected=5/3
left.plot(x,x**3/3+selected,color="#c45b12",lw=2.5,ls="--",label=r"$C=5/3$")
left.scatter([1],[2],color="#c45b12",s=55,zorder=3)
left.annotate(r"$F(1)=2$",xy=(1,2),xytext=(-.45,3.2),color="#c45b12",
              arrowprops={"arrowstyle":"->","color":"#c45b12"},fontsize=13)
left.set(xlim=(-2,2),ylim=(-5,5),xlabel=r"$x$",ylabel=r"$F_C(x)$",
         title=r"Antiderivatives $F_C(x)=x^3/3+C$")
left.legend(frameon=False,loc="lower right",fontsize=11)
right.plot(x,x*x,color="#333333",lw=2.7)
right.text(-1.3,2.5,r"$F_C'(x)=x^2$",fontsize=16)
right.text(0,1.5,"Every value of C\ngives this same derivative",fontsize=13,ha="center",
           bbox={"facecolor":"white","edgecolor":"none","alpha":.9,"pad":4})
right.set(xlim=(-2,2),ylim=(-.25,4.25),xlabel=r"$x$",ylabel=r"$g(x)$",
          title="One rate of change; different reference levels")
for ax in (left,right):
    ax.axhline(0,color="#aaaaaa",lw=.8)
    ax.axvline(0,color="#aaaaaa",lw=.8)
    ax.grid(alpha=.15)
fig.suptitle("A derivative determines change, while an initial value fixes the offset",fontsize=16)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
