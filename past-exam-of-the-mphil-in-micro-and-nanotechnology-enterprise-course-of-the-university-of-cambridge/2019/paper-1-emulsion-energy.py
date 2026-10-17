"""Original explanatory diagram; Python 3.14, numpy and matplotlib (root pyproject)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Ellipse
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})

c=np.logspace(-3,2,500)
e=.36+.64*np.clip(-np.log10(c)/3,0,1)
fig,ax=plt.subplots(figsize=(7.2,4.4));ax.semilogx(c,e,lw=2.4,color='#2171b5')
ax.axvline(1,ls='--',color='.45',lw=1);ax.text(1.2,.85,'illustrative CMC')
ax.set(xlabel='Amphiphile concentration / illustrative CMC',ylabel='Surface energy / initial surface energy',ylim=(.27,1.05),title='Adsorption lowers interfacial energy at fixed droplet area')
ax.text(.002,.43,'Initial adsorption',fontsize=10);ax.annotate('near-saturation plateau',xy=(30,.362),xytext=(.02,.61),arrowprops={'arrowstyle':'->'},fontsize=10)
fig.tight_layout()
fig.savefig("paper-1-emulsion-energy.png", dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
