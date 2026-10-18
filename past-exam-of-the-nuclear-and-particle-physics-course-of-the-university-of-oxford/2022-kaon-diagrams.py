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
    fig,axes=plt.subplots(3,1,figsize=(8.4,10.0))
    ax=axes[0]
    for y,lab1,lab2,rev in [(2.1,r"$\bar s$",r"$\bar d$",True),(.1,r"$d$",r"$s$",False)]:
        line(ax,(.7,y),(2.2,y),reverse=rev)
        line(ax,(2.2,y),(4.8,y),reverse=rev)
        line(ax,(4.8,y),(6.3,y),reverse=rev)
        txt(ax,.35,y,lab1);txt(ax,6.65,y,lab2)
    line(ax,(2.2,.1),(2.2,2.1),"wave",label=r"$W$")
    line(ax,(4.8,.1),(4.8,2.1),"wave",label=r"$W$")
    txt(ax,3.5,2.5,r"$\bar u_j$",11);txt(ax,3.5,-.25,r"$u_i$",11)
    txt(ax,3.5,3.15,r"$K^0(d\bar s)\ \longrightarrow\ \bar K^0(s\bar d)$",13)
    txt(ax,3.5,-.75,r"$u_i,u_j=u,c,t$; four charged-current vertices",10)
    setup(ax,ylim=(-1.0,3.6))
    for ax,three in zip(axes[1:],[False,True]):
        line(ax,(.7,1.1),(2.1,1.1),reverse=True)
        line(ax,(2.1,1.1),(6.2,1.1),reverse=True)
        line(ax,(.7,-.1),(6.2,-.1))
        line(ax,(2.1,1.1),(3.5,2.5),"wave",label=r"$W^+$")
        line(ax,(3.5,2.5),(6.2,3.1))
        line(ax,(3.5,2.5),(6.2,2.3),reverse=True)
        for x,y,s in [(.35,1.1,r"$\bar s$"),(.35,-.1,r"$d$"),(6.6,3.1,r"$u$"),(6.6,2.3,r"$\bar d$"),(6.6,1.1,r"$\bar u$"),(6.6,-.1,r"$d$")]:txt(ax,x,y,s)
        if three:
            line(ax,(1.5,-.1),(3.5,-1.3),"gluon",label=r"$g$")
            line(ax,(3.5,-1.3),(6.2,-1.0))
            line(ax,(3.5,-1.3),(6.2,-1.9),reverse=True)
            txt(ax,6.6,-1.0,r"$d$");txt(ax,6.6,-1.9,r"$\bar d$")
        setup(ax,ylim=(-2.3,3.65))
        ax.set_title(r"$K^0\to\pi^+\pi^-\pi^0$: add a soft $d\bar d$ pair" if three else r"$K^0\to\pi^+\pi^-$: spectator $d$",fontsize=12,pad=5)
    fig.suptitle("Neutral-kaon mixing and representative weak decays",fontsize=15)
    fig.text(.5,.015,"Fermion arrows track quark number. Charge-conjugate amplitudes complete the CP states.",ha="center",fontsize=9)
    fig.tight_layout(rect=(0,.04,1,.96),h_pad=1.4);save(fig)

if __name__=="__main__":main()
