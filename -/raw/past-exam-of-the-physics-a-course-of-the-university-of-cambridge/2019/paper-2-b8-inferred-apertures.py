"""Original solution figure; tested with Python 3.14.

Uses NumPy and Matplotlib as declared in the root pyproject.toml.
Writes its PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    w=2*np.pi/5;h=2*np.pi;s=2*np.pi/2.5
    fig,ax=plt.subplots(figsize=(6.8,6.3),layout="constrained")
    ax.add_patch(plt.Rectangle((-2.6,-4.1),5.2,8.2,facecolor="#e7e7e7",edgecolor="none"))
    for center in (-s/2,s/2):
        ax.add_patch(plt.Rectangle((center-w/2,-h/2),w,h,facecolor="white",edgecolor="#555555",lw=1.5))
        ax.plot([center,center],[-h/2-.1,h/2+.1],ls=":",color="#999999",lw=.8)
    def dimension(a,b,text,position):
        ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"<->","color":"#0068a0"})
        ax.text(*position,text,ha="center",va="center",fontsize=11,color="#0068a0")
    dimension((-s/2,h/2+.48),(s/2,h/2+.48),"Centre spacing 2.51 μm",(0,h/2+.8))
    dimension((s/2-w/2,-h/2-.35),(s/2+w/2,-h/2-.35),"Width 1.26 μm",(s/2,-h/2-.7))
    dimension((s/2+w/2+.42,-h/2),(s/2+w/2+.42,h/2),"",(0,0))
    ax.text(s/2+w/2+.65,0,"Height 6.28 μm",rotation=90,ha="center",va="center",fontsize=11,color="#0068a0")
    ax.text(0,0,"Gap\n1.26 μm",ha="center",va="center",fontsize=10)
    ax.set(xlim=(-3.1,3.1),ylim=(-4.4,4.4),xlabel="x (μm)",ylabel="y (μm)",
           title="Inferred aperture geometry: centred representative")
    ax.set_aspect("equal");ax.set_xticks([-2,0,2]);ax.set_yticks([-3,0,3])

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
