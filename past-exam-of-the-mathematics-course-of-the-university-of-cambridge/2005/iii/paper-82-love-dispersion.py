"""Original Love-wave dispersion/profile figure; Python 3.14.4.
Existing NumPy 2.3.5/Matplotlib 3.10.7; basename PNG output to caller CWD.
Honor caller MPLCONFIGDIR; no publication or media-mirroring logic.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

BETA = 1.8
MODULUS_RATIO = BETA**2  # Equal densities, layer shear speed normalized to one.


def root(omega_scale, order):
    lo = order*np.pi
    hi = min(omega_scale, (order+.5)*np.pi)
    if omega_scale <= lo:
        return None
    hi -= 1e-11
    for _ in range(80):
        mid = (lo+hi)/2
        residual = mid*np.tan(mid)-MODULUS_RATIO*np.sqrt(max(0,omega_scale**2-mid**2))
        if residual > 0:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def main():
    fig, (ax, profile) = plt.subplots(1, 2, figsize=(10.8,4.7), dpi=100, facecolor="white", gridspec_kw={"width_ratios":[1.5,1]})
    fig.subplots_adjust(left=.075,right=.96,bottom=.18,top=.86,wspace=.30)
    contrast = np.sqrt(1-BETA**-2)
    colors=["#286b93","#b2602c","#488148","#85569a"]
    for order,color in enumerate(colors):
        scales = np.linspace(order*np.pi+.018,4.4*np.pi,450)
        qh = np.array([root(x,order) for x in scales])
        speed = 1/np.sqrt(1-(qh/scales)**2*contrast**2)
        ax.plot(scales/np.pi,speed,color=color,lw=2,label="Fundamental" if order==0 else f"Overtone {order}")
        ax.plot(order,BETA,"o",mfc="white",mec=color,ms=6)
    ax.axhline(1,color="#777777",ls=":",lw=1)
    ax.set(xlim=(0,4.4),ylim=(.98,1.86),xlabel=r"$\Omega/\pi=|\omega|h\sqrt{\beta_0^{-2}-\beta^{-2}}/\pi$",ylabel=r"Phase speed $c_L/\beta_0$",title="Trapped modes lie strictly below the cutoff speed")
    ax.legend(frameon=False,fontsize=9)
    ax.spines[["top","right"]].set_visible(False)
    scale = 2*np.pi
    q = root(scale,1)
    p = np.sqrt(scale*scale-q*q)
    depth=np.linspace(0,2.2,500)
    amplitude=np.where(depth<=1,np.cos(q*depth),np.cos(q)*np.exp(-p*(depth-1)))
    profile.axhspan(0,1,color="#edf1f7")
    profile.axhline(1,color="#888888",lw=1)
    profile.axvline(0,color="#999999",lw=.8)
    profile.plot(amplitude,depth,color=colors[1],lw=2)
    profile.set(xlim=(-1.15,1.15),ylim=(2.2,-.06),xlabel="Normalized SH displacement",ylabel=r"Depth $z/h$",title=r"Overtone 1 at $\Omega=2\pi$")
    profile.text(-1.07,.11,"Free surface",fontsize=9)
    profile.text(.10,1.08,"Half-space: exponential tail",fontsize=9)
    profile.spines[["top","right"]].set_visible(False)
    fig.text(.5,.035,r"$\beta/\beta_0=1.8$, equal densities; hollow endpoints have zero decay exponent and are not trapped modes.",ha="center",fontsize=10)
    fig.savefig(Path.cwd()/"paper-82-love-dispersion.png",facecolor="white",transparent=False)
    plt.close(fig)


if __name__ == "__main__":
    main()
