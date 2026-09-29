"""Original explanatory diagram; Python 3.14, numpy and matplotlib (root pyproject)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Ellipse
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})

h=np.linspace(.075,14,2200)
fig,ax=plt.subplots(figsize=(8,4.7))
rep=7*.11**11/12
for k,label,color in [(.65,'low salt: high barrier','#2171b5'),(1.4,'more salt: lower barrier','#e6550d'),(3.,'high salt: no barrier','#a50f15')]:
 u=rep/h**12+45*np.exp(-k*h)-7/h
 ax.plot(h,u,lw=2,label=label,color=color)
ax.axhline(0,color='.5',lw=.8)
ax.annotate('primary attractive well\n(molecular cutoff model)',xy=(.12,-17),xytext=(1.1,-14),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.annotate('weak secondary minimum',xy=(9.7,-.64),xytext=(7,8),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(xlim=(0,14),ylim=(-20,30),xlabel='Surface gap (arbitrary length units)',ylabel=r'Interaction energy / $k_BT$',title='Illustrative pair interactions; not a fit to a particular dispersion')
ax.legend(loc='upper right',fontsize=9)
fig.tight_layout()
fig.savefig("paper-1-colloid-potentials.png", dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
