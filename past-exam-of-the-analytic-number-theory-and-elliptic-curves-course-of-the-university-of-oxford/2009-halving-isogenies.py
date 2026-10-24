"""Original isogeny lifting diagram. Python 3.14 and Matplotlib. Output in CWD."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(9,4.8),facecolor="white")
ax.set(xlim=(0,10),ylim=(0,5));ax.axis("off")
box=dict(boxstyle="round,pad=.65",fc="#f0f7fb",ec="#2166ac",lw=1.5)
ax.text(1.4,2.5,r"$R\in C(\mathbb{Q})$",ha="center",va="center",bbox=box,fontsize=14)
ax.text(5,3.7,r"$Q_1=(\alpha,-2\alpha)$",ha="center",va="center",bbox=box,fontsize=13)
ax.text(5,1.3,r"$Q_2=(\alpha+4,\,2(\alpha+4))$",ha="center",va="center",bbox=box,fontsize=12)
ax.text(8.9,2.5,r"$P=(1,1)$",ha="center",va="center",bbox=box,fontsize=14)
for start,end in [((2.5,2.7),(3.5,3.35)),((2.5,2.3),(3.5,1.65)),
                  ((6.55,3.35),(8,2.75)),((6.75,1.65),(8,2.25))]:
 ax.annotate("",end,start,arrowprops=dict(arrowstyle="->",lw=1.7,color="#2166ac"))
ax.text(2.7,3.4,r"$\phi$",fontsize=15);ax.text(2.7,1.6,r"$\phi$",fontsize=15)
ax.text(7.2,3.45,r"$\widehat\phi$",fontsize=15);ax.text(7.3,1.45,r"$\widehat\phi$",fontsize=15)
ax.text(5,4.6,r"First lift exists iff $\alpha$ is a rational square.",ha="center",fontsize=12)
ax.text(5,.45,r"Second lift exists iff $\alpha+4$ is a rational square.",ha="center",fontsize=12)
ax.text(5,2.5,r"$\widehat\phi\circ\phi=[2]$",ha="center",fontsize=15,color="#176858")
ax.set_title("A half of P exists exactly when one branch lifts",fontsize=15,pad=16)
fig.tight_layout()
fig.savefig("2009-halving-isogenies.png",dpi=150,facecolor="white")
