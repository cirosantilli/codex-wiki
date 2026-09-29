"""Original Gaussian spreading with and without a uniform growth term."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-7,7,1400)
fig,axes=plt.subplots(1,2,figsize=(9.1,3.8),layout="constrained",sharey=True)
for time,color in [(0.5,"#aa4928"),(1,"#24719b"),(2,"#568a3c")]:
    gaussian=np.exp(-x*x/(4*time))
    axes[0].plot(x,gaussian/np.sqrt(time),color=color,lw=2,label=f"t = {time:g}")
    axes[1].plot(x,np.sqrt(time)*gaussian,color=color,lw=2,label=f"t = {time:g}")
for ax,title in zip(axes,["Diffusion: constant total mass","Diffusion plus growth: mass proportional to t"]):
    ax.set(xlim=(-7,7),ylim=(0,1.6),xlabel="x",ylabel="Profile amplitude",title=title)
    ax.grid(alpha=0.2);ax.legend(fontsize=9)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
