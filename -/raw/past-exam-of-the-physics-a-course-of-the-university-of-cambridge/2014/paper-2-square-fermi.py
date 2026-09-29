"""Original square Brillouin-zone filling diagrams."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle
fig,axes=plt.subplots(1,3,figsize=(10,3.8),layout="constrained")
for ax in axes:
    ax.set_aspect("equal");ax.set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),xlabel=r"$k_xa/\pi$",ylabel=r"$k_ya/\pi$",xticks=[-1,0,1],yticks=[-1,0,1])
    ax.axhline(0,color=".8",lw=.6);ax.axvline(0,color=".8",lw=.6)
axes[0].add_patch(Circle((0,0),np.sqrt(2*np.pi)/np.pi,facecolor="#c6dfea",edgecolor="#245d84",lw=2))
axes[1].add_patch(Circle((0,0),np.sqrt(4*np.pi)/np.pi,facecolor="#c6dfea",edgecolor="#245d84",lw=2))
axes[2].add_patch(Rectangle((-1,-1),2,2,facecolor="#d8e7cc",edgecolor="none"))
for ax in axes:ax.add_patch(Rectangle((-1,-1),2,2,fill=False,edgecolor=".2",lw=1.8))
axes[0].set_title("Monovalent: half-filled band\nNo band insulator in this model",fontsize=10)
axes[1].set_title("Divalent free gas: circle crosses zone\nEqual area does not imply a gap",fontsize=10)
axes[2].set_title("Divalent insulator: full first band\nNo Fermi contour; global gap needed",fontsize=10)
fig.suptitle("One atom per primitive cell; spin degeneracy two")
fig.savefig("paper-2-square-fermi.png",dpi=150,facecolor="white")
