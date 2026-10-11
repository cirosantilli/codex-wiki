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
fig,ax=plt.subplots(figsize=(8.1,3.9),layout="constrained")
t=np.linspace(0,2.4,700)
# Schematic smooth interpolation: T^5 at low T, T at high T.
p=t**5/(.28**4+t**4)
ax.plot(t,.13+p,lw=2,color="#1565a8",label="purer metal")
ax.plot(t,.68+p,lw=2,color="#ca6720",label="additional static disorder")
ax.axhline(.13,color="#1565a8",ls=":",lw=1)
ax.axhline(.68,color="#ca6720",ls=":",lw=1)
ax.annotate("residual plateaus",xy=(.03,.4),xytext=(.45,.4),arrowprops={"arrowstyle":"->"})
ax.annotate(r"phonon contribution $\propto T^5$",xy=(.24,.23),xytext=(.45,1.2),arrowprops={"arrowstyle":"->"})
ax.annotate(r"approximately $\propto T$",xy=(1.8,1.93),xytext=(1.05,2.7),arrowprops={"arrowstyle":"->"})
ax.set(xlabel="Temperature (schematic)",ylabel="Electrical resistivity (arbitrary units)",xlim=(0,2.4),ylim=(0,3.3))
ax.set_xticks([]);ax.set_yticks([])
ax.legend(frameon=False,loc="upper left")
ax.set_title("Normal-metal phonon + disorder model; not measured iron or steel curves")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=135)
