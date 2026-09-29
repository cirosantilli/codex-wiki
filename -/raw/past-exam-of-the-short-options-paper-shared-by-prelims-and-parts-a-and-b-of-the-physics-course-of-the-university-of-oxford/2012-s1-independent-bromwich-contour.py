"""An independently chosen contour, not a reconstruction of the absent figure."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({"font.size":12,"figure.facecolor":"white","axes.facecolor":"white"})
    fig,ax=plt.subplots(figsize=(7,5.4),layout="constrained");R=3.;sig=1.;eps=.36;d=.13;b=np.sqrt(eps**2-d**2)
    ax.axhline(0,color=".75",lw=.8);ax.axvline(0,color=".75",lw=.8);ax.plot([-R,0],[0,0],color="#D55E00",lw=2,ls="--",label="negative-real branch cut")
    def edge(p,q,color=".25"):
        ax.plot([p[0],q[0]],[p[1],q[1]],color=color,lw=1.8)
        v=np.array(q)-np.array(p);mid=(np.array(p)+np.array(q))/2
        ax.annotate("",mid+.08*v,mid-.08*v,arrowprops={"arrowstyle":"->","color":color,"lw":1.8})
    edge((sig,-R),(sig,R),"black");edge((sig,R),(-R,R));edge((-R,R),(-R,d))
    edge((-R,d),(-b,d),"#0072B2");angle=np.arcsin(d/eps);th=np.linspace(np.pi-angle,-np.pi+angle,401)
    ax.plot(eps*np.cos(th),eps*np.sin(th),color="#0072B2",lw=1.8);ax.annotate("",(eps*np.cos(-.25),eps*np.sin(-.25)),(eps*np.cos(.25),eps*np.sin(.25)),arrowprops={"arrowstyle":"->","color":"#0072B2","lw":1.8})
    edge((-b,-d),(-R,-d),"#0072B2");edge((-R,-d),(-R,-R));edge((-R,-R),(sig,-R))
    ax.scatter([0],[0],color="#D55E00",s=22,zorder=5);ax.text(1.11,1.5,r"$\gamma$ upward",fontsize=11);ax.text(-2.6,2.6,r"$\Gamma$: independent slit rectangle");ax.text(-1.8,.37,r"$(-x+i0)^{-1/2}=-i/\sqrt{x}$",fontsize=10);ax.text(-1.8,-.55,r"$(-x-i0)^{-1/2}=+i/\sqrt{x}$",fontsize=10)
    ax.set(xlim=(-3.7,2.5),ylim=(-3.5,3.5),xlabel=r"$\mathrm{Re}\,z$",ylabel=r"$\mathrm{Im}\,z$",title="A valid deformation when the original contour is unavailable");ax.set_xticks([-R,0,sig],[r"$-R$","0",r"$\sigma=1$"]);ax.set_yticks([-R,0,R],[r"$-R$","0",r"$R$"]);ax.set_aspect("equal");ax.legend(loc="lower left",fontsize=9)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white");plt.close(fig)


if __name__=="__main__":main()
