"""Schematic diffusive wall-layer and top-hat plume profiles.
Python 3.14; NumPy/Matplotlib. Output basename to caller CWD.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
x=np.array([0,1,3.5,4.6,5.3,6])
fig, axes=plt.subplots(1,2,figsize=(10,4),facecolor="white")
for ax, edge, variable, lower, upper, color in zip(axes,[0.90,0.95],["T","C"],["T_i","C_i"],[r"T_\infty",r"C_\infty"],["#b64c32","#2676a6"]):
    y=np.array([0,edge,edge,0.975,0.998,1])
    ax.set_facecolor("white")
    ax.axvspan(0,1,color="#c8dfe8",alpha=0.5)
    ax.axvspan(1,3.5,color="#f1eadb",alpha=0.7)
    ax.plot(x,y,color=color,lw=2.5)
    ax.axhline(1,color="#777777",ls=":",lw=1)
    ax.set_xlim(0,6)
    ax.set_ylim(-0.06,1.13)
    ax.set_yticks([0,1],labels=[rf"${lower}$",rf"${upper}$"])
    ax.set_xticks([0,1,3.5,6],labels=["Interface",r"$\delta$","Plume edge","Ocean"])
    ax.set_xlabel("Distance normal to the ice wall (schematic)")
    ax.set_title("Temperature" if variable=="T" else "Salinity")
    ax.text(0.5,0.15,"Laminar\nlayer",ha="center",fontsize=10)
    ax.text(2.25,0.36,"Mixed\nplume",ha="center",fontsize=10)
    ax.text(4.75,0.36,"Ambient\nocean",ha="center",fontsize=10)
    ax.text(2.2,edge-0.09,rf"${variable}$",fontsize=12,color=color)
fig.suptitle("Glacier-ablation profiles: most of each contrast lies across the wall layer")
fig.tight_layout()
fig.savefig("paper-72-plume-profiles.png",dpi=150,facecolor="white",transparent=False)
plt.close(fig)
