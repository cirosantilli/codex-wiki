"""Original mathematical illustration; write the PNG basename to the cwd.

Tested with Python 3.14.4, NumPy 2.3.5 and Matplotlib 3.10.7.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig,axes=plt.subplots(1,2,figsize=(10,4.7),layout="constrained",facecolor="white")
    coord=np.linspace(0,np.pi,501)
    X,Y=np.meshgrid(coord,coord)
    for ax,(m,n) in zip(axes,[(3,4),(4,3)]):
        values=np.sin(m*X)*np.sin(n*Y)
        im=ax.imshow(values,extent=(0,np.pi,0,np.pi),origin="lower",cmap="RdBu_r",vmin=-1,vmax=1,interpolation="bilinear")
        for j in range(1,m):ax.axvline(j*np.pi/m,color="white",ls="--",lw=.8)
        for j in range(1,n):ax.axhline(j*np.pi/n,color="white",ls="--",lw=.8)
        ax.set_xticks([0,np.pi/2,np.pi],["0",r"$\pi/2$",r"$\pi$"])
        ax.set_yticks([0,np.pi/2,np.pi],["0",r"$\pi/2$",r"$\pi$"])
        ax.set(xlabel="$x$",ylabel="$y$",title=rf"$\sin({m}x)\sin({n}y)$")
    fig.colorbar(im,ax=axes,shrink=.82,label="Mode value")
    fig.suptitle(r"Two independent modes with $-\Delta u=25u$")
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=160,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
