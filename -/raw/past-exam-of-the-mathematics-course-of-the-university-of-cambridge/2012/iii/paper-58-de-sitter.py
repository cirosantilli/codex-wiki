"""Original schematic for Paper 58. Python 3.14; root matplotlib/numpy dependencies.
Caller supplies MPLCONFIGDIR; output is this script's basename PNG in cwd only.
"""
from pathlib import Path
import os
if not os.environ.get("MPLCONFIGDIR"):
    raise RuntimeError("Set MPLCONFIGDIR to a caller-owned writable cache directory")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
plt.rcParams.update({"font.size": 10, "axes.titlesize": 13})
fig,ax=plt.subplots(figsize=(8,5.2),facecolor="white")
P=np.pi
ax.add_patch(Polygon([(0,-P/2),(0,P/2),(P/2,0)],facecolor="#e6f0ff",edgecolor="none"))
ax.add_patch(Polygon([(P,-P/2),(P,P/2),(P/2,0)],facecolor="#e6f0ff",edgecolor="none"))
ax.plot([0,P,P,0,0],[-P/2,-P/2,P/2,P/2,-P/2],color="#333333",lw=1.8)
ax.plot([0,P],[-P/2,P/2],color="#a94727",lw=1.8)
ax.plot([0,P],[P/2,-P/2],color="#a94727",lw=1.8)
ax.text(.43,0,"north\nstatic patch",ha="center",va="center")
ax.text(P-.43,0,"south\nstatic patch",ha="center",va="center")
ax.text(P/2,.88,"expanding region",ha="center")
ax.text(P/2,-.88,"contracting region",ha="center")
ax.text(P/2,P/2+.16,r"$\mathcal{I}^+$ (spacelike)",ha="center")
ax.text(P/2,-P/2-.20,r"$\mathcal{I}^-$ (spacelike)",ha="center")
ax.text(-.18,0,r"$\psi=0$",rotation=90,va="center")
ax.text(P+.10,0,r"$\psi=\pi$",rotation=90,va="center")
ax.set_xlim(-.4,P+.4);ax.set_ylim(-P/2-.4,P/2+.4)
ax.set_aspect("equal");ax.axis("off")
ax.set_title("Global de Sitter spacetime")
fig.subplots_adjust(left=.06,right=.94,top=.88,bottom=.10)
fig.text(.5,.025,"Each interior point represents a two-sphere; pole lines are regular, not singular.",ha="center",fontsize=9)
fig.savefig(Path.cwd() / (Path(__file__).stem + ".png"), dpi=100, facecolor="white", transparent=False)
plt.close(fig)
