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
    fig,ax=plt.subplots(figsize=(7.8,5),layout="constrained")
    for mirror in (0,2):ax.plot([mirror,mirror],[-.4,4.1],color="#777777",lw=5)
    def ray(a,b,color="#0068a0"):
        ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"->","lw":1.8,"color":color})
    ray((-1,-.35),(0,0))
    for j in range(3):
        y=1.4*j;ray((0,y),(2,y+.7));ray((2,y+.7),(3.1,y+1.085),"#b55713")
        ax.text(3.15,y+1.09,f"Beam {j+1}",fontsize=10,va="center",color="#b55713")
        if j<2:ray((2,y+.7),(0,y+1.4))
    direction=np.array([1.,.35]);direction/=np.linalg.norm(direction)
    first=np.array([2.,.7]);second=np.array([2.,2.1]);foot=first+np.dot(second-first,direction)*direction
    ax.plot([second[0],foot[0]],[second[1],foot[1]],ls="--",color="#555555",lw=1.5)
    ax.text(2.48,1.9,"Common outgoing\nwavefront",fontsize=9)
    ax.plot([0,.9],[0,0],ls=":",color="#777777")
    ax.text(.45,.06,r"$\theta$",fontsize=12)
    ax.annotate("",xy=(2,-.6),xytext=(0,-.6),arrowprops={"arrowstyle":"<->","color":"#555555"})
    ax.text(.95,-.88,r"$d$",fontsize=13)
    ax.text(.55,3.8,"Air gap",fontsize=11)
    ax.text(-.8,-1.15,r"Path difference on the same wavefront: $2d\cos\theta$",fontsize=12)
    ax.set(xlim=(-1.2,4),ylim=(-1.45,4.4),title="Multiple transmitted paths in an etalon")
    ax.set_aspect("equal");ax.axis("off")

    fig.savefig(Path(__file__).with_suffix(".png").name, dpi=150,
                facecolor="white", transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
