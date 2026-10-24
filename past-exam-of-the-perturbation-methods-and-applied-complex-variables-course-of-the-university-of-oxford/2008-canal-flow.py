"""Original free-streamline and hodograph plot. Python3.14, NumPy, Matplotlib. Output CWD."""
import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
a=.5;t=np.linspace(-np.pi+1e-7,-.002,2000)
x=-a/np.pi*(np.log(1-np.cos(t))+np.cos(t)-np.log(2)+1)
y=1-a/np.pi*(t+np.pi+np.sin(t))
right=1.1;mask=x<right;x=x[mask];y=y[mask];t=t[mask]
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,4.7),facecolor="white",gridspec_kw={"width_ratios":[1.3,1]})
poly=np.array([[-.55,0],[right,0],[right,y[-1]],*zip(x[::-1],y[::-1]),[0,1],[right,1],[right,1.5],[-.55,1.5]])
ax.fill(poly[:,0],poly[:,1],color="#d8eef7")
ax.plot([-.55,right],[0,0],color=".2",lw=3);ax.plot([0,right],[1,1],color=".2",lw=3)
ax.plot(x,y,color="#2166ac",lw=2.5);ax.plot([.2,right],[a,a],color=".6",ls=":",lw=1)
ax.scatter([0],[1],color=".15",s=25,zorder=5);ax.text(.025,1.07,"D",fontsize=12)
ax.text(.43,.80,"air",fontsize=12,color=".4");ax.text(-.48,1.24,"fluid",fontsize=12)
ax.text(.63,.38,r"$a=1/2$",fontsize=12)
for start,end in [((.3,.21),(.68,.21)),((.8,1.21),(.42,1.21))]:
 ax.annotate("",end,start,arrowprops=dict(arrowstyle="->",color="#176858",lw=2))
ax.set(xlim=(-.55,right),ylim=(-.05,1.5),xlabel=r"$x$",ylabel=r"$y$",title="Physical plane")
ax.set_aspect("equal");ax.spines[["top","right"]].set_visible(False)
ang=np.linspace(0,np.pi,300);qx=np.cos(ang);qy=np.sin(ang)
bx.fill(np.r_[qx,-1],np.r_[qy,0],color="#d8eef7")
bx.plot(qx,qy,color="#2166ac",lw=2.5);bx.plot([-1,1],[0,0],color=".25",lw=2)
bx.scatter([-1,0,1],[0,0,0],s=25,color=".2",zorder=5)
bx.text(-1,-.18,"D",ha="center",fontsize=12);bx.text(0,-.18,"A, E",ha="center",fontsize=12)
bx.text(1,-.18,"B, C",ha="center",fontsize=12)
bx.text(-.45,.45,r"$q=e^{-i\theta}$",fontsize=13)
bx.annotate("",(.6,.8),(.15,.99),arrowprops=dict(arrowstyle="->",color="#2166ac",lw=2))
bx.set(xlim=(-1.2,1.2),ylim=(-.3,1.25),xlabel=r"$\operatorname{Re}q=u$",
       ylabel=r"$\operatorname{Im}q=-v$",title="Velocity plane")
bx.set_aspect("equal");bx.spines[["top","right"]].set_visible(False)
fig.suptitle("A horizontal lip gives a one-half canal contraction",fontsize=14)
fig.tight_layout();fig.savefig("2008-canal-flow.png",dpi=150,facecolor="white")
