"""Generate 2017-shortest-path-conventions.png in the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np


def draw(ax, positions, edges, labels, parents=None):
    for u,v,weight in edges:
        start,end=np.array(positions[u]),np.array(positions[v])
        color="#b91c1c" if weight<0 else "#64748b"
        ax.plot([start[0],end[0]],[start[1],end[1]],color=color,lw=1.5,zorder=0)
        middle=(start+end)/2
        ax.text(*middle,str(weight),ha="center",va="center",fontsize=12,bbox=dict(facecolor="white",edgecolor="none",pad=2))
    for vertex,point in positions.items():
        ax.add_patch(Circle(point,.14,facecolor="#dbeafe",edgecolor="#2563eb",lw=1.5,zorder=3))
        ax.text(*point,vertex,ha="center",va="center",fontsize=12,zorder=4)
        if labels:
            offset=(-.22,-.30) if vertex=="v" else (.19,.14)
            ax.text(point[0]+offset[0],point[1]+offset[1],labels[vertex],fontsize=10,color="#166534")
    for child,parent in parents or []:
        start,end=np.array(positions[child]),np.array(positions[parent]);direction=(end-start)/np.linalg.norm(end-start)
        ax.add_patch(FancyArrowPatch(start+.17*direction,end-.17*direction,arrowstyle="-|>",mutation_scale=16,color="#15803d",lw=2.5,zorder=2))
    ax.set_aspect("equal");ax.axis("off")


def main():
    fig,axes=plt.subplots(1,2,figsize=(10.8,4.5),dpi=100,facecolor="white")
    draw(axes[0],{"v":(0,1.4),"a":(-1,0),"b":(1,0)},[("v","a",2),("v","b",2),("a","b",-1)],None)
    axes[0].set(xlim=(-1.5,1.5),ylim=(-.8,1.9))
    axes[0].set_title("A signed triangle has no shortest-path tree",fontsize=12)
    axes[0].text(0,-.43,"v → b → a and v → a → b both have weight 1",ha="center",fontsize=10)
    draw(axes[1],{"v":(0,.8),"a":(1,1.7),"b":(1,-.1),"c":(2.3,.8)},[("v","a",2),("v","b",1),("a","b",2),("a","c",1),("b","c",4)],{"v":"d=0","a":"d=2","b":"d=1","c":"d=3"},[("a","v"),("b","v"),("c","a")])
    axes[1].set(xlim=(-.4,2.9),ylim=(-.8,2.1))
    axes[1].set_title("Positive weights: predecessors decrease distance",fontsize=12)
    axes[1].text(1.2,-.53,"Green arrows select a rooted shortest-path tree",ha="center",fontsize=10,color="#166534")
    fig.suptitle("Shortest simple paths and compatible predecessor choices",fontsize=15,y=.96)
    fig.subplots_adjust(left=.03,right=.98,bottom=.06,top=.82,wspace=.22)
    fig.savefig("2017-shortest-path-conventions.png",dpi=100,facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
