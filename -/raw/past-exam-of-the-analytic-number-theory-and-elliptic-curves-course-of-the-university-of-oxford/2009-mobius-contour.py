"""Original contour schematic. Python 3.14, NumPy and Matplotlib. Output in CWD."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(8,5),facecolor="white")
alpha,c,T=.42,1.4,1.6
ax.axhline(0,color=".75",lw=.8);ax.axvline(0,color=".75",lw=.8)
ax.axvspan(alpha,1,alpha=.10,color="#2a9d8f")
ax.plot([c,c],[-T,T],color="#2166ac",lw=2.5)
ax.plot([c,c],[-2.2,-T],color="#2166ac",lw=2,ls="--")
ax.plot([c,c],[T,2.2],color="#2166ac",lw=2,ls="--")
ax.plot([c,alpha,alpha,c],[T,T,-T,-T],color="#b2182b",lw=2)
for x,y,dy,col in [(c,0,.45,"#2166ac"),(alpha,0,.45,"#b2182b")]:
 ax.annotate("",(x,y+dy),(x,y),arrowprops=dict(arrowstyle="->",color=col,lw=2))
ax.scatter([1],[0],s=45,color="#2a9d8f",zorder=5)
ax.annotate(r"$1/\zeta$ has a zero at $1$",(1,0),(.70,.55),
             arrowprops=dict(arrowstyle="->",color=".3"),fontsize=11)
ax.text(.13,1.81,r"$t=T$",fontsize=11)
ax.text(.11,-1.98,r"$t=-T$",fontsize=11)
ax.text(1.45,1.9,"tail estimate",color="#2166ac",fontsize=11)
ax.text(.45,-.75,"finite zero-free\nrectangle",color="#176858",fontsize=11)
ax.text(.20,-2.65,r"First $x\to\infty$ at fixed $T$; then $T\to\infty$.",fontsize=12)
ax.set(xticks=[alpha,1,c],xticklabels=[r"$\alpha_T$","1",r"$c=1+1/\log x$"],
       yticks=[],xlim=(-.12,2.1),ylim=(-2.8,2.4),xlabel=r"$\operatorname{Re}s$",
       ylabel=r"$\operatorname{Im}s$",title="A finite contour shift for the smoothed Möbius sum")
ax.spines[["top","right"]].set_visible(False)
fig.tight_layout()
fig.savefig("2009-mobius-contour.png",dpi=150,facecolor="white")
