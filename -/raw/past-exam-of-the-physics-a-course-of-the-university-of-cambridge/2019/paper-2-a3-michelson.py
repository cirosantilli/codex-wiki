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
    fig, ax = plt.subplots(figsize=(7.7, 5.0), layout="constrained")
    def arrow(a,b,color="#0068a0"):
        ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"->","color":color,"lw":2})
    ax.plot([-0.33,0.33],[-0.33,0.33],color="#555555",lw=4)
    ax.plot([-0.6,0.6],[2.1,2.1],color="#555555",lw=5)
    ax.plot([3,3],[-0.6,0.6],color="#555555",lw=5)
    arrow((-2.7,0),(0,0));arrow((0,0),(3,0));arrow((0,0),(0,2.1))
    arrow((2.95,-0.11),(0,-0.11),"#b55713");arrow((-.11,2.05),(-.11,-1.9),"#b55713")
    arrow((0,-.1),(0,-1.9),"#b55713")
    ax.add_patch(plt.Rectangle((-.6,-2.18),1.2,.28,facecolor="#dddddd",edgecolor="#555555"))
    ax.text(-2.8,.28,"Selected spectral line\nand collimated input",fontsize=11)
    ax.text(.4,-.68,"Beam splitter",fontsize=11)
    ax.text(.55,1.5,"Fixed arm",fontsize=11)
    ax.text(1.1,.3,"Moving arm",fontsize=11)
    ax.text(-.65,2.38,"Fixed mirror",fontsize=11)
    ax.text(2.6,.75,"Moving mirror",fontsize=11)
    ax.annotate("",xy=(3.7,-.9),xytext=(2.9,-.9),arrowprops={"arrowstyle":"<->","color":"#555555"})
    ax.text(3.12,-1.26,r"$\Delta x$",fontsize=13)
    ax.text(-.75,-2.56,"Detector: count N fringes",fontsize=11)
    ax.text(-2.6,-1.45,"Round-trip path change:"+'\n'+r"$2\Delta x$; $\lambda=2\Delta x/N$",fontsize=12)
    ax.set(xlim=(-3,4.1),ylim=(-2.8,2.85),title="Michelson wavelength measurement")
    ax.set_aspect("equal");ax.axis("off")

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
