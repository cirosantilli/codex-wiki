"""Original solution diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired PNG output directory. No external image inputs.
"""
from pathlib import Path
import io
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white", "savefig.transparent": False})

fig, ax = plt.subplots(figsize=(7.6, 6.1), layout="constrained")
pos={"A":(-1.5,1.1),"B":(0,2),"G":(1.7,1.1),"D":(-.8,-.5),"F":(1,-.7),"C":(-2,-1.4),"E":(.1,.6)}
base=[("C","D"),("F","G"),("B","D"),("A","B"),("A","G"),("B","G"),("D","F")]
for a,b in base:
    ax.plot([pos[a][0],pos[b][0]],[pos[a][1],pos[b][1]],color="#2b4759",lw=2,zorder=1)
for v in "ABCDFG":
    ax.plot([pos["E"][0],pos[v][0]],[pos["E"][1],pos[v][1]],color="#b44b55",lw=1.8,ls="--",zorder=1)
slots={"A":1,"B":2,"C":1,"D":3,"E":4,"F":2,"G":3}
colors={1:"#dceafa",2:"#ffe4b5",3:"#dcefd9",4:"#f2d9e8"}
for v,(x,y) in pos.items():
    ax.scatter([x],[y],s=1150,color=colors[slots[v]],edgecolor="0.2",zorder=3)
    ax.text(x,y,v,ha="center",va="center",weight="bold",zorder=4)
    ax.text(x,y-.3,f"slot {slots[v]}",ha="center",fontsize=10,zorder=5)
ax.set(xlim=(-2.7,2.5),ylim=(-2,2.7))
ax.axis("off")
ax.set_title("Conflict graph for the stated audience-overlap assumptions",fontsize=13)
ax.text(-2.65,-1.98,"Solid: named shared audiences. Dashed: possible society overlaps, including Head of Department.",fontsize=8.5)

buffer = io.BytesIO()
fig.savefig(buffer, format="png", dpi=160, facecolor="white", transparent=False, metadata={"Software":"Matplotlib"})
output = Path(Path(__file__).with_suffix(".png").name)
temporary = output.with_suffix(".png.tmp")
temporary.write_bytes(buffer.getvalue())
os.replace(temporary, output)
plt.close(fig)
