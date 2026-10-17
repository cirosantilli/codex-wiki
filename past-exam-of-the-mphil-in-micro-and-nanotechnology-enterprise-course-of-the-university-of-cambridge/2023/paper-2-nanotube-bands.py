"""Original explanatory diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import os
import numpy as np
os.environ.setdefault("MPLCONFIGDIR", "/tmp/cambridge-nano2-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon, FancyArrowPatch, Wedge
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "savefig.facecolor": "white"})

fig, axs = plt.subplots(1, 3, figsize=(11, 3.8), layout="constrained")
k = np.linspace(-1, 1, 300)
for ax, metal in zip(axs[:2], [False, True]):
    for j, gap in enumerate(([.48, .92] if not metal else [.78, 1.2])):
        E = np.sqrt(k*k+gap*gap)
        ax.plot(k, E, color="#246c99"); ax.plot(k, -E, color="#246c99")
        if j == 0 or not metal:
            x = .1 + .2*j
            y = np.sqrt(x*x+gap*gap)
            ax.annotate("", (x,y),(x,-y), arrowprops=dict(arrowstyle="<->", color="#b23a37"))
            ax.text(x+.06, 0, ("M" if metal else "S")+str(j+1)*2, color="#b23a37")
    if metal:
        ax.plot(k, k, "k", lw=1.2); ax.plot(k, -k, "k", lw=1.2)
    ax.axhline(0,color=".6",lw=.7,ls="--"); ax.set(xlabel="Axial wave vector (schematic)", ylabel="Energy", ylim=(-1.65,1.65), title="Metallic tube" if metal else "Semiconducting tube", xticks=[],yticks=[])
ax = axs[2]
a1=np.array([1.,0.]);a2=np.array([.5,np.sqrt(3)/2])
for i in range(-1,9):
    for j in range(-1,8):
        v=i*a1+j*a2; ax.plot(*v, ".",color=".75",ms=3)
for v, label, color in [(a1*6+a2*6,"(6,6): metallic","#246c99"),(a1*7,"(7,0): semiconducting","#b23a37")]:
    ax.annotate("",v,(0,0),arrowprops=dict(arrowstyle="-|>",color=color,lw=2))
    ax.text(v[0]*.5,v[1]*.5+.3,label,rotation=np.degrees(np.arctan2(v[1],v[0])),color=color,ha="center")
for a,l in [(a1,r"$\mathbf{a}_1$"),(a2,r"$\mathbf{a}_2$")]:
    ax.annotate("",a*2,(0,0),arrowprops=dict(arrowstyle="->",lw=1.5));ax.text(*(a*2.2),l)
ax.set(aspect="equal",xlim=(-.5,10),ylim=(-1,7),xticks=[],yticks=[],title="Roll-up vectors on Bravais lattice")
ax.text(.02,.02,"Points mark unit cells;\neach cell contains two carbon atoms.",transform=ax.transAxes,fontsize=8)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145)
