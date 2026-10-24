"""Generate PNG in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(12,4),facecolor="white",layout="constrained")
def arrow(ax,a,b,color="#12679b"):
 ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",color=color,lw=1.8))
h=lambda x:x**3/3-x
for ax,lam in zip(axs[:2],[.5,1.5]):
 x=np.linspace(-2.35,2.35,600)
 ax.plot(x,h(x),color="0.5",lw=1)
 mid=np.linspace(-1,1,200);ax.plot(mid,h(mid),"--",color="#b23c41",lw=2)
 for lo,hi in[(-2.2,-1),(1,2.2)]:
  xx=np.linspace(lo,hi,150);ax.plot(xx,h(xx),color="#12679b",lw=2)
 for y in[-1.15,0,1.15]:
  for a in[-2.05,-.5,.5,2.05]:
   v=y-h(a);arrow(ax,(a,y),(a+.25*np.sign(v),y),"#9ca5ad")
 ax.set(xlim=(-2.5,2.5),ylim=(-1.5,1.5),xlabel="$x$",ylabel="$y$",title=fr"$\lambda={lam}$: fast and slow motion")
 ax.grid(alpha=.15)
for x0,x1 in[(-1.8,-1.5),(-1.35,-1.12),(1.8,1.5),(1.35,1.12)]:
 arrow(axs[0],(x0,h(x0)),(x1,h(x1)))
arrow(axs[0],(-1,2/3),(2,2/3),"#c05a16")
arrow(axs[0],(1,-2/3),(-2,-2/3),"#c05a16")
axs[0].scatter([.5],[h(.5)],facecolor="white",edgecolor="#b23c41",zorder=5)
axs[1].scatter([1.5],[h(1.5)],color="#12679b",zorder=5)
for a,b in[(-1.8,-1.3),(1.05,1.35),(2.1,1.8)]:
 arrow(axs[1],(a,h(a)),(b,h(b)))
arrow(axs[1],(-1,2/3),(2,2/3),"#c05a16")
axs[1].text(.1,-.25,"Stable\n equilibrium",fontsize=9)
def times(x):
 q=(x*x-1)/(.5-x)
 return np.r_[0,np.cumsum((q[:-1]+q[1:])/2*np.diff(x))]
xl=np.linspace(-2,-1,1000);xr=np.linspace(2,1,1000)
tl=times(xl);tr=times(xr);period=tl[-1]+tr[-1]
for j in range(2):
 base=j*period
 axs[2].plot(tl+base,xl,color="#12679b",lw=2)
 axs[2].plot(tr+tl[-1]+base,xr,color="#12679b",lw=2)
 axs[2].plot([base+tl[-1]]*2,[-1,2],color="#c05a16",lw=1.5)
 axs[2].plot([base+period]*2,[1,-2],color="#c05a16",lw=1.5)
axs[2].set(xlabel="$t/k$",ylabel="$x$",title=r"$\lambda=1/2$: leading time trace",ylim=(-2.3,2.3))
axs[2].grid(alpha=.15)
fig.savefig("2007-relaxation-orbit.png",dpi=160,facecolor="white")
