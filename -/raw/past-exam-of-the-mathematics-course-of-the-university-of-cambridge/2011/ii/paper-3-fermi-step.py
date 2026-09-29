"""Zero-temperature Fermi occupation. Tested with Python 3.14.4 and Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 3.2), dpi=100, facecolor="white")
ax.plot([0,1],[1,1],color="#185f9a",lw=2.5)
ax.plot([1,1.8],[0,0],color="#185f9a",lw=2.5)
ax.plot([1,1],[0,1],ls=":",color="0.5")
ax.plot([1,1],[0,1],"o",mfc="white",mec="#185f9a",ms=6)
ax.set(xlim=(0,1.8),ylim=(-.15,1.2),xlabel=r"momentum $p/p_F$",ylabel=r"occupation $\bar n(p)$",title="Fermi occupation at zero temperature")
ax.set_yticks([0,1])
ax.set_xticks([0,1,1.5])
ax.grid(alpha=.15)
fig.subplots_adjust(left=.13,right=.97,bottom=.19,top=.85)
fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, facecolor="white", transparent=False)
plt.close(fig)
