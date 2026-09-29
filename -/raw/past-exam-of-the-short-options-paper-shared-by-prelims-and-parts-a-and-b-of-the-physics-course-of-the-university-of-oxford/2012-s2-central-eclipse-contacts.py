"""Conditional standard-contact geometry, with no recovered light-curve data."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def main():
    plt.rcParams.update({"font.size":12,"figure.facecolor":"white","axes.facecolor":"white"})
    fig,axes=plt.subplots(1,4,figsize=(11,3),layout="constrained");small=.45;centres=[-1-small,-1+small,1-small,1+small]
    for j,(ax,pos)in enumerate(zip(axes,centres),1):
        ax.add_patch(Circle((0,0),1,facecolor="#F0C75E",edgecolor=".3",lw=1.3));ax.add_patch(Circle((pos,0),small,facecolor="#B46B52",edgecolor=".2",lw=1.3));ax.axhline(0,color=".5",lw=.7,ls=":");ax.set(xlim=(-2,2),ylim=(-1.2,1.2),title=rf"$t_{j}$: "+("external contact"if j in[1,4]else"internal contact"));ax.set_aspect("equal");ax.set_axis_off()
        ax.annotate("",(pos+.25,-.8),(pos-.25,-.8),arrowprops={"arrowstyle":"->"})
    fig.suptitle("Central eclipse with a smaller foreground star: standard contact labels",fontsize=13)
    fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120,facecolor="white");plt.close(fig)


if __name__=="__main__":main()
