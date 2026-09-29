"""Generate PNG in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,2,figsize=(9,4.5),facecolor="white",layout="constrained")
a,b=2.,1.5
ax=axs[0]
ax.fill([0,3.2,3.2,0],[0,0,2.8,2.8],color="#eaf4fa")
ax.axhline(0,color="0.25",lw=1.5);ax.axvline(0,color="0.25",lw=1.5)
for x,y,positive,label in[(a,b,True,r"$+\Gamma$"),(a,-b,False,r"$-\Gamma$"),(-a,b,False,r"$-\Gamma$"),(-a,-b,True,r"$+\Gamma$")]:
 ax.scatter([x],[y],color="#12679b"if positive else"#b86a16",s=55,zorder=5)
 ax.text(x+.12,y+.12,label,fontsize=13)
ax.text(.3,2.45,"Physical fluid",color="#12679b",fontsize=11)
ax.set(xlim=(-3,3.2),ylim=(-2.5,2.8),aspect="equal",xlabel="$x$",ylabel="$y$",title="Three images enforce both walls")
ax=axs[1];ell=a*b/np.sqrt(a*a+b*b);const=1/a**2+1/b**2
x=np.linspace(ell*1.001,5.5,1000);y=1/np.sqrt(const-1/x**2)
ax.plot(x,y,color="#12679b",lw=2)
ax.axvline(ell,color="0.5",ls="--",lw=1);ax.axhline(ell,color="0.5",ls="--",lw=1)
ax.scatter([a],[b],color="#b23c41",s=35,zorder=5);ax.text(a+.08,b+.16,"$(a,b)$",fontsize=11)
for v in[1.45,2.7,4.1]:
 def f(t):return 1/np.sqrt(const-1/t**2)
 ax.annotate("",xy=(v+.18,f(v+.18)),xytext=(v,f(v)),arrowprops=dict(arrowstyle="->",color="#12679b",lw=2))
ax.text(1.3,4.6,r"$x=\ell$",fontsize=11);ax.text(4.2,ell+.12,r"$y=\ell$",fontsize=11)
ax.set(xlim=(0,5.5),ylim=(0,5.2),aspect="equal",xlabel="$x_1$",ylabel="$y_1$",title=r"$x_1^{-2}+y_1^{-2}=a^{-2}+b^{-2}$")
ax.grid(alpha=.15)
fig.savefig("2006-options-quadrant-vortex.png",dpi=160,facecolor="white")
