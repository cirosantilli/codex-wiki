"""Original nonrecombining American Asian-put tree, Oxford B10 2010.

Writes 2010-asian-put-tree.png in the process CWD, white background.
Tested: Python 3.14.4, Matplotlib 3.10.7; root pyproject.toml.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    points={"0":(0,0),"u":(1,1.5),"d":(1,-1.5),"uu":(2,2.5),"ud":(2,.85),"du":(2,-.85),"dd":(2,-2.5)}
    text={"0":"S = £100, A = £100\nExercise: £15\nContinuation: £100/11",
          "u":"S = £120, A = £110\nOption: £5 (exercise)",
          "d":"S = £100, A = £100\nOption: £15 (exercise)",
          "uu":"S = £144, A = £364/3\nPayoff: £0",
          "ud":"S = £120, A = £340/3\nPayoff: £5/3",
          "du":"S = £120, A = £320/3\nPayoff: £25/3",
          "dd":"S = £100, A = £100\nPayoff: £15"}
    fig,ax=plt.subplots(figsize=(10,6.4),facecolor="white")
    for a,b in [("0","u"),("0","d"),("u","uu"),("u","ud"),("d","du"),("d","dd")]:
        ax.annotate("",xy=points[b],xytext=points[a],arrowprops={"arrowstyle":"->","color":"#85939a","lw":1.6,"shrinkA":52,"shrinkB":52},zorder=1)
    for name,xy in points.items():
        ax.text(*xy,text[name],ha="center",va="center",fontsize=10.5,bbox={"boxstyle":"round,pad=.6","facecolor":"#fff3e3" if len(name)<2 else "#f0f6fa","edgecolor":"#597481","linewidth":1.2},zorder=3)
    for t in range(3):ax.text(t,-3.25,f"Time {t}",ha="center",fontsize=12)
    ax.set_title("Arithmetic-average American put: strike £115\nRisk-free multiplier 1.1; each branch has probability 1/2",fontsize=14,pad=20)
    ax.set(xlim=(-.5,2.55),ylim=(-3.5,3.15))
    ax.axis("off")
    fig.tight_layout()
    fig.savefig("2010-asian-put-tree.png",dpi=150,facecolor="white")
    plt.close(fig)


if __name__=="__main__":main()
