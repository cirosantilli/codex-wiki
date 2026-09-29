"""Original induced-dipole illustration. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Writes an opaque basename PNG in the process current working directory.
No measured car parameters: weak-anomaly dipole profiles in arbitrary units.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def anomaly(x, direction, across=False):
    r = np.column_stack((np.zeros_like(x), x, -np.ones_like(x))) if across else np.column_stack((x, np.zeros_like(x), -np.ones_like(x)))
    rr = np.linalg.norm(r, axis=1)
    moment = np.asarray(direction, dtype=float)
    field = (3*r*(r@moment)[:, None]/rr[:, None]**2-moment)/rr[:, None]**3
    return field@moment

def main():
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-4, 4, 1201)
    fig, axes = plt.subplots(1, 3, figsize=(11, 4.3), layout="constrained")
    for ax, direction, title in zip(axes, [(0,0,1), (1,0,0), (0,0,-1)], ["North magnetic pole", "Magnetic equator", "South magnetic pole"]):
        y = anomaly(x, direction)
        ax.plot(x,y,lw=2.3,color="#225f89",label="north–south traverse")
        if title == "Magnetic equator":
            ax.plot(x,anomaly(x,direction,True),"--",color="#b4492a",label="east–west traverse")
            ax.legend(fontsize=8,loc="upper right")
        ax.axhline(0,color="0.4",lw=.7)
        ax.axvline(0,color="0.6",ls=":")
        ax.set(title=title,xlabel="Offset / burial depth",ylim=(-1.15,2.3),ylabel="Total-field anomaly / arbitrary unit")
        ax.text(0,.03,"car",transform=ax.get_xaxis_transform(),ha="center",fontsize=9)
    fig.suptitle("Induced moment parallel to local field; total-field projection, not a vertical-component reading",fontsize=11)
    fig.savefig(Path(__file__).with_suffix(".png").name,dpi=130,facecolor="white")

if __name__ == "__main__":
    main()
