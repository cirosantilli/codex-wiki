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


def labels(ax,nu,e,swap=False):
    txt(ax,.25,2.5,nu,11);txt(ax,.25,.25,e,11)
    txt(ax,5.8,2.5,e if swap else nu,11);txt(ax,5.8,.25,nu if swap else e,11)


def main():
    fig,axes=plt.subplots(4,2,figsize=(10,10.5))
    cases=[(r"$\nu_e$",r"$e^-$",False,"(i)"),(r"$\nu_\mu$",r"$e^-$",False,"(ii)"),
           (r"$\bar\nu_e$",r"$e^-$",True,"(iii)"),(r"$\bar\nu_e$",r"$e^+$",True,"(iv)")]
    for row,(ne,el,anti,title) in enumerate(cases):
        ax=axes[row,0]
        for y,rev in [(2.5,anti),(.25,row==3)]:
            line(ax,(.75,y),(3,y),reverse=rev);line(ax,(3,y),(5.25,y),reverse=rev)
        line(ax,(3,.25),(3,2.5),"wave",label=r"$Z$")
        labels(ax,ne,el);ax.set_title(title+"  Neutral current: $t$ channel",fontsize=12)
        ax=axes[row,1]
        if row==1:
            txt(ax,3,1.5,"No tree-level charged-current\ndiagram for this elastic channel",12,color="#555555")
        elif row==2:
            a,b=(2,1.4),(4,1.4)
            line(ax,(.75,2.5),a,reverse=True);line(ax,(.75,.25),a)
            line(ax,a,b,"wave",label=r"$W^-$")
            line(ax,b,(5.25,2.5),reverse=True);line(ax,b,(5.25,.25))
            labels(ax,ne,el);ax.set_title(title+"  Charged current: $s$ channel",fontsize=12)
        else:
            # Final positions are exchanged to show the crossed flavor pairing.
            for y in [2.5,.25]:
                line(ax,(.75,y),(3,y),reverse=anti);line(ax,(3,y),(5.25,y),reverse=anti)
            line(ax,(3,2.5),(3,.25),"wave",label=r"$W^-$" if anti else r"$W^+$")
            labels(ax,ne,el,swap=True);ax.set_title(title+"  Charged current: $u$ channel",fontsize=12)
        for ax in axes[row]:setup(ax,xlim=(-.25,6.3),ylim=(-.5,3.2))
    fig.suptitle("Elastic neutrino scattering: the allowed leading diagrams",fontsize=15)
    fig.text(.5,.018,"Outgoing positions are exchanged in the crossed diagrams. Arrows indicate fermion number.",ha="center",fontsize=10)
    fig.tight_layout(rect=(0,.04,1,.96),h_pad=1.7,w_pad=2);save(fig)

if __name__=="__main__":main()
