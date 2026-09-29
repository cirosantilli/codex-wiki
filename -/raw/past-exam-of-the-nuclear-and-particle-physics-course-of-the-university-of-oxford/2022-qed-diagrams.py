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
    fig,axes=plt.subplots(3,2,figsize=(10,9.2))
    for col,ax in enumerate(axes[0]):
        a,b=(2,1),(4,1)
        line(ax,(.65,1),a);line(ax,a,b,label=r"$e^{-*}$");line(ax,b,(5.35,1))
        incoming,outgoing=(a,b) if col==0 else (b,a)
        line(ax,(.65,2.85),incoming,"wave");line(ax,outgoing,(5.35,2.85),"wave")
        for x,y,s in [(.25,1,r"$e^-$"),(5.75,1,r"$e^-$"),(.3,3.05,r"$\gamma$"),(5.7,3.05,r"$\gamma$")]:txt(ax,x,y,s,11)
        ax.set_title("Compton: "+("$s$ channel" if col==0 else "$u$ channel"),fontsize=12)
        setup(ax,xlim=(-.15,6.2),ylim=(-.7,3.55))
    for col,ax in enumerate(axes[1]):
        a,b=(2.1,2),(3.9,2)
        emission,scatter=(a,b) if col==0 else (b,a)
        line(ax,(.65,2),a);line(ax,a,b);line(ax,b,(5.35,2))
        line(ax,emission,(5.35,3.3),"wave")
        line(ax,scatter,(3,.0),"wave",label=r"$\gamma^*$")
        line(ax,(.65,0),(3,0),"plain");line(ax,(3,0),(5.35,0),"plain")
        for x,y,s in [(.25,2,r"$e^-$"),(5.75,2,r"$e^-$"),(5.7,3.35,r"$\gamma$"),(.25,0,r"$Z$"),(5.75,0,r"$Z$")]:txt(ax,x,y,s,11)
        ax.set_title("Bremsstrahlung: "+("emit before" if col==0 else "emit after"),fontsize=12)
        setup(ax,xlim=(-.15,6.2),ylim=(-.65,3.85))
    for col,ax in enumerate(axes[2]):
        a,b=(2.1,2),(3.9,2)
        real,virtual=(a,b) if col==0 else (b,a)
        line(ax,(.65,1.25),a);line(ax,a,b);line(ax,b,(5.35,1.25))
        line(ax,(.65,3.35),real,"wave")
        line(ax,virtual,(3,0),"wave",label=r"$\gamma^*$")
        line(ax,(.65,0),(3,0),"plain");line(ax,(3,0),(5.35,0),"plain")
        for x,y,s in [(.25,1.25,r"$e^+$"),(5.75,1.25,r"$e^-$"),(.3,3.45,r"$\gamma$"),(.25,0,r"$Z$"),(5.75,0,r"$Z$")]:txt(ax,x,y,s,11)
        ax.set_title("Pair production: ordering "+str(col+1),fontsize=12)
        setup(ax,xlim=(-.15,6.2),ylim=(-.65,3.95))
    fig.suptitle("Leading QED diagrams",fontsize=16)
    fig.text(.5,.022,"The heavy-source approximation retains radiation on the electron line. Crossings have no vertex dot.",ha="center",fontsize=10)
    fig.tight_layout(rect=(0,.05,1,.96),h_pad=2,w_pad=2);save(fig)

if __name__=="__main__":main()
