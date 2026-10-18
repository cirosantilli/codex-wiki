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
    fig,axes=plt.subplots(2,1,figsize=(8.8,7.5))
    ax=axes[0]
    line(ax,(.6,2.2),(2,1.3),reverse=True);line(ax,(.6,.4),(2,1.3))
    txt(ax,.25,2.2,r"$\bar d$");txt(ax,.25,.4,r"$u$")
    line(ax,(2,1.3),(3.5,1.3),"wave",label=r"$W^{+*}$")
    line(ax,(3.5,1.3),(7.4,2.6));txt(ax,7.8,2.6,r"$\nu_\mu$")
    line(ax,(3.5,1.3),(5.2,.4),reverse=True)
    line(ax,(5.2,.4),(7.4,.4),reverse=True);txt(ax,7.8,.4,r"$\mu^+$")
    line(ax,(5.2,.4),(7.3,-1.1),"wave");txt(ax,7.8,-1.1,r"$\gamma$")
    txt(ax,4.5,.35,r"$\mu^{+*}$",10)
    setup(ax,xlim=(-.2,8.5),ylim=(-1.65,3.2))
    ax.set_title(r"$\pi^+(u\bar d)\to\mu^+\nu_\mu\gamma$: one emission diagram",fontsize=13)
    ax=axes[1]
    line(ax,(.6,1.2),(2,1.2));txt(ax,.2,1.2,r"$\mu^-$")
    line(ax,(2,1.2),(4.1,2.9));txt(ax,4.5,2.9,r"$\nu_\mu$")
    line(ax,(2,1.2),(3.6,1.2),"wave",label=r"$W^{-*}$")
    line(ax,(3.6,1.2),(5.1,1.2));line(ax,(5.1,1.2),(7.6,1.2));txt(ax,8,1.2,r"$e^-_1$")
    line(ax,(3.6,1.2),(6,-1),reverse=True);txt(ax,6.45,-1,r"$\bar\nu_e$")
    line(ax,(5.1,1.2),(6.2,2.5),"wave",label=r"$\gamma^*$")
    line(ax,(6.2,2.5),(7.6,3.15));txt(ax,8,3.15,r"$e^-_2$")
    line(ax,(6.2,2.5),(7.6,2.15),reverse=True);txt(ax,8,2.15,r"$e^+$")
    setup(ax,xlim=(-.2,8.5),ylim=(-1.65,3.65))
    ax.set_title(r"$\mu^-\to e^-e^-e^+\nu_\mu\bar\nu_e$: internal photon conversion",fontsize=13)
    fig.text(.5,.025,"Solid arrows show fermion number; starred lines are off shell. Complete amplitudes need the other emissions.",ha="center",fontsize=9)
    fig.tight_layout(rect=(0,.06,1,.99),h_pad=2);save(fig)

if __name__=="__main__":main()
