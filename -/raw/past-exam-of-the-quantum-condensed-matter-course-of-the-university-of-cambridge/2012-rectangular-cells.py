"""Original illustrative figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the corresponding _media directory; the PNG is written to cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

a=1.3;b=.8;K=np.pi/a;L=np.pi/b
fig,(ax,bx)=plt.subplots(1,2,figsize=(9,4),layout="constrained")
for i in range(-1,3):
 for j in range(-1,3):ax.plot(i*a,j*b,"ko",ms=4)
ax.add_patch(Rectangle((0,0),a,b,facecolor="#dbeafe",edgecolor="#2563eb",lw=2));ax.annotate("",xy=(a,0),xytext=(0,0),arrowprops={"arrowstyle":"->","color":"#dc2626","lw":2});ax.annotate("",xy=(0,b),xytext=(0,0),arrowprops={"arrowstyle":"->","color":"#059669","lw":2});ax.text(a/2,-.18,"a = 1.3 nm",ha="center");ax.text(-.1,b/2,"b = 0.8 nm",rotation=90,va="center",ha="right");ax.set(xlim=(-.5,2.05),ylim=(-.3,1.5),xlabel="x (nm)",ylabel="y (nm)",title="Real-space unit cell")
for i in range(-1,2):
 for j in range(-1,2):bx.plot(2*K*i,2*L*j,"ko",ms=4)
bx.add_patch(Rectangle((-K,-L),2*K,2*L,facecolor="#dbeafe",edgecolor="#2563eb",lw=2));bx.add_patch(Rectangle((0,0),2*K,2*L,fill=False,edgecolor="#dc2626",lw=1.5,ls="--"));bx.text(0,-L-.7,r"Width $2\pi/a=4.833$",ha="center");bx.text(-K-.5,0,r"Height $2\pi/b=7.854$",rotation=90,va="center",ha="right");bx.text(0,-1,"First BZ",ha="center",color="#2563eb");bx.set(xlim=(-4.2,5.9),ylim=(-5.3,8.9),xlabel=r"$k_x$ (nm$^{-1}$)",ylabel=r"$k_y$ (nm$^{-1}$)",title="Reciprocal unit cells")
for a in (ax,bx):a.set_aspect("equal");a.axhline(0,color="black",lw=.5);a.axvline(0,color="black",lw=.5)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, bbox_inches="tight", facecolor="white")
plt.close(fig)
