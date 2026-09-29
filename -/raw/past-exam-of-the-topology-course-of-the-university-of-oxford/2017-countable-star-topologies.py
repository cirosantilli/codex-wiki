"""Generate 2017-countable-star-topologies.png in the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    fig,(left,right)=plt.subplots(1,2,figsize=(10,4.7),dpi=100,facecolor="white")
    for n,angle in enumerate(np.linspace(0,2*np.pi,9,endpoint=False),start=1):
        direction=np.array([np.cos(angle),np.sin(angle)])
        delta=.4/n;point=.8/n
        left.plot([0,direction[0]],[0,direction[1]],color="#94a3b8",lw=1.1)
        left.plot([0,delta*direction[0]],[0,delta*direction[1]],color="#2563eb",lw=4)
        left.scatter([point*direction[0]],[point*direction[1]],color="#b91c1c",s=24,zorder=5)
        if n in [1,3,6]:
            left.text(*(1.11*direction),rf"arm {n}",ha="center",va="center",fontsize=9)
    left.scatter([0],[0],color="#111827",s=25,zorder=6)
    left.text(-1.15,-1.32,r"Blue: $0\leq t<t_n/2$; red: $x_n$ at $t_n$",fontsize=10)
    left.set_title("Weak star: independent radii on the arms",fontsize=12,pad=12)
    left.set(xlim=(-1.4,1.4),ylim=(-1.4,1.3));left.set_aspect("equal");left.axis("off")
    for n in range(1,19):
        direction=np.exp(1j/n)
        right.plot([0,direction.real],[0,direction.imag],color="#64748b",lw=1)
        right.plot([0,.27*direction.real],[0,.27*direction.imag],color="#2563eb",lw=2.1)
        if n in [1,2]:right.text(direction.real+.025,direction.imag,rf"$n={n}$",fontsize=10)
    right.plot([0,1.12],[0,0],color="#b91c1c",ls="--",lw=1.3)
    right.add_patch(Circle((0,0),.27,fill=False,color="#7e22ce",lw=1.1,ls=":"))
    right.scatter([0],[0],color="#111827",s=25,zorder=5)
    right.annotate(r"Uniform radius $\varepsilon$",xy=(.22,.14),xytext=(.28,.35),fontsize=10,
                   arrowprops=dict(arrowstyle="->",color="#7e22ce"),color="#7e22ce")
    right.text(.53,-.10,"Limiting ray omitted",color="#b91c1c",fontsize=10,ha="center")
    right.set_title(r"Metric fan: $t\mapsto te^{i/n}$",fontsize=12,pad=12)
    right.set(xlim=(-.15,1.28),ylim=(-.25,1.05));right.set_aspect("equal");right.axis("off")
    fig.suptitle("A finite drawing illustrates two different infinite-star topologies",fontsize=14,y=.97)
    fig.subplots_adjust(left=.025,right=.98,top=.80,bottom=.09,wspace=.20)
    fig.savefig("2017-countable-star-topologies.png",dpi=100,facecolor="white");plt.close(fig)


if __name__=="__main__":main()
