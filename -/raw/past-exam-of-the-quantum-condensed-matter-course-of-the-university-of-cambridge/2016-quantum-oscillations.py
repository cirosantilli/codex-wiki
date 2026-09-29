"""Original explanatory plot; run from the corresponding _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(9,3.6),layout='constrained');B=np.linspace(.045,.4,600)
for n in range(14):axs[0].plot(B,(n+.5)*B,lw=1)
axs[0].axhline(1,color='black',ls='--',label=r'$E_F$');axs[0].set(xlabel=r'$B/F$',ylabel=r'$E_\ell/E_F$',ylim=(0,1.8),xlim=(.045,.4),title='Orbital levels cross a fixed Fermi energy');axs[0].legend(fontsize=8)
x=np.linspace(2.5,14,1600);axs[1].plot(x,np.cos(2*np.pi*x),color='tab:blue');axs[1].set(xlabel=r'$F/B$',ylabel='Oscillatory response (arbitrary units)',title='Equal spacing in inverse field');axs[1].axhline(0,color='0.7',lw=.7)
for a in axs:a.grid(alpha=.15)
fig.suptitle('Illustrative transverse parabolic-band levels and an undamped inverse-field harmonic')

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
