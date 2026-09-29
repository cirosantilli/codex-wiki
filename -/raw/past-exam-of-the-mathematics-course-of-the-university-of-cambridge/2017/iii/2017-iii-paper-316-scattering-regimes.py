"""Original conditional scattering map; output an opaque PNG in the current directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from pathlib import Path

def main():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=100, facecolor="white")
    x = np.geomspace(.01, 100, 600); y = np.geomspace(.001, 1000, 600)
    X,Y = np.meshgrid(x,y)
    strong = Y > X**(-1.5); fast = Y > X**(.75)
    region = 2*strong.astype(int)+fast.astype(int)
    ax.pcolormesh(X,Y,region,cmap=ListedColormap(["#eeeeee","#ffedd5","#dbeafe","#dcfce7"]),
                  vmin=-.5,vmax=3.5,shading="auto",rasterized=True)
    ax.plot(x,x**(-1.5),color="#7c3a13",lw=2,label=r"Escape-speed boundary: $\chi=1$")
    ax.plot(x,x**(.75),color="#175485",lw=2,ls="--",label=r"Diffusion-age boundary: $t_{\rm ej}=t_\star$")
    ax.scatter([1],[1],s=35,color="#202020",zorder=5)
    box=dict(facecolor="white",edgecolor="none",alpha=.9,pad=4)
    ax.text(.02,8,"Weak kicks, short diffusion clock\nCollision / accretion favoured",fontsize=10,bbox=box)
    ax.text(2.7,170,"Strong kicks, short diffusion clock\nEjection favoured",fontsize=10,bbox=box)
    ax.text(.018,.015,"Weak kicks, long diffusion clock\nEjection diffusion incomplete",fontsize=10,bbox=box)
    ax.text(2.7,.055,"Strong kicks, long diffusion clock\nEjection diffusion incomplete",fontsize=10,bbox=box)
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(.01,100); ax.set_ylim(.001,1000)
    ax.set_xlabel(r"Planetary orbital radius $a_p/a_{\rm cross}$")
    ax.set_ylabel(r"Planetary mass $M_p/M_{\rm cross}$")
    ax.set_title("Conditional planetary scattering outcomes",fontsize=14)
    ax.legend(loc="lower right",fontsize=9,framealpha=.96)
    ax.grid(which="major",alpha=.18)
    fig.text(.5,.025,r"Fixed $M_\star,\rho_p,t_\star$ and $a_0=a_p$; collision rates and correlated encounters need additional information.",
             ha="center",fontsize=9)
    fig.subplots_adjust(left=.10,right=.98,bottom=.17,top=.90)
    fig.savefig(Path.cwd()/"2017-iii-paper-316-scattering-regimes.png",dpi=100,facecolor="white",transparent=False)
    plt.close(fig)

if __name__ == "__main__":
    main()
