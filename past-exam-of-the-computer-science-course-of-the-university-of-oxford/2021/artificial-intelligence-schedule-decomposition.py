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

fig,ax=plt.subplots(figsize=(9.5,4.8),layout="constrained")
pos={"K1":(0,1),"K2":(3,1),"K3":(6,1),"K4":(3,-1)}
for a,b in [("K1","K2"),("K2","K3"),("K2","K4")]:
    ax.plot([pos[a][0],pos[b][0]],[pos[a][1],pos[b][1]],color="0.35",lw=2)
labels={"K1":"K1\n{A, B, E, G}","K2":"K2\n{B, D, E, G}","K3":"K3\n{D, E, F, G}","K4":"K4\n{C, D, E}"}
for key,(x,y) in pos.items():
    ax.text(x,y,labels[key],ha="center",va="center",bbox={"boxstyle":"round,pad=.75","facecolor":"#e1edf5","edgecolor":"0.2"},fontsize=13)
ax.set(xlim=(-1.5,7.5),ylim=(-2,2.1))
ax.axis("off")
ax.set_title("A width-3 tree decomposition: largest bag has four vertices",fontsize=14)

buffer = io.BytesIO()
fig.savefig(buffer, format="png", dpi=160, facecolor="white", transparent=False, metadata={"Software":"Matplotlib"})
output = Path(Path(__file__).with_suffix(".png").name)
temporary = output.with_suffix(".png.tmp")
temporary.write_bytes(buffer.getvalue())
os.replace(temporary, output)
plt.close(fig)
