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

fig, ax = plt.subplots(figsize=(9.1, 4.5), layout="constrained")
pos={"S":(0,0), "P":(3,1.2), "G4":(6,1.2), "G5":(3,-1.3)}
for a,b,c in [("S","P",1),("P","G4",3),("S","G5",5)]:
    x,y=pos[a];xx,yy=pos[b]
    ax.add_patch(FancyArrowPatch((x,y),(xx,yy),shrinkA=30,shrinkB=30,arrowstyle="->",mutation_scale=18,lw=1.6))
    ax.text((x+xx)/2,(y+yy)/2+0.18,f"cost {c}",ha="center")
for key,(x,y) in pos.items():
    color="#def0de" if key.startswith("G") else "#e0ebf5"
    ax.add_patch(Circle((x,y),.42,facecolor=color,edgecolor="0.2",lw=1.5))
    ax.text(x,y,{"S":"S","P":"P","G4":r"$G_4$","G5":r"$G_5$"}[key],ha="center",va="center")
    h=3 if key=="P" else 0
    ax.text(x,y-.69,f"h = {h}",ha="center",fontsize=11)
ax.text(6,-1.25,"Goal path costs: 4 and 5",ha="center",fontsize=12)
ax.set(xlim=(-1,7.5),ylim=(-2.2,2.2))
ax.axis("off")
ax.set_title("An admissible, consistent heuristic still leaves all three altered rules suboptimal",fontsize=13)

buffer = io.BytesIO()
fig.savefig(buffer, format="png", dpi=160, facecolor="white", transparent=False, metadata={"Software":"Matplotlib"})
output = Path(Path(__file__).with_suffix(".png").name)
temporary = output.with_suffix(".png.tmp")
temporary.write_bytes(buffer.getvalue())
os.replace(temporary, output)
plt.close(fig)
