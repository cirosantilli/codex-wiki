"""Original parabola and quartic, with parameter direction and critical points."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,1200)
fig,axes=plt.subplots(1,2,figsize=(9.2,5.0),layout="constrained")
ax=axes[0];ax.plot(x,2*x*x,color="#267ba6",lw=2)
ax.fill_between(x,0,2*x*x,color="#267ba6",alpha=.14)
ax.text(0,.6,r"Area $=4/3$",ha="center",fontsize=12)
ax.scatter([-1,1],[2,2],facecolors="white",edgecolors="#267ba6",s=40,zorder=5)
ax.set(title=r"$y=1+\cos(2\theta)=2x^2$",ylim=(-.12,2.3))
ax=axes[1];ax.plot(x,8*x**4-8*x*x+1,color="#955586",lw=2)
ax.scatter([-1,1],[1,1],facecolors="white",edgecolors="#955586",s=40,zorder=5)
ax.scatter([0,-1/np.sqrt(2),1/np.sqrt(2)],[1,-1,-1],color="#9a492b",s=30,zorder=5,label="Interior extrema")
ax.scatter([-1/np.sqrt(6),1/np.sqrt(6)],[-1/9]*2,color="#267ba6",marker="D",s=29,zorder=5,label="Inflection points")
ax.annotate(r"$(0,1)$",(0,1),xytext=(0,1.24),ha="center",fontsize=10)
ax.text(0,-1.24,r"Minima: $(\pm1/\sqrt{2},-1)$",ha="center",fontsize=10)
ax.set(title=r"$y=\cos(4\theta)=8x^4-8x^2+1$",ylim=(-1.45,1.55))
ax.legend(loc="upper center",bbox_to_anchor=(.5,-.23),ncol=2,fontsize=9)
for ax in axes:
    ax.annotate("Increasing θ",xy=(-.65,ax.get_ylim()[1]-.18),xytext=(.68,ax.get_ylim()[1]-.18),arrowprops=dict(arrowstyle="->",color="#555555"),ha="center",fontsize=9)
    ax.axhline(0,color="#777777",lw=.7);ax.axvline(0,color="#777777",lw=.7)
    ax.set(xlim=(-1.12,1.12),xlabel="x = cos θ",ylabel="y");ax.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white")
plt.close(fig)
