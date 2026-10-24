"""Original Fourier branch-cut prescription. Python3.14 and Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(8,5),facecolor="white")
eps=.8;delta=.4
ax.axhline(0,color=".75",lw=.8);ax.axvline(0,color=".75",lw=.8)
ax.plot([0,0],[eps,1.8],color="#b2182b",lw=3)
ax.plot([0,0],[0,-1.4],color="#2166ac",lw=3)
ax.scatter([0,0],[eps,0],s=40,color=["#b2182b","#2166ac"],zorder=5)
ax.plot([-2,2],[delta,delta],color="#176858",lw=2)
ax.annotate("",(1.4,delta),(.8,delta),arrowprops=dict(arrowstyle="->",color="#176858",lw=2))
ax.text(.15,1.3,r"cut of $(\widehat k-i\epsilon)^{1/2}$",color="#b2182b",fontsize=12)
ax.text(.15,-.9,r"cut of $\widehat k^{-3/4}$",color="#2166ac",fontsize=12)
ax.text(.1,eps+.05,r"$i\epsilon$",fontsize=12);ax.text(.07,-.18,"0",fontsize=11)
ax.text(-1.95,delta+.12,r"$\operatorname{Im}\widehat k=\delta=\epsilon/2$",color="#176858",fontsize=12)
ax.scatter([-.9],[-.5],color=".2",marker="x",s=60)
ax.text(-1.85,-.6,r"pole at $\widehat k=k$",fontsize=11)
ax.set(xlim=(-2,2),ylim=(-1.4,1.8),xlabel=r"$\operatorname{Re}\widehat k$",
       ylabel=r"$\operatorname{Im}\widehat k$",title="The contour stays between two opposing branch cuts")
ax.spines[["top","right"]].set_visible(False)
fig.tight_layout();fig.savefig("2008-branch-cuts.png",dpi=150,facecolor="white")
