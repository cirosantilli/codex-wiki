"""Original explanatory figure; run from the mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "figure.facecolor": "white", "axes.facecolor": "white"})

fig,axs=plt.subplots(1,2,figsize=(8,3.4),layout='constrained');x=np.linspace(.001,4,800)
axs[0].plot(x,np.where(x<=1,x,x**-2));axs[1].plot(x,np.where(x<=1,(3-x*x)/2,1/x));axs[0].plot(0,0,'o');axs[1].plot(0,1.5,'o')
axs[0].set(ylabel=r'$E/E(R)$',title='Electric field magnitude');axs[1].set(ylabel=r'$V/V(R)$',title=r'Potential with $V(\infty)=0$')
for a in axs:a.axvline(1,color='0.6',ls='--',label='Surface');a.set(xlabel=r'$r/R$',xlim=(0,4),ylim=(0,1.65));a.grid(alpha=.2);a.legend(fontsize=8)

fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name, dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
