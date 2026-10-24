"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. PNG output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
eps, target, n = .06, -1.5, 7000
def integrate(terminal, keep=False):
 y,p=0.,terminal
 h=-1/n
 ys,ps=[y],[p]
 def rhs(y,p):return p,(p-np.exp(np.clip(y,-700,30)))/eps
 for _ in range(n):
  a,b=rhs(y,p);c,d=rhs(y+h*a/2,p+h*b/2);e,f=rhs(y+h*c/2,p+h*d/2);g,j=rhs(y+h*e,p+h*f)
  y+=h*(a+2*c+2*e+g)/6;p+=h*(b+2*d+2*f+j)/6
  if keep:ys.append(y);ps.append(p)
 return (np.array(ys[::-1]),np.array(ps[::-1])) if keep else y
lo,hi=0.,100.
for _ in range(48):
 mid=(lo+hi)/2
 if integrate(mid)>target:lo=mid
 else:hi=mid
ys,ps=integrate((lo+hi)/2,True)
fig,axes=plt.subplots(1,2,figsize=(10,4.5),facecolor="white")
for ax,ylim in zip(axes,[(-2,28),(-.2,1.5)]):
 y=np.linspace(-1.85,.2,19);p=np.linspace(*ylim,21);yy,pp=np.meshgrid(y,p)
 dy=pp;dp=(pp-np.exp(yy))/eps
 norm=np.sqrt((dy/2.05)**2+(dp/(ylim[1]-ylim[0]))**2)+1e-15
 ax.quiver(yy,pp,dy/norm,dp/norm,color=".78",angles="xy",scale_units="xy",scale=20,width=.0025)
 t=np.linspace(-1.85,.2,400)
 ax.plot(t,np.exp(t),"--",color="C1",label=r"$p=e^y$")
 ax.plot(ys,ps,color="C0",lw=2.2,label="Boundary-value trajectory")
 ax.axhline(0,color=".4",lw=.7)
 ax.set(xlim=(-1.85,.2),ylim=ylim,xlabel=r"$y$",ylabel=r"$p=y'$")
 ax.spines[["top","right"]].set_visible(False)
axes[0].set_title("Terminal departure into a fast layer")
axes[1].set_title("Slow portion near the nullcline")
axes[0].scatter([ys[0],ys[-1]],[ps[0],ps[-1]],color="C0",s=22)
axes[0].text(-1.55,2,"Start: y=A");axes[0].text(-.55,25,"End: y=0")
axes[1].legend(frameon=False,fontsize=9)
fig.suptitle(r"Exponential reaction: $y'=p,\quad \epsilon p'=p-e^y$",y=1.01)
fig.tight_layout();fig.savefig("2009-nonlinear-phase.png",dpi=150,facecolor="white",bbox_inches="tight")
