"""Original explanatory diagram; Python 3.14, numpy and matplotlib (root pyproject)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Ellipse
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})

fig,ax=plt.subplots(figsize=(7.3,5))
for xy,wh,label,c in [((-1.8,2),(1.8,1.4),'ordinary\ncapacitors','#9ecae1'),((0,1.1),(1.7,1.5),'supercapacitors','#a1d99b'),((1.8,-.1),(1.7,1.7),'batteries','#fdae6b')]:
 ax.add_patch(Ellipse(xy,*wh,color=c,alpha=.75))
 ax.text(*xy,label,ha='center',va='center')
x=np.linspace(-3,3,300)
for b,label in [(2,'shorter discharge time'),(-1.7,'longer discharge time')]:
 ax.plot(x,x+b,color='0.45',ls='--',lw=.9)
 xt=-2.85 if b>0 else 0.45
 ax.text(xt,xt+b+.12,label,rotation=33,fontsize=9,color='.35')
ax.set(xlim=(-3,3),ylim=(-2,3.3),xticks=[],yticks=[],xlabel=r'Specific energy $E/m$  (increasing logarithmically $\rightarrow$)',ylabel=r'Specific power $P/m$ (logarithmic)',title='Qualitative Ragone regions; technology ranges overlap')
ax.text(0,-1.7,r'Constant-time lines: $P/m=(E/m)/t$',ha='center',fontsize=10)
fig.tight_layout()
fig.savefig("paper-1-ragone.png", dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
