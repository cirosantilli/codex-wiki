"""Original explanatory figure. Python 3.14; root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,(ax,bx)=plt.subplots(1,2,figsize=(8,4),layout="constrained")
y=np.linspace(0,1,200);x=np.linspace(0,.6,80);X,Y=np.meshgrid(x,y);H=np.cos(np.pi*Y)
im=ax.pcolormesh(X,Y,H,shading="auto",cmap="RdBu_r",vmin=-1,vmax=1);ax.axhline(.5,color="#222",ls="--");ax.set(xlabel="Short direction (units of b)",ylabel="Long direction y/b",title=r"Closed tank: $h/A=\cos(\pi y/b)$",aspect="equal")
ax.text(.3,.93,"− antinode",ha="center");ax.text(.3,.06,"+ antinode",ha="center");ax.text(.3,.52,"node",ha="center",va="bottom")
fig.colorbar(im,ax=ax,label="Surface displacement / A",shrink=.75)
s=np.linspace(0,1,300);bx.plot(s,np.cos(np.pi*s/2),lw=2,color="#1565c0");bx.axhline(0,color="#999",lw=.8);bx.set(xlabel="Distance from closed head / L",ylabel="Surface displacement / A",title="One open end: quarter wavelength",xlim=(-.03,1.03),ylim=(-.05,1.15));bx.scatter([0,1],[1,0],color="#d84315");bx.annotate("Closed head: antinode",(0,1),xytext=(.12,1.05),fontsize=9);bx.annotate("Open mouth: node",(1,0),xytext=(.32,.2),arrowprops={"arrowstyle":"->"},fontsize=9);bx.grid(alpha=.2)

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
