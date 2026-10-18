"""Original geometry; Python 3.14 with numpy/matplotlib. Writes exactly one PNG in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

u=np.linspace(-6,6,800);f=4*np.arctan(np.exp(u));density=4/np.cosh(u)**2
fig,axs=plt.subplots(1,2,figsize=(11,4.2),layout="constrained")
axs[0].plot(u,f,color="#165b91",lw=2);axs[0].set(xlabel="u = sqrt(ab) (x - center)",ylabel="b phi",title="Kink between neighboring vacua",yticks=[0,np.pi,2*np.pi],yticklabels=["0","pi","2 pi"])
axs[0].axhline(0,color="gray",ls=":");axs[0].axhline(2*np.pi,color="gray",ls=":")
axs[1].plot(u,density,color="#bf5a13",lw=2);axs[1].fill_between(u,density,color="#bf5a13",alpha=.15)
axs[1].set(xlabel="u = sqrt(ab) (x - center)",ylabel="b squared / (ab) times energy density",title="Localized energy: integral in u equals 8")
for ax in axs:ax.grid(alpha=.2)
save(fig)
