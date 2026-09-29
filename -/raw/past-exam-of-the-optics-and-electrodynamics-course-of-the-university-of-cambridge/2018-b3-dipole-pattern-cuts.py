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
    angle=np.linspace(0,2*np.pi,1001)
    fig,(xz,xy)=plt.subplots(1,2,figsize=(9,4.9),subplot_kw={"projection":"polar"})
    xz.set_theta_zero_location("N");xz.set_theta_direction(-1)
    xz.plot(angle,np.sin(angle)**2,color="#0068a0",lw=2.3)
    xz.fill(angle,np.sin(angle)**2,color="#0068a0",alpha=.1)
    xz.set_thetagrids([0,90,180,270],["+z","+x","−z","−x"])
    xz.set_title(r"xz cut: $\sin^2\theta$",pad=24,fontsize=13)
    xy.set_theta_zero_location("E")
    xy.plot(angle,np.ones_like(angle),color="#b55713",lw=2.3)
    xy.fill(angle,np.ones_like(angle),color="#b55713",alpha=.08)
    xy.set_thetagrids([0,90,180,270],["+x","+y","−x","−y"])
    xy.set_title("xy cut: constant in azimuth",pad=24,fontsize=13)
    for ax in (xz,xy):
        ax.set_ylim(0,1.08);ax.set_yticks([.5,1]);ax.set_rlabel_position(35);ax.grid(alpha=.25)
    fig.text(.5,.06,"Radius is normalized time-averaged power per solid angle, not field amplitude.\nThe z-directed receiving dipole selects z-polarized light incident along x.",ha="center",fontsize=10)
    fig.subplots_adjust(left=.055,right=.945,bottom=.2,top=.8,wspace=.35)

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
