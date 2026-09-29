"""Original explanatory figure. Python 3.14; root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white"})

z=np.linspace(-1.4,1.4,700)
fig,ax=plt.subplots(figsize=(7,4),layout="constrained")
for D,color in [(.25,"#888"),(.5,"#1565c0"),(.75,"#d84315")]:
 B=(1+(z-D)**2)**(-1.5)+(1+(z+D)**2)**(-1.5);B0=2*(1+D*D)**(-1.5)
 ax.plot(z,B/B0,lw=2,label=f"Separation / radius = {2*D:g}",color=color)
ax.axhline(1,color="#bbb",ls=":");ax.set(xlabel="Axial position z/a",ylabel="B(z) / B(0)",title="The Helmholtz spacing removes the quadratic variation",ylim=(.35,1.12));ax.legend(fontsize=9);ax.grid(alpha=.2)

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
