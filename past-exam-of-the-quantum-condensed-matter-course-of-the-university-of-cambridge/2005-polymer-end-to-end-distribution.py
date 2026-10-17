"""Original scaled Gaussian-chain vector and radial density profiles."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

s=np.linspace(0,3,1200)
vector=(3/(2*np.pi))**1.5*np.exp(-1.5*s*s)
radial=4*np.pi*s*s*vector
fig,axes=plt.subplots(1,2,figsize=(9.0,3.9),layout="constrained")
axes[0].plot(s,vector,color="#2a729e",lw=2)
axes[0].set(xlabel=r"$s=R/\sqrt{Na^2}$",ylabel=r"$(Na^2)^{3/2}p(\mathbf{R})$",title="Density per vector volume")
axes[0].annotate("Largest at zero displacement",(0,vector[0]),(0.5,0.28),arrowprops={"arrowstyle":"->"},fontsize=10)
axes[1].plot(s,radial,color="#b1582a",lw=2)
axes[1].fill_between(s,0,radial,color="#e8bd9b",alpha=.35)
peak=np.sqrt(2/3)
axes[1].axvline(peak,color="#777777",ls="--",lw=1)
axes[1].text(1.2,0.96,r"Peak at $s=\sqrt{2/3}$",fontsize=10)
axes[1].set(xlabel=r"$s=R/\sqrt{Na^2}$",ylabel=r"$p_s(s)=4\pi s^2(3/2\pi)^{3/2}e^{-3s^2/2}$",title="Density per distance interval")
for ax in axes:ax.set_xlim(0,3);ax.set_ylim(bottom=0);ax.grid(alpha=.18)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
