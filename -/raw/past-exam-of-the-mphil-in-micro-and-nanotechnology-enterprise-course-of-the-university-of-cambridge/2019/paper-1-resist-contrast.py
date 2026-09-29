"""Original explanatory diagram; Python 3.14, numpy and matplotlib (root pyproject)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Ellipse
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})

x=np.linspace(-1.1,.15,600)
fig,ax=plt.subplots(figsize=(7.3,4.5))
for gamma,color in [(1.33,'#e6550d'),(5.66,'#2171b5')]:
 y=np.clip(-gamma*x,0,1)
 ax.plot(x,y,lw=2.3,color=color,label=rf'$\gamma={gamma}$; width $1/\gamma={1/gamma:.3f}$ decades')
 ax.axvline(-1/gamma,color=color,ls=':',lw=1)
ax.axvline(0,color='0.45',ls='--',lw=1)
ax.set(xlabel=r'$\log_{10}(D/D_c)$',ylabel='Remaining thickness / initial thickness',ylim=(-.06,1.08),title='Positive resists at a common illustrative clearing dose')
ax.legend(loc='lower left',fontsize=10)
fig.tight_layout()
fig.savefig("paper-1-resist-contrast.png", dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
