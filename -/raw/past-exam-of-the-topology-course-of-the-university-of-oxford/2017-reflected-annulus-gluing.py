"""Generate 2017-reflected-annulus-gluing.png in the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def main():
    fig,ax=plt.subplots(figsize=(8,5.2),dpi=100,facecolor="white")
    ax.add_patch(Rectangle((0,0),1,1,facecolor="#dbeafe",edgecolor="none"))
    ax.add_patch(Rectangle((0,1),1,1,facecolor="#dcfce7",edgecolor="none"))
    for yy in [0,2]:ax.plot([0,1],[yy,yy],color="#b91c1c",lw=2)
    for xx in [0,1]:ax.plot([xx,xx],[0,2],color="#2563eb",lw=2)
    ax.plot([0,1],[1,1],color="#64748b",lw=1.5,ls="--")
    for start,end in [((.30,0),(.70,0)),((.70,2),(.30,2))]:
        ax.annotate("",xy=end,xytext=start,arrowprops=dict(arrowstyle="-|>",color="#b91c1c",lw=2,mutation_scale=16))
    for xx in [0,1]:
        ax.annotate("",xy=(xx,1.35),xytext=(xx,.65),arrowprops=dict(arrowstyle="-|>",color="#2563eb",lw=2,mutation_scale=16))
    ax.text(.5,.48,r"$A_1:\ \tau=2r-1$",ha="center",fontsize=14,color="#1d4ed8")
    ax.text(.5,1.5,r"$A_2:\ \tau=3-2r$",ha="center",fontsize=14,color="#166534")
    ax.text(.5,1.06,"Outer boundaries: identity gluing",ha="center",va="bottom",fontsize=10)
    ax.text(-.07,0,r"$\tau=0$",ha="right",va="center",fontsize=12)
    ax.text(-.07,1,r"$\tau=1$",ha="right",va="center",fontsize=12)
    ax.text(-.07,2,r"$\tau=2$",ha="right",va="center",fontsize=12)
    ax.text(.5,2.20,r"Inner ends: $(z,0)\sim(\overline{z},2)$",ha="center",fontsize=13,color="#b91c1c")
    ax.text(.5,-.19,r"Angular coordinate $\theta/(2\pi)$",ha="center",fontsize=12)
    ax.text(1.06,1,"Circle\nperiodicity",ha="left",va="center",fontsize=11,color="#2563eb")
    ax.set(xlim=(-.30,1.40),ylim=(-.33,2.45));ax.axis("off")
    fig.suptitle("Two annuli give the reflection mapping torus: a Klein bottle",fontsize=14,y=.97)
    fig.subplots_adjust(left=.04,right=.98,top=.88,bottom=.04)
    fig.savefig("2017-reflected-annulus-gluing.png",dpi=100,facecolor="white");plt.close(fig)


if __name__=="__main__":main()
