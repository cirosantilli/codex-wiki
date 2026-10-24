"""Oxford B10 2011: original backward-induction tree for question 4(e).

Writes 2011-american-put-tree.png in the process CWD, white background.
Tested with Python 3.14.4, Matplotlib 3.10.7; root pyproject.toml.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    nodes={"0":(0,0),"u":(1,1),"d":(1,-1),"uu":(2,2),"ud":(2,0),"dd":(2,-2)}
    labels={"0":"Stock: £100\nPut: £20\nWait", "u":"Stock: £120\nPut: £6\nWait", "d":"Stock: £90\nPut: £27\nExercise = wait", "uu":"Stock: £144\nPayoff: £0", "ud":"Stock: £108\nPayoff: £9", "dd":"Stock: £81\nPayoff: £36"}
    fig,ax=plt.subplots(figsize=(8.2,5.3),facecolor="white")
    for first,second in [("0","u"),("0","d"),("u","uu"),("u","ud"),("d","ud"),("d","dd")]:
        a,b=nodes[first],nodes[second]
        ax.annotate("",xy=b,xytext=a,arrowprops={"arrowstyle":"->","color":"#83929b","lw":1.5,"shrinkA":39,"shrinkB":39},zorder=1)
    for name,xy in nodes.items():
        ax.text(*xy,labels[name],ha="center",va="center",fontsize=11,bbox={"boxstyle":"round,pad=.5","facecolor":"#f3f7fa" if name!="d" else "#fff5e9","edgecolor":"#56717f","linewidth":1.2},zorder=3)
    for t in range(3):ax.text(t,-2.7,f"Time {t}",ha="center",fontsize=11,color="#3a4b55")
    ax.set_title("American put: strike £117, risk-free multiplier 1\nUp probability 1/3; down probability 2/3",fontsize=14,pad=20)
    ax.set(xlim=(-.45,2.55),ylim=(-2.95,2.6))
    ax.axis("off")
    fig.tight_layout()
    fig.savefig("2011-american-put-tree.png",dpi=150,facecolor="white")
    plt.close(fig)


if __name__=="__main__":main()
