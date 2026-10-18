"""Original Oxford CP2 2014 solution figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"axes.labelsize":12,"legend.fontsize":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","font.family":"DejaVu Sans"})

fig,ax=plt.subplots(figsize=(7,4),layout="constrained")
u=np.geomspace(.01,100,900)
phase=-np.arctan(u-1/u)*180/np.pi
ax.semilogx(u,phase,color="#146b9c",lw=2.5)
ax.axhline(0,color=".6",lw=.8);ax.axvline(1,color=".5",ls=":")
ax.axhline(90,color=".7",ls=":");ax.axhline(-90,color=".7",ls=":")
ax.plot(1,0,"ko",ms=5)
ax.set(xlim=(.01,100),ylim=(-100,100),yticks=[-90,-45,0,45,90],xlabel=r"$\omega/\omega_0$",ylabel="Current phase − voltage phase (degrees)",title=r"Series RLC: $\omega_0=1/\sqrt{LC}$, $\omega_0L/R=1$")
ax.text(.018,48,"Current leads\n(capacitive)",fontsize=11)
ax.text(6,-40,"Current lags\n(inductive)",fontsize=11)
ax.grid(alpha=.2)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=160, facecolor="white", metadata={"Software":"Oxford CP2 original Matplotlib figure"})
plt.close(fig)
