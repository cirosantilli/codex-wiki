"""Original two-variable dual feasible region. Python3.14, NumPy, Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
u=np.linspace(-.3,4.4,600)
lines=[.5-.25*u,2-3*u,3-4*u,1-.4*u];env=np.maximum.reduce(lines)
fig,ax=plt.subplots(figsize=(7,5),facecolor="white")
ax.fill_between(u,env,4.4,color="#e1f2ee",label="dual feasible region")
for v,label in zip(lines,[r"$2u+8v=4$",r"$3u+v=2$",r"$4u+v=3$",r"$2u+5v=5$"]):
 ax.plot(u,v,lw=1,ls="--",label=label)
ax.plot(u,env,color="#176858",lw=2.5)
ax.plot(u,4/3-u,color="#b2182b",lw=1.8,label=r"$u+v=4/3$")
ax.scatter([5/9,10/3],[7/9,-1/3],color="#b2182b",zorder=5)
ax.annotate(r"optimum $(5/9,7/9)$",(5/9,7/9),(1,1.3),arrowprops=dict(arrowstyle="->"),fontsize=11)
ax.annotate(r"$(10/3,-1/3)$",(10/3,-1/3),(2.3,-.9),arrowprops=dict(arrowstyle="->"),fontsize=11)
ax.axhline(0,color=".6",lw=.7);ax.axvline(0,color=".6",lw=.7)
ax.set(xlim=(-.3,4.4),ylim=(-1.2,4.4),xlabel="u",ylabel="v",
       title="Free dual variables; minimum objective value 400")
ax.spines[["top","right"]].set_visible(False);ax.legend(loc="upper right",fontsize=8)
fig.tight_layout();fig.savefig("2007-dual-envelope.png",dpi=150,facecolor="white")
