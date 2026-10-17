"""Original explanatory figure; Python 3.14 and root pyproject dependencies."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,"figure.facecolor":"white","axes.facecolor":"white"})

fig,ax=plt.subplots(figsize=(7,4),layout="constrained")
r=np.linspace(1,3,100);u=(3-r)/2
ax.plot(r,u,color="#1565c0",lw=2)
for x,y,label in [(1,1,"Inner contact: axle speed"),(2,.5,"Ball centre: translation"),(3,0,"Outer contact: casing fixed")]:
 ax.scatter([x],[y],color="#d84315",zorder=4);ax.annotate(label,(x,y),xytext=(8,12 if x<3 else 18),textcoords="offset points",ha="left" if x<3 else "right",fontsize=9)
ax.axvline(2,color="#aaa",ls=":");ax.axhline(0,color="#aaa",lw=.7)
ax.text(1.05,.12,r"Spin: $\Omega=-\omega/2$",color="#1565c0")
ax.set(xlim=(.85,3.25),ylim=(-.08,1.22),xlabel="Distance from axle axis / a",ylabel=r"Tangential velocity / $(a\omega)$",title="No-slip matching across one ball's diameter")
ax.grid(alpha=.18)

fig.savefig(Path(__file__).stem+".png",dpi=150,facecolor="white",bbox_inches="tight")
plt.close(fig)
