"""Original exam-solution illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    t=np.linspace(-1.65,1.65,700)
    fig,ax=plt.subplots(figsize=(5.8,5),layout="constrained",facecolor="white")
    ax.plot(t*t,t**3,color="#17648e",lw=2.5)
    ax.axhline(0,color=".6",lw=.8);ax.axvline(0,color=".6",lw=.8)
    ax.scatter([0],[0],s=30,color="#b84732",zorder=5)
    ax.annotate("Cusp (0, 0)",(0,0),xytext=(.75,.55),arrowprops={"arrowstyle":"->","color":"#b84732"},fontsize=10)
    ax.text(2,3.5,r"$y=x^{3/2}$",color="#17648e")
    ax.text(1.75,-3.75,r"$y=-x^{3/2}$",color="#17648e")
    ax.set(xlim=(-.35,3.0),ylim=(-4.7,4.7),xlabel="$x$",ylabel="$y$",title=r"$y^2=x^3$, $x\geq0$")
    ax.grid(alpha=.14)
    fig.savefig(Path("paper-1-semicubical-parabola.png"),dpi=160,facecolor="white");plt.close(fig)


if __name__ == "__main__":
    main()
