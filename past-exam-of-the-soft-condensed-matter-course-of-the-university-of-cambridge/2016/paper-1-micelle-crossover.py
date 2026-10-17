"""Original explanatory model; no exam image or experimental points copied.
Tested with Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7.
Writes its same-basename PNG to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})

q=50
ct=np.linspace(0,10,1000)
mon=np.zeros_like(ct)
for j,c in enumerate(ct):
    lo,hi=0.,max(1.,c)
    for _ in range(65):
        m=(lo+hi)/2
        if m+m**q>c:hi=m
        else:lo=m
    mon[j]=(lo+hi)/2
agg=ct-mon
fig,axes=plt.subplots(1,2,figsize=(8.6,3.5),constrained_layout=True)
axes[0].plot(ct,ct,":",color=".6",label="No association")
axes[0].plot(ct,mon,color="#2466a5",lw=2,label="Free monomers")
axes[0].plot(ct,agg,color="#ba492c",lw=2,label="In aggregates")
axes[0].set(xlim=(0,10),ylim=(0,10),xlabel=r"Total $c_{\rm tot}/c^\circ$",ylabel=r"Amphiphile amount / $c^\circ$")
axes[0].legend(fontsize=8)
axes[1].plot(ct[1:],agg[1:]/ct[1:],color="#347748",lw=2)
axes[1].set(xlim=(0,10),ylim=(0,1),xlabel=r"Total $c_{\rm tot}/c^\circ$",ylabel="Fraction of amphiphiles in aggregates")
for ax in axes:ax.grid(alpha=.18)
fig.suptitle(r"Illustrative mass action: $q=50$, $qK_q=1$ (chosen normalization)",fontsize=12)

fig.savefig(Path(__file__).stem + ".png", dpi=150, facecolor="white", bbox_inches="tight")
plt.close(fig)
