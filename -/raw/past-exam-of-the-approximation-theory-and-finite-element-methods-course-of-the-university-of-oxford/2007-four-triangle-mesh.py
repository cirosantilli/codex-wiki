"""Generate 2007-four-triangle-mesh.png in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
pts=np.array([[0,2],[1,1],[2,0],[1,2],[2,1],[2,2]],float)
cells=[[0,1,3],[1,2,4],[1,3,4],[3,4,5]]
fig,ax=plt.subplots(figsize=(5.5,4.5),facecolor="white",layout="constrained")
ax.add_collection(PolyCollection([pts[c]for c in cells],facecolors=["#e9f3fa","#e9f3fa","#c8e3f2","#f1f1f1"],edgecolors="#52606d",lw=1.5))
ax.plot([0,2],[2,0],color="#197c4d",lw=3,label="Homogeneous Neumann")
ax.plot([0,2,2],[2,2,0],color="#b23c41",lw=3,label="Homogeneous Dirichlet")
offsets=[(-.13,.11),(-.35,-.25),(.05,-.05),(-.14,.12),(.08,0),(.05,.1)]
for i,(q,d)in enumerate(zip(pts,offsets)):
 ax.scatter(*q,color="#b23c41"if i!=1 else"#12679b",s=35,zorder=5)
 ax.text(*(q+d),f"{'ABCDEF'[i]} ({'1/4'if i==1 else'0'})",fontsize=11)
for cell,label in zip(cells,["$2-y$","$2-x$","$3-x-y$","$0$"]):
 q=pts[cell].mean(axis=0);ax.text(*q,label,ha="center",va="center",fontsize=12)
ax.set(xlim=(-.45,2.7),ylim=(-.35,2.45),aspect="equal",xlabel="$x$",ylabel="$y$",title=r"Nodal values of $u_h$; formulas for $\phi_B$")
ax.legend(loc="lower left",frameon=False,fontsize=9)
fig.savefig("2007-four-triangle-mesh.png",dpi=160,facecolor="white")
