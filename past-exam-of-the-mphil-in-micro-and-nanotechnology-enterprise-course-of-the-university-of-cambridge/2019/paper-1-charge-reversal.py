"""Original explanatory diagram; Python 3.14, numpy and matplotlib (root pyproject)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Ellipse
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.spines.top": False, "axes.spines.right": False})

x=np.linspace(0,8,600)
y=np.where(x<=1,120-190*x,-70*np.exp(-.75*(x-1)))
fig,ax=plt.subplots(figsize=(7.7,4.7));ax.plot(x,y,lw=2.3,color='#2171b5');ax.axhline(0,color='.45',lw=.8);ax.axvline(1,color='.5',ls='--',lw=1)
ax.axvspan(0,1,color='#fdd0a2',alpha=.45)
ax.text(.5,105,'compact\nlayer',ha='center',fontsize=10);ax.text(3,50,'diffuse layer: approaches zero from below',fontsize=10)
ax.annotate('negative potential after\nphosphate overcompensation',xy=(1,-70),xytext=(2,-100),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(xlabel='Distance from surface (schematic units)',ylabel='Potential (mV)',xticks=[0,1],xticklabels=['0',r'$d_S$'],ylim=(-115,140),title='Interfacial charge reversal; far-field screening is a separate process')
fig.tight_layout()
fig.savefig("paper-1-charge-reversal.png", dpi=170, bbox_inches="tight", facecolor="white")
plt.close(fig)
