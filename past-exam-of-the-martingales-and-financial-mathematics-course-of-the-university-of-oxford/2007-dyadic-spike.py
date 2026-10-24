"""Original dyadic martingale illustration. Python3.14, NumPy, Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,3,figsize=(10,3.5),facecolor="white")
for ax,n in zip(axes,[1,2,4]):
 left=.5-2**(-n);height=2**n
 ax.fill_between([left,.5],0,height,color="#d8e9f5")
 ax.plot([0,left],[0,0],color="#2166ac",lw=2)
 ax.plot([left,left,.5,.5],[0,height,height,0],color="#2166ac",lw=2)
 ax.plot([.5,1],[0,0],color="#2166ac",lw=2)
 ax.scatter([left],[height],facecolors="white",edgecolors="#2166ac",s=35,zorder=4)
 ax.scatter([.5],[height],color="#2166ac",s=35,zorder=4)
 ax.set(xlim=(0,1),ylim=(-.2,height*1.2),xlabel=r"$\omega$",title=f"n={n}; area = 1",xticks=[0,.5,1])
 ax.spines[["top","right"]].set_visible(False)
fig.suptitle("A dyadic spike shrinks toward one null point",fontsize=14)
fig.tight_layout();fig.savefig("2007-dyadic-spike.png",dpi=150,facecolor="white")
