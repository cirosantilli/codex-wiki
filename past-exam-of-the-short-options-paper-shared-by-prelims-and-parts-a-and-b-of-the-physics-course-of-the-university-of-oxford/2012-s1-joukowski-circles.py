"""Original circle/ellipse geometry for 2012 Short Options S1; PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "axes.facecolor": "white"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), layout="constrained")
    th = np.linspace(0, 2*np.pi, 1201)
    for r, color, style in [(.5, "#D55E00", "--"), (1, "#009E73", "-"), (2, "#0072B2", "-")]:
        zz = r*np.exp(1j*th);ww = zz+1/zz
        axes[0].plot(zz.real, zz.imag, color=color, linestyle=style, label=rf"$\rho={r:g}$")
        axes[1].plot(ww.real, ww.imag, color=color, linestyle=style, label=rf"$\rho={r:g}$")
        a = .7 if r >= 1 else 3.8
        z0 = r*np.exp(1j*a);z1 = r*np.exp(1j*(a+.18))
        w0=z0+1/z0;w1=z1+1/z1
        axes[0].annotate("",(z1.real,z1.imag),(z0.real,z0.imag),arrowprops={"arrowstyle":"->","color":color,"lw":2})
        if r!=1:axes[1].annotate("",(w1.real,w1.imag),(w0.real,w0.imag),arrowprops={"arrowstyle":"->","color":color,"lw":2})
    axes[1].scatter([-2,2],[0,0],color="black",s=25,zorder=5)
    axes[1].annotate("foci",(2,0),(.7,-.6),arrowprops={"arrowstyle":"->"},fontsize=10)
    for ax,title in zip(axes,["Source circles (positive traversal)","Images: reciprocal radii, one ellipse"]):
        ax.set(xlabel="real part",ylabel="imaginary part",title=title,xlim=(-2.8,2.8),ylim=(-2.3,2.3));ax.set_aspect("equal");ax.grid(alpha=.2);ax.legend(fontsize=10,loc="upper left")
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white");plt.close(fig)


if __name__=="__main__":main()
