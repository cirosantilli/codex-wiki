"""Original Fourier solution of cooling from a triangular tent; output to cwd."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

u=np.linspace(0,1,1101)
x=np.pi*u
fig,ax=plt.subplots(figsize=(6.8,4.0),layout="constrained")
ax.plot(u,2*np.minimum(u,1-u),color="#333333",lw=2,label=r"$\tau=0$ (initial)")
for time,color in [(0.03,"#b45028"),(0.15,"#29709e"),(0.5,"#568c42")]:
    profile=np.zeros_like(x)
    for n in range(1,251,2):
        profile+=8/np.pi**2*np.sin(n*np.pi/2)/n**2*np.exp(-n*n*time)*np.sin(n*x)
    ax.plot(u,profile,color=color,lw=2,label=rf"$\tau={time:g}$")
ax.set(xlim=(0,1),ylim=(-0.02,1.06),xlabel=r"Position $x/\pi$",ylabel=r"Temperature $T/(\pi/2)$",title="A corner is smoothed as heat escapes through the ends")
ax.grid(alpha=0.2);ax.legend(fontsize=10)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
