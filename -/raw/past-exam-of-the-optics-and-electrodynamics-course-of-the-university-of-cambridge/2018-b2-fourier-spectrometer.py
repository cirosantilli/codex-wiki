"""Original solution figure; tested with Python 3.14.

Uses the NumPy and Matplotlib dependencies in the root pyproject.toml.
Writes the PNG basename to the current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,ax=plt.subplots(figsize=(9,5),layout="constrained")
    def arrow(a,b,color="#0068a0"):
        ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"->","color":color,"lw":1.8})
    ax.plot([-.3,.3],[-.3,.3],lw=4,color="#555555")
    ax.plot([-.5,.5],[2,2],lw=5,color="#555555")
    ax.plot([2.5,2.5],[-.5,.5],lw=5,color="#555555")
    arrow((-2.3,0),(0,0));arrow((0,0),(2.5,0));arrow((0,0),(0,2))
    arrow((2.45,-.12),(0,-.12),"#b55713");arrow((-.12,1.95),(-.12,-1.8),"#b55713")
    arrow((0,-.12),(0,-1.8),"#b55713")
    ax.text(-2.4,.3,"Broadband input",fontsize=11)
    ax.text(-.65,2.3,"Fixed mirror",fontsize=11)
    ax.text(.3,-.6,"Non-polarizing\nbeam splitter",fontsize=10)
    ax.text(2.1,.7,"Scanning mirror",fontsize=11)
    ax.annotate("",xy=(3.3,-.75),xytext=(2.35,-.75),arrowprops={"arrowstyle":"<->","color":"#555555"})
    ax.text(2.8,-1.12,"x",fontsize=12)
    ax.add_patch(plt.Rectangle((-.55,-2.1),1.1,.3,facecolor="#dddddd",edgecolor="#555555"))
    ax.text(-1.2,-2.45,"Detector: I(x)",fontsize=11)
    ax.text(-2.4,-1.18,r"$D=2x$"+'\n'+r"$\tau=2x/c$",fontsize=12)
    arrow((.6,-1.95),(2.15,-1.95),"#555555")
    ax.add_patch(plt.Rectangle((2.2,-2.3),1.8,.7,facecolor="#edf4f8",edgecolor="#555555"))
    ax.text(3.1,-1.95,"Background\nsubtraction + FFT",fontsize=10,ha="center",va="center")
    arrow((4.05,-1.95),(4.7,-1.95),"#555555")
    ax.text(4.8,-1.95,"Spectrum",fontsize=11,va="center")
    ax.text(3.3,1.2,"Record signal and\ncalibrated mirror position",fontsize=10)
    ax.set(xlim=(-2.65,5.9),ylim=(-2.7,2.65),title="Fourier transform spectroscopy with a scanned Michelson")
    ax.set_aspect("equal");ax.axis("off")

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
