"""Question 14 equilibrium branches. Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7.6, 4.4), dpi=100, facecolor="white")
lo = np.linspace(0.05, 1, 200)
hi = np.linspace(1, 1.5, 200)
interior = np.linspace(1, 1.25, 300)
root = np.sqrt(np.maximum(5 - 4 * interior, 0))
color = "#185f9a"
ax.plot(lo, 0 * lo, color=color, lw=2, label="stable")
ax.plot(hi, 0 * hi, color=color, lw=2, ls="--", label="unstable")
ax.plot(lo, lo, color=color, lw=2, ls="--")
ax.plot(hi, hi, color=color, lw=2)
ax.plot(interior, (1 - root)/2, color="#ad4e11", lw=2)
ax.plot(interior, (1 + root)/2, color="#ad4e11", lw=2, ls="--")
for x,y,label,offset in [(1,0,"transcritical",(-95,20)),(1,1,"pitchfork",(-80,20)),(1.25,.5,"saddle-node",(15,-20))]:
    ax.plot(x,y,"o",color="black",ms=5)
    ax.annotate(label,(x,y),xytext=offset,textcoords="offset points",fontsize=10,arrowprops={"arrowstyle":"-","color":"0.4"})
ax.text(.35,.37,r"$(0,\mu)$",fontsize=11,rotation=28)
ax.text(.38,.045,r"$(1,0)$",fontsize=11)
ax.text(1.08,.22,r"$y_-$",fontsize=12,color="#ad4e11")
ax.text(1.08,.86,r"$y_+$",fontsize=12,color="#ad4e11")
ax.set(xlim=(0,1.52),ylim=(-.08,1.55),xlabel=r"parameter $\mu$",ylabel=r"equilibrium coordinate $y$",title="Boundary and interior equilibria")
ax.set_xticks([0,.5,1,1.25,1.5])
ax.grid(alpha=.2)
ax.legend(loc="upper left",frameon=False)
fig.subplots_adjust(left=.11,right=.97,bottom=.14,top=.9)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
plt.close(fig)
