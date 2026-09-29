"""Python 3.14; NumPy and Matplotlib in ../pyproject.toml. PNG output in CWD."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
a=np.pi/(np.pi+2)
theta=np.linspace(-np.pi/2,-.00001,1000)
x=-2*a/np.pi*(np.log(np.abs(np.tan(theta/2)))+np.cos(theta))
y=1-2*a/np.pi*(1+np.sin(theta))
fig,axs=plt.subplots(1,3,figsize=(11,3.7),facecolor="white")
ax=axs[0]
ax.fill_between(x,0,y,color="C0",alpha=.13)
ax.fill_between([-1.1,0],[0,0],[2,2],color="C0",alpha=.13)
ax.plot(x,y,color="C0",lw=2)
ax.plot([-1.1,3.1],[0,0],color="black",lw=2)
ax.plot([0,0],[1,2],color="black",lw=2)
ax.axhline(a,color=".55",ls=":",lw=1)
ax.text(1.7,a+.16,r"$y=a$")
ax.text(.05,1.08,"D");ax.text(-.22,1.8,"E");ax.text(-1,.07,"A");ax.text(2.85,.06,"B");ax.text(2.85,a+.11,"C")
ax.set(xlim=(-1.1,3.1),ylim=(-.1,2),xlabel="x",ylabel="y",title="Physical plane")
ax=axs[1]
ax.fill_between([-2,2],0,a,color="C0",alpha=.13)
ax.plot([-2,2],[0,0],color="black",lw=2)
ax.plot([-2,0],[a,a],color="black",lw=2)
ax.plot([0,2],[a,a],color="C0",lw=2)
ax.text(.03,a+.04,"D");ax.text(-1.9,.06,"A");ax.text(-1.9,a+.04,"E");ax.text(1.8,.06,"B");ax.text(1.8,a+.04,"C")
ax.text(-.6,.29,r"$0<\psi<a$")
ax.set(xlim=(-2,2),ylim=(-.1,1.1),xlabel=r"$\phi$",ylabel=r"$\psi$",title="Potential strip")
ax=axs[2]
t=np.linspace(0,np.pi/2,400)
ax.fill(np.r_[0,np.cos(t),0],np.r_[0,np.sin(t),0],color="C0",alpha=.13)
ax.plot(np.cos(t),np.sin(t),color="C0",lw=2)
ax.plot([0,1],[0,0],color="black",lw=2);ax.plot([0,0],[0,1],color="black",lw=2)
ax.text(.03,.03,"A,E");ax.text(1.01,-.05,"B,C");ax.text(.02,1.02,"D")
ax.set(xlim=(-.1,1.2),ylim=(-.1,1.2),xlabel=r"$\mathrm{Re}\,q$",ylabel=r"$\mathrm{Im}\,q$",title="Velocity quarter disk")
ax.set_aspect("equal")
for ax in axs:ax.spines[["top","right"]].set_visible(False)
fig.tight_layout();fig.savefig("2009-draining-flow.png",dpi=150,facecolor="white")
