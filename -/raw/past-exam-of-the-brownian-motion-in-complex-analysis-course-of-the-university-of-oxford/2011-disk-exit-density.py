"""Oxford C10.1b 2011: original visualization of disk harmonic measure.

Writes 2011-disk-exit-density.png in the process CWD, white background.
Tested: Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Dependencies: repository root pyproject.toml.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import Normalize
import numpy as np


def main():
    w=.6+.25j
    theta=np.linspace(0,2*np.pi,1201)
    points=np.column_stack([np.cos(theta),np.sin(theta)])
    density=(1-abs(w)**2)/(2*np.pi*abs(np.exp(1j*theta)-w)**2)
    segments=np.stack([points[:-1],points[1:]],axis=1)
    fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.3),facecolor="white",gridspec_kw={"width_ratios":[1,1.35]})
    curve=LineCollection(segments,cmap="Blues",norm=Normalize(vmin=0,vmax=density.max()),linewidths=7)
    curve.set_array((density[:-1]+density[1:])/2)
    ax.add_collection(curve)
    ax.scatter([0],[0],color="#8c969c",s=18)
    ax.scatter([w.real],[w.imag],color="#bd5b21",s=55,zorder=3)
    ax.annotate(r"$w=0.6+0.25i$",(w.real,w.imag),xytext=(-.15,.68),fontsize=11,arrowprops={"arrowstyle":"->","color":"#bd5b21"})
    ax.set(xlim=(-1.18,1.18),ylim=(-1.18,1.18),xlabel=r"$\mathrm{Re}\,z$",ylabel=r"$\mathrm{Im}\,z$")
    ax.set_aspect("equal")
    ax.set_title("Exit density around the unit circle")
    ax.spines[["top","right"]].set_visible(False)
    bx.plot(theta,density,color="#176b97",lw=2,label="Start at w")
    bx.axhline(1/(2*np.pi),color="#7d858a",ls="--",label="Start at 0")
    bx.axvline(np.angle(w),color="#bd5b21",ls=":",lw=1.2)
    bx.set(xlim=(0,2*np.pi),ylim=(0,density.max()*1.1),xlabel=r"Exit angle $\theta$",ylabel=r"Density $h(\theta)$")
    bx.set_xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],["0",r"$\pi/2$",r"$\pi$",r"$3\pi/2$",r"$2\pi$"])
    bx.set_title(r"$h(\theta)=\frac{1-|w|^2}{2\pi|e^{i\theta}-w|^2}$")
    bx.spines[["top","right"]].set_visible(False)
    bx.grid(alpha=.15)
    bx.legend(frameon=False)
    fig.tight_layout(w_pad=3)
    fig.savefig("2011-disk-exit-density.png",dpi=150,facecolor="white")
    plt.close(fig)


if __name__=="__main__":main()
