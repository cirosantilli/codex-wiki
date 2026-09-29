"""Original solution figure; tested with Python 3.14.4.
Dependencies: NumPy 2.3.5 and Matplotlib 3.10.7 (root pyproject.toml).
Writes its PNG basename into the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","axes.spines.top":False,"axes.spines.right":False})
from matplotlib.patches import Rectangle
fig,ax=plt.subplots(figsize=(6,5.2),layout="constrained")
x,y=np.meshgrid([-2,0,2],[-2,0,2]);ax.scatter(x,y,color=".25",s=27)
ax.add_patch(Rectangle((-1,-1),2,2,facecolor="#1565a8",edgecolor="#1565a8",alpha=.15,lw=2))
for z in [-1,1]:
 ax.axvline(z,color="#1565a8",ls="--",lw=1);ax.axhline(z,color="#1565a8",ls="--",lw=1)
ax.annotate("",xy=(2,0),xytext=(0,0),arrowprops={"arrowstyle":"->","color":"#ca6720","lw":2})
ax.annotate("",xy=(0,2),xytext=(0,0),arrowprops={"arrowstyle":"->","color":"#33865b","lw":2})
ax.text(1.4,.16,r"$\mathbf{b}_1$",color="#ca6720")
ax.text(.14,1.5,r"$\mathbf{b}_2$",color="#33865b")
ax.text(0,-.55,"first Brillouin zone",ha="center",fontsize=9)
ax.text(-.2,.1,"0",fontsize=9)
ax.set(xlim=(-2.7,2.7),ylim=(-2.7,2.7),xticks=[-2,-1,0,1,2],yticks=[-2,-1,0,1,2],xlabel=r"$k_x/(\pi/a)$",ylabel=r"$k_y/(\pi/a)$",aspect="equal",title="Square direct lattice: spacing a\nReciprocal spacing 2π/a; bisectors at ±π/a")
ax.grid(alpha=.13)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=135)
