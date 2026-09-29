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
    fig,ax=plt.subplots(figsize=(8.4,7.0))
    # The six incoming valence lines and their outgoing flavor assignments.
    incoming=[(9.2,9.2,"u"),(8.65,8.65,"u"),(8.1,8.1,"d"),
              (6.6,6.6,"u"),(6.05,4.2,"u"),(5.5,6.05,"d")]
    for ya,yb,q in incoming:
        line(ax,(1,ya),(8,yb));txt(ax,.65,ya,"$"+q+"$",11);txt(ax,8.3,yb,"$"+q+"$",11)
    v1=(4,3.0);v2=(4.6,4.85)
    line(ax,(2,6.6),v1,"gluon",label=r"$g$")
    # Second emission is placed exactly on the incoming d line.
    line(ax,(2,5.5+.55/7),v2,"gluon",label=r"$g$")
    for v,end,lab,rev in [(v1,(8,3.65),r"$\bar d$",True),(v1,(8,2.25),r"$d$",False),
                          (v2,(8,5.5),r"$s$",False),(v2,(8,1.7),r"$\bar s$",True)]:
        line(ax,v,end,reverse=rev);txt(ax,8.3,end[1],lab,11)
    for lo,hi,name in [(8.0,9.3,r"$p\ (uud)$"),(5.4,6.7,r"$\Lambda^0\ (uds)$"),
                        (3.55,4.3,r"$\pi^+\ (u\bar d)$"),(1.6,2.35,r"$K^0\ (d\bar s)$")]:
        ax.plot([8.6,8.8,8.8,8.6],[lo,lo,hi,hi],color="#8a4c20",lw=1.4)
        ax.text(9.0,(lo+hi)/2,name,va="center",fontsize=12)
    txt(ax,.2,8.65,r"$p$",13);txt(ax,.2,6.05,r"$p$",13)
    txt(ax,4.8,.55,r"New pairs: $d\bar d$ and $s\bar s$; net flavor is conserved.",11)
    setup(ax,xlim=(-.1,11.6),ylim=(.1,10))
    ax.set_title("Associated kaon production: one quark-flow assignment",fontsize=14,pad=15)
    fig.text(.5,.025,"Crossings are not vertices. Additional gluon exchanges and color flow are suppressed.",ha="center",fontsize=9)
    fig.tight_layout(rect=(0,.06,1,.98));save(fig)

if __name__=="__main__":main()
