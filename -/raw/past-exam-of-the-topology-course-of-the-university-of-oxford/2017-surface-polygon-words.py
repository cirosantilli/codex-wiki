"""Generate 2017-surface-polygon-words.png in the current directory."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def main():
    models=[("Sphere", [("a",1),("b",1),("b",-1),("a",-1)],r"$a b b^{-1}a^{-1}$"),
            ("Torus", [("a",1),("b",1),("a",-1),("b",-1)],r"$a b a^{-1}b^{-1}$"),
            ("Real projective plane", [("a",1),("b",1),("a",1),("b",1)],r"$a b a b$"),
            ("Klein bottle", [("a",1),("b",1),("a",-1),("b",1)],r"$a b a^{-1}b$")]
    vertices=np.array([[-1,-1],[1,-1],[1,1],[-1,1]])
    colors={"a":"#2563eb","b":"#b91c1c"}
    fig,axes=plt.subplots(1,4,figsize=(12,3.6),dpi=100,facecolor="white")
    for ax,(title,word,formula) in zip(axes,models):
        ax.fill(vertices[:,0],vertices[:,1],color="#f1f5f9")
        for j,(label,sign) in enumerate(word):
            start,end=vertices[j],vertices[(j+1)%4];delta=end-start
            ax.plot([start[0],end[0]],[start[1],end[1]],color=colors[label],lw=2)
            aa=start+(.32 if sign>0 else .68)*delta
            bb=start+(.68 if sign>0 else .32)*delta
            ax.annotate("",xy=bb,xytext=aa,arrowprops=dict(arrowstyle="-|>",color=colors[label],lw=1.6,mutation_scale=13))
            normal=np.array([delta[1],-delta[0]])/np.linalg.norm(delta)
            mid=(start+end)/2+.22*normal
            ax.text(*mid,label,ha="center",va="center",fontsize=13,color=colors[label])
        ax.set(xlim=(-1.55,1.55),ylim=(-1.7,1.5));ax.set_aspect("equal");ax.axis("off")
        ax.set_title(title,fontsize=12,pad=7)
        ax.text(0,-1.58,formula,ha="center",va="center",fontsize=13)
    fig.suptitle("Pair edges in their arrow directions; read words counterclockwise",fontsize=14,y=.97)
    fig.subplots_adjust(left=.015,right=.985,top=.80,bottom=.06,wspace=.13)
    fig.savefig("2017-surface-polygon-words.png",dpi=100,facecolor="white");plt.close(fig)


if __name__=="__main__":main()
