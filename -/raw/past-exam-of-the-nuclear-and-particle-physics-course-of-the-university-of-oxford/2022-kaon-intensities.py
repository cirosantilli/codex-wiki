"""Original solution figure; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Dependencies are declared in the repository pyproject.toml. The only output is
this script's PNG basename in the caller's current working directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def line(ax, a, b, kind="fermion", reverse=False, label=None):
    a,b=np.asarray(a,dtype=float),np.asarray(b,dtype=float)
    d=b-a; n=np.array([-d[1],d[0]])/np.linalg.norm(d)
    if kind in ("wave","gluon"):
        t=np.linspace(0,1,300)
        phase=14*np.pi*t
        z=a[:,None]+d[:,None]*t+0.048*n[:,None]*np.sin(phase)
        if kind=="gluon":
            z+=0.035*(d/np.linalg.norm(d))[:,None]*(np.cos(phase)-1)*np.sin(np.pi*t)
        ax.plot(*z,color="#23628a",lw=1.7)
    else:
        ax.plot([a[0],b[0]],[a[1],b[1]],color="#282e33",lw=1.6)
        if kind=="fermion":
            v,w=(b,a) if reverse else (a,b)
            ax.annotate("",xy=v+.61*(w-v),xytext=v+.43*(w-v),
                        arrowprops=dict(arrowstyle="-|>",color="#282e33",lw=1.25))
    if label:
        pos=(a+b)/2+.18*n
        ax.text(*pos,label,ha="center",va="center",fontsize=11,color="#164866",
                bbox=dict(facecolor="white",edgecolor="none",pad=.5))


def txt(ax,x,y,s,size=12,**kw):
    ax.text(x,y,s,ha="center",va="center",fontsize=size,**kw)


def setup(ax,xlim=(-.2,7.1),ylim=(-1,3.7)):
    ax.set_xlim(*xlim);ax.set_ylim(*ylim);ax.axis("off")


def dot(ax,*v):
    ax.plot(*v,"o",color="#282e33",ms=3)


def save(fig):
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,
                dpi=130,facecolor="white",transparent=False)
    plt.close(fig)


def main():
    x=np.linspace(0,10,1001)
    tau_s=8.958e-11;tau_l=5.18e-8;hbar=6.582119569e-22
    omega=3.49e-12*tau_s/hbar;r=tau_s/tau_l
    common=np.exp(-x)+np.exp(-r*x)
    interference=2*np.exp(-(1+r)*x/2)*np.cos(omega*x)
    fig,ax=plt.subplots(figsize=(8.0,4.8))
    ax.plot(x,(common+interference)/4,label=r"$I_{K^0}$",lw=2.4,color="#125c99")
    ax.plot(x,(common-interference)/4,label=r"$I_{\bar K^0}$",lw=2.4,color="#c45c23")
    ax.plot(x,np.exp(-r*x)/4,ls=":",color="#666666",lw=1.3,label=r"$e^{-t/\tau_L}/4$")
    cross=np.pi/(2*omega)
    ax.axvline(cross,color="#888888",ls="--",lw=.9)
    ax.annotate("First crossing\n$\\,t/\\tau_S=3.307$",xy=(cross,.255),xytext=(4.8,.65),
                arrowprops=dict(arrowstyle="->",color="#555555"),fontsize=11)
    ax.set(xlim=(0,10),ylim=(0,1.02),xlabel=r"Proper time $t/\tau_S$",ylabel="Intensity / initial intensity",
           title="Flavor oscillation and decay of an initially pure $K^0$ beam")
    ax.grid(alpha=.2);ax.legend(loc="upper right",frameon=False)
    fig.tight_layout();save(fig)

if __name__=="__main__":main()
