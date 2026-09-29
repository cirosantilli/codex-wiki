"""Original explanatory diagram; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import os
import numpy as np
os.environ.setdefault("MPLCONFIGDIR", "/tmp/cambridge-nano2-matplotlib")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, RegularPolygon, FancyArrowPatch, Wedge
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "savefig.facecolor": "white"})

fig,axs=plt.subplots(2,3,figsize=(10,5.6),layout="constrained")
for row in range(2):
    for stage in range(3):
        ax=axs[row,stage]
        ax.add_patch(Rectangle((0,0),4,2.8,fc="#edf4f8",ec=".6"))
        if row==1:ax.add_patch(Rectangle((0,0),4,.5,fc="#a5a5a5"))
        for x,y in [(.5,1.4),(3.5,2.2),(2.8,1.9),(.9,2.3)]:ax.plot(x,y,".",color="#246c99",ms=5)
        if stage:
            radius=.28 if stage==1 else .68
            center=(2,1.4) if row==0 else (2,.5)
            patch=Wedge(center,radius,0,180,fc="#ca9c35",ec="#8b6b1a") if row==1 else Circle(center,radius,fc="#ca9c35",ec="#8b6b1a")
            ax.add_patch(patch)
        ax.set(xlim=(-.1,4.1),ylim=(-.1,3));ax.axis("off")
        ax.set_title(["Dissolved precursor / reduction","Critical cluster","Growth of stable nucleus"][stage],fontsize=10)
        if stage==0:ax.text(.05,.07,"Homogeneous: free particle" if row==0 else "Heterogeneous: supported cap",transform=ax.transAxes,fontsize=9)
fig.suptitle("Solution heating supplies reactant mobility; favourable interfaces lower the nucleation barrier",fontsize=12)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145)
