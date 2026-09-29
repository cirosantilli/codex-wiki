"""Conceptual lytic cycle, not an experimental protocol; Python 3.14/Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(10, 2.3), facecolor="white")
ax.set(xlim=(0, 10), ylim=(0, 2.1))
ax.axis("off")
labels=["Host\nrecognition", "Genome\ndelivery", "Genome copying\nand protein\nproduction", "Assembly and\nATP-powered\npackaging", "Progeny\nrelease"]
for i,label in enumerate(labels):
    x=.12+2*i
    ax.add_patch(FancyBboxPatch((x,.65),1.65,.90,boxstyle="round,pad=0.06",facecolor="#e8f1fa",edgecolor="#285780"))
    ax.text(x+.825,1.10,label,ha="center",va="center",fontsize=10)
    if i<4:
        ax.annotate("",xy=(x+1.95,1.10),xytext=(x+1.73,1.10),arrowprops={"arrowstyle":"->","lw":1.8,"color":"#285780"})
ax.text(5,1.94,"Conceptual lytic bacteriophage cycle",ha="center",fontsize=13)
ax.text(5,.20,"Packaging stores free energy in confined DNA and its ionic environment.",ha="center",fontsize=10)
fig.subplots_adjust(left=.015,right=.985,bottom=.02,top=.98)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False)
