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
    fig,axes=plt.subplots(1,2,figsize=(10.3,5.7))
    for ax in axes:
        ax.axhline(0,color="#666666",lw=.8);ax.axvline(0,color="#666666",lw=.8)
        ax.set(xlim=(-1.9,1.9),ylim=(-2.3,1.8),xlabel=r"$I_z$",ylabel=r"$B+S$")
        ax.set_xticks([-1.5,-1,-.5,0,.5,1,1.5]);ax.set_xticklabels([r"$-3/2$",r"$-1$",r"$-1/2$","0",r"$1/2$","1",r"$3/2$"],fontsize=9)
        ax.set_yticks([-2,-1,0,1]);ax.grid(alpha=.12)
        pts=np.array([[-.5,1],[.5,1],[1,0],[.5,-1],[-.5,-1],[-1,0],[-.5,1]])
        ax.plot(*pts.T,color="#a7b8c5",lw=1.4)
    ax=axes[0]
    for x,y,label,dx,dy in [(-.5,1,r"$n\ (udd)$",-.2,.28),(.5,1,r"$p\ (uud)$",.2,.28),
                           (-1,0,r"$\Sigma^-\ (dds)$",-.18,-.3),(1,0,r"$\Sigma^+\ (uus)$",.18,-.3),
                           (-.5,-1,r"$\Xi^-\ (dss)$",-.18,-.3),(.5,-1,r"$\Xi^0\ (uss)$",.18,-.3)]:
        ax.plot(x,y,"o",color="#145d91",ms=7);ax.text(x+dx,y+dy,label,ha="center",fontsize=11)
    ax.plot(0,0,"o",color="#145d91",ms=7)
    ax.text(.03,.28,r"$\Sigma^0,\ \Lambda^0$"+"\n"+r"$uds$",ha="center",fontsize=11,bbox=dict(facecolor="white",edgecolor="none",pad=1))
    for x,y in [(-1.5,1),(1.5,1),(0,-2)]:ax.plot(x,y,"o",ms=14,mfc="none",mec="#999999",ls="none")
    ax.set_title(r"Ground-state baryon octet, $J=1/2$",fontsize=12)
    ax=axes[1]
    for x,y,label,dx,dy in [(-.5,1,r"$K^0\ (d\bar s)$",-.2,.28),(.5,1,r"$K^+\ (u\bar s)$",.2,.28),
                           (-1,0,r"$\pi^-\ (d\bar u)$",-.18,-.3),(1,0,r"$\pi^+\ (u\bar d)$",.18,-.3),
                           (-.5,-1,r"$K^-\ (s\bar u)$",-.18,-.3),(.5,-1,r"$\bar K^0\ (s\bar d)$",.18,-.3)]:
        ax.plot(x,y,"o",color="#bd5c26",ms=7);ax.text(x+dx,y+dy,label,ha="center",fontsize=11)
    ax.plot(0,0,"o",color="#bd5c26",ms=7)
    ax.text(0,.23,r"$\pi^0,\ \eta,\ \eta'$",ha="center",fontsize=12,bbox=dict(facecolor="white",edgecolor="none",pad=1))
    ax.text(0,-1.95,r"$\eta,\eta'$ mix the octet and singlet basis states.",ha="center",fontsize=10)
    ax.set_title(r"Pseudoscalar meson nonet, $J=0$",fontsize=12)
    fig.suptitle("Light-hadron flavor weights: vertical coordinate is $B+S$",fontsize=14)
    fig.tight_layout(rect=(0,.02,1,.94),w_pad=2);save(fig)

if __name__=="__main__":main()
