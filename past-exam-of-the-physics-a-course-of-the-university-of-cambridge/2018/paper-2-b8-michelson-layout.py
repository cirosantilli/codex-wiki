"""Original solution figure; tested with Python 3.14.4.
Uses NumPy 2.3.5 and Matplotlib 3.10.7 from the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
from matplotlib.patches import Rectangle
fig,ax=plt.subplots(figsize=(8.3,5.3),layout="constrained")
ax.set_xlim(-3.5,5.8);ax.set_ylim(-3.4,3.9);ax.axis("off")
# Shift the returning tracks slightly for readability; optical axes meet at BS.
ax.annotate("",xy=(-.25,0),xytext=(-3,0),arrowprops={"arrowstyle":"->","color":"#ca6720","lw":2})
ax.text(-3.2,.35,"Collimated source")
ax.plot([0,4.4],[0,0],color="#1565a8",lw=1.8)
ax.plot([0,0],[0,3],color="#1565a8",lw=1.8)
ax.plot([4.4,.15,.15],[.14,.14,-2.6],color="#33865b",lw=1.6)
ax.plot([-.13,-.13,0],[3,.12,0],color="#33865b",lw=1.6)
ax.plot([0,0],[-.05,-2.6],color="#1565a8",lw=1.8)
ax.plot([-.45,.45],[-.45,.45],color="0.15",lw=4)
ax.text(-.95,-.8,"50:50 beam\nsplitter",ha="center")
ax.plot([4.4,4.4],[-.6,.65],color="k",lw=5)
ax.plot([-.6,.65],[3,3],color="k",lw=5)
ax.text(3.65,.95,"M₁ (movable)")
ax.text(.75,3.05,"M₂ (fixed)")
ax.annotate("",xy=(4.9,-.1),xytext=(4,-.1),arrowprops={"arrowstyle":"<->","color":"#ca6720"})
ax.text(5,.05,"d")
ax.plot([1.45,1.75],[-.35,.45],color="0.5",lw=3)
ax.text(2.2,-1,"Compensating\nplate",ha="center")
ax.plot([-.4,.55],[-2.65,-2.65],color="k",lw=4)
ax.text(.75,-2.7,"Detector")
ax.text(-3.1,-1.3,"Blue: outgoing paths\nGreen: returning paths\n(offset for clarity)",fontsize=9)
ax.text(-3.1,-3.2,"A mirror motion d changes the optical path difference by 2d.",fontsize=10)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=135)
