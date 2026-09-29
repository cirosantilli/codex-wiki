"""Original explanatory figure. Python 3.14; root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,ax=plt.subplots(figsize=(6,4.1),layout="constrained");ax.set(xlim=(-2.2,3.6),ylim=(-1.7,3.3));ax.axis("off")
blue="#1565c0";orange="#ef6c00"
ax.annotate("",xy=(0,0),xytext=(-1.8,0),arrowprops={"arrowstyle":"->","color":"#444","lw":2});ax.text(-1.9,.3,"Coherent source",fontsize=10)
ax.plot([-.22,.22],[-.22,.22],lw=4,color="#444");ax.text(-.3,.55,"Beam splitter",ha="right")
ax.plot([0,2.8],[.05,.05],color=blue,lw=2);ax.annotate("",xy=(1.7,.05),xytext=(.9,.05),arrowprops={"arrowstyle":"->","color":blue})
ax.plot([2.8,0],[-.05,-.05],color=orange,lw=2);ax.annotate("",xy=(.9,-.05),xytext=(1.7,-.05),arrowprops={"arrowstyle":"->","color":orange})
ax.plot([-.05,-.05],[0,2.7],color=blue,lw=2);ax.annotate("",xy=(-.05,1.7),xytext=(-.05,.9),arrowprops={"arrowstyle":"->","color":blue})
ax.plot([.05,.05],[2.7,0],color=orange,lw=2);ax.annotate("",xy=(.05,.9),xytext=(.05,1.7),arrowprops={"arrowstyle":"->","color":orange})
ax.plot([2.8,2.8],[-.35,.35],color="#333",lw=5);ax.text(2.9,.55,"Mirror 1",ha="center")
ax.plot([-.35,.35],[2.7,2.7],color="#333",lw=5);ax.text(.5,2.7,"Mirror 2",va="center")
ax.annotate("",xy=(0,-1.25),xytext=(0,-.25),arrowprops={"arrowstyle":"->","color":"#7b1fa2","lw":2});ax.text(.2,-1.1,"Recombined beams\nto fringe detector",va="center")
ax.text(1.5,.45,r"Arm length $\ell$",ha="center");ax.text(-.25,1.45,r"$\ell$",ha="right")
ax.text(-1.85,-1.45,"Rotate the complete optical system to test orientation dependence.",fontsize=9)
ax.set_title("Conceptual round-trip comparison; single-pass schematic")

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
