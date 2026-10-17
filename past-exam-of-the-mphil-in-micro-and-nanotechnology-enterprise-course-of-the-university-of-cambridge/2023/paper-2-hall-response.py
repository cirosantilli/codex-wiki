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

fig,axs=plt.subplots(1,2,figsize=(9,3.5),layout="constrained")
B=np.linspace(.5,7,3000);bfill=6.4746
nu=np.maximum(1,np.floor(bfill/B+.5))
axs[0].plot(B,4*B,"--",color=".5",label="Classical")
axs[0].plot(B,25.8984/nu,color="#246c99",label="Illustrative integer plateaux")
axs[0].set(xlabel="Magnetic flux density B (T)",ylabel=r"$|\rho_{xy}|$ (k$\Omega$)",title="Sheet Hall resistivity");axs[0].legend(fontsize=8)
axs[1].plot(B,np.abs(np.sin(np.pi*bfill/B))**12,color="#b23a37")
axs[1].set(xlabel="Magnetic flux density B (T)",ylabel=r"$\rho_{xx}$ (schematic)",title="Dissipative peaks between plateaux",yticks=[])
fig.suptitle("Illustrative disorder-broadened integer quantum Hall response; not a fit")
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=145)
