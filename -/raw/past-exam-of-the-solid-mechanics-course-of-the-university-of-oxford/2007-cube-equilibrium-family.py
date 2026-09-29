"""Generate PNG in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
v=np.linspace(.08,4.6,1000);x,y=np.meshgrid(v,v);s=x+y+1/(x*y)
fig,ax=plt.subplots(figsize=(5.5,4.6),facecolor="white",layout="constrained")
cs=ax.contour(x,y,s,levels=[3.1,4,5],colors=["#12679b","#b86a16","#197c4d"],linewidths=2)
ax.clabel(cs,fmt=lambda q:fr"$\tau/\mu={q:g}$",inline=True,fontsize=10)
ax.scatter([1],[1],color="#b23c41",s=35,zorder=5)
ax.annotate("Unit triple",xy=(1,1),xytext=(1.5,.45),arrowprops=dict(arrowstyle="->",color="#b23c41"),color="#b23c41",fontsize=10)
ax.set(xlim=(0,4.6),ylim=(0,4.6),aspect="equal",xlabel="$v_1$",ylabel="$v_2$",title=r"Equilibrium families with $v_3=1/(v_1v_2)$")
ax.grid(alpha=.15)
fig.savefig("2007-cube-equilibrium-family.png",dpi=160,facecolor="white")
