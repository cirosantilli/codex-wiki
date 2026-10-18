"""Original solution diagram. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.
Run from the directory where the PNG should be written.
"""
from pathlib import Path
import io
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Ellipse
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white", "savefig.transparent": False})

fig, ax = plt.subplots(figsize=(15.8, 6.8), layout="constrained")
positions = {}
for depth in range(5):
    for index in range(2**depth):
        positions[(depth,index)] = ((index+0.5)*16/(2**depth), -depth)
for depth in range(4):
    choices = ("T", "B") if depth % 2 == 0 else ("L", "R")
    for index in range(2**depth):
        x,y = positions[(depth,index)]
        for action in range(2):
            xx,yy = positions[(depth+1,2*index+action)]
            ax.plot([x,xx],[y,yy], color="0.4", lw=1, zorder=1)
            ax.text(0.5*(x+xx), 0.5*(y+yy)+0.04, choices[action], ha="center", fontsize=10, bbox={"facecolor":"white", "edgecolor":"none", "pad":0.5})
for depth in range(4):
    for index in range(2**depth):
        x,y=positions[(depth,index)]
        ax.scatter([x],[y],s=260,facecolor="white",edgecolor="#222222",zorder=4)
        ax.text(x,y,str(1+depth%2),ha="center",va="center",fontsize=10,zorder=5)
for index in range(4):
    x,y=positions[(2,index)]
    ax.text(x,y+0.25,("TL","TR","BL","BR")[index],ha="center",color="#2678b2",fontsize=10)
for depth,pairs in [(1,[(0,1)]),(3,[(0,1),(2,3),(4,5),(6,7)])]:
    for j,(a,b) in enumerate(pairs):
        x,y=positions[(depth,a)];xx,_=positions[(depth,b)]
        ax.plot([x,xx],[y,y],color="#a92a3b",ls="--",lw=1.7,zorder=2)
        ax.text((x+xx)/2,y+0.16,r"$I^0_2$" if depth==1 else r"$I_2^{"+("TL","TR","BL","BR")[j]+"}$",ha="center",color="#a92a3b",fontsize=10)
payoffs=np.array([[(1,5),(0,0)],[(0,0),(2,1)]])
for index in range(16):
    bits=[(index>>k)&1 for k in [3,2,1,0]]
    u=payoffs[bits[0],bits[1]]+payoffs[bits[2],bits[3]]
    x,y=positions[(4,index)]
    ax.text(x,y,f"({u[0]}, {u[1]})",ha="center",va="center",fontsize=9, bbox={"facecolor":"#edf3f5", "edgecolor":"none", "pad":2})
ax.set(xlim=(0,16),ylim=(-4.4,0.75))
ax.axis("off")
ax.set_title("Two rounds: dashed links are player 2's information sets; player 1's nodes are singleton sets",fontsize=13,pad=10)

buf = io.BytesIO()
fig.savefig(buf, format="png", dpi=160, facecolor="white", transparent=False, metadata={"Software": "Matplotlib"})
output = Path(Path(__file__).with_suffix(".png").name)
temporary = output.with_suffix(".png.tmp")
temporary.write_bytes(buf.getvalue())
os.replace(temporary, output)
plt.close(fig)
