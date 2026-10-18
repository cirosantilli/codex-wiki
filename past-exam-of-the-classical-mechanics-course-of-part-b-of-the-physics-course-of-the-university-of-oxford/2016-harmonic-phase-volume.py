"""Original plots; Python 3.14, numpy/matplotlib. Writes one PNG in the current working directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","savefig.facecolor":"white"})
def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white",transparent=False,metadata={"Software":"Matplotlib"})
    plt.close(fig)

from matplotlib.patches import Polygon
fig,axs=plt.subplots(1,2,figsize=(10,4.5),layout="constrained")
patch=np.array([[1.7,-.2],[2.3,-.2],[2.3,.2],[1.7,.2]])
theta=np.linspace(0,2*np.pi,500);axs[0].plot(2*np.cos(theta),2*np.sin(theta),"k--",alpha=.35,lw=1)
for angle,color,label in [(0,"#165b91","0"),(np.pi/2,"#bf5a13","pi / 2"),(np.pi,"#488523","pi"),(3*np.pi/2,"#8c4e9f","3 pi / 2")]:
    M=np.array([[np.cos(angle),np.sin(angle)],[-np.sin(angle),np.cos(angle)]])
    rotated=patch@M.T;axs[0].add_patch(Polygon(rotated,facecolor=color,alpha=.45,edgecolor=color,label="omega t = "+label))
axs[0].set(xlabel="Canonical X",ylabel="Canonical P",title="Rotation preserves every patch area",xlim=(-2.7,2.7),ylim=(-2.7,2.7),aspect="equal");axs[0].legend(loc="center",fontsize=8)
initial=np.array([[-.4,-.2],[.4,-.2],[.4,.2],[-.4,.2]])
squeezed=initial@np.diag([.4,2.5])
axs[1].add_patch(Polygon(initial,facecolor="#165b91",edgecolor="#165b91",alpha=.35,label="initial: area 0.32"))
axs[1].add_patch(Polygon(squeezed,facecolor="#bf5a13",edgecolor="#bf5a13",alpha=.35,label="squeezed: area 0.32"))
axs[1].set(xlabel="Position-like canonical coordinate",ylabel="Momentum-like canonical coordinate",title="Focusing trades width for divergence",xlim=(-.7,.7),ylim=(-.7,.7),aspect="equal");axs[1].legend(fontsize=8)
for ax in axs:ax.grid(alpha=.2)
save(fig)
