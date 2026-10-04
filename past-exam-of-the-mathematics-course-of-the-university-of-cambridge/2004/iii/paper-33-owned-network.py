"""Draw the owned communication network. Tested with Python 3.14; NumPy/Matplotlib from root pyproject."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def main():
    fig,ax=plt.subplots(figsize=(9,5),dpi=120,facecolor="white")
    ax.set_facecolor("white")
    positions={"A":(0,0),"B":(2.1,1.1),"C":(2.1,-1.1),"D":(4.2,0)}
    colors={"i":"#17689e","j":"#be5b13","k":"#6a4599"}
    edges=[("A","B","i",3,(-.10,.22)),("A","C","j",1,(-.10,-.25)),
           ("B","D","j",1,(.10,.22)),("C","D","i",2,(.10,-.25)),
           ("B","C","k",2,(.32,0))]
    for u,v,owner,capacity,offset in edges:
        p,q=positions[u],positions[v]
        ax.add_patch(FancyArrowPatch(p,q,arrowstyle="-|>",mutation_scale=18,
                                    linewidth=2.2,color=colors[owner],shrinkA=15,shrinkB=15))
        x,y=(p[0]+q[0])/2+offset[0],(p[1]+q[1])/2+offset[1]
        ax.text(x,y,f"{owner}: capacity {capacity}",fontsize=12,ha="center",va="center",
                color=colors[owner],bbox={"facecolor":"white","edgecolor":"none","pad":2})
    for name,(x,y) in positions.items():
        ax.scatter([x],[y],s=650,color="white",edgecolors="#222222",linewidths=1.7,zorder=4)
        ax.text(x,y,name,fontsize=15,ha="center",va="center",zorder=5)
    ax.text(2.1,1.62,"Communication links: owner and flow capacity",ha="center",fontsize=15)
    ax.text(2.1,-1.61,"A to D earns £6000/unit; B to C earns £4000/unit",
            ha="center",fontsize=12)
    ax.set_xlim(-.6,4.8);ax.set_ylim(-1.9,1.95);ax.set_aspect("equal");ax.axis("off")
    fig.subplots_adjust(left=.03,right=.97,bottom=.03,top=.98)
    fig.savefig(Path.cwd()/"paper-33-owned-network.png",dpi=120,facecolor="white",transparent=False)
    plt.close(fig)

if __name__=="__main__":
    main()
