"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.6),layout='constrained');B=np.linspace(0,5,300)
for mu in [.2,.35,.6,1]:
 rho0=1/(2*mu);MR=(mu*B)**2;label=rf'$\mu={mu:g}$'
 axs[0].plot(B,MR,label=label);axs[1].plot((B/rho0)**2,MR,label=label)
axs[0].set(xlabel='Magnetic field (model units)',ylabel=r'$[\rho(B)-\rho(0)]/\rho(0)$',title='Changing mobility changes the field curve');axs[0].legend(fontsize=8)
axs[1].set(xlabel=r'$[B/\rho(0)]^2$ (model units)',ylabel=r'$[\rho(B)-\rho(0)]/\rho(0)$',title='All curves follow a common straight line')
for a in axs:a.grid(alpha=.2)
fig.suptitle(r'Original equal-density, equal-mobility model with $ne=1$; these are not the exam data')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
