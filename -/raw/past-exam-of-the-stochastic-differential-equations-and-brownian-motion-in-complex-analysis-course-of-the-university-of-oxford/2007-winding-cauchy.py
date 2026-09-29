"""Generate PNG in CWD; Python 3.14, NumPy, Matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(11,3.8),facecolor="white",layout="constrained")
t=np.linspace(0,1,1000);theta=4*np.pi*t+.4*np.sin(3*np.pi*t)
b=(1-t)*(1+.15*np.sin(10*np.pi*t));z=np.exp(-b+1j*theta)
ax=axs[0]
a=np.linspace(0,2*np.pi,500);ax.plot(np.cos(a),np.sin(a),color="0.5",lw=1)
ax.plot(z.real,z.imag,color="#12679b",lw=1.8)
ax.scatter([z.real[0],1],[z.imag[0],0],color=["#197c4d","#b23c41"],s=30,zorder=5)
ax.text(.15,-1.25,r"Exit angle modulo $2\pi$: 0",ha="center",fontsize=9)
ax.set(xlim=(-1.15,1.15),ylim=(-1.4,1.2),aspect="equal",xlabel=r"$\Re Z$",ylabel=r"$\Im Z$",title="A schematic lifted path")
ax=axs[1];ax.plot(theta,b,color="#12679b",lw=1.8);ax.axhline(0,color="0.5",lw=1)
ax.scatter([0,4*np.pi],[1,0],color=["#197c4d","#b23c41"],s=30,zorder=5)
ax.set(xlabel=r"Accumulated angle $\theta$",ylabel=r"$-\log|Z|$",ylim=(-.12,1.15),title="Continuous logarithmic lift",xticks=[0,2*np.pi,4*np.pi],xticklabels=["0",r"$2\pi$",r"$4\pi$"])
ax.text(6,.9,"Two full turns are retained",ha="center",fontsize=9)
ax=axs[2];s=np.linspace(-10,10,1001);ax.plot(s,1/(np.pi*(1+s*s)),color="#12679b",lw=2)
ax.fill_between(s,0,1/(np.pi*(1+s*s)),where=np.abs(s)>3,color="#f2bc8f")
ax.set(xlabel="Exit winding angle",ylabel="Probability density",title=r"Exact exit law when $|Z_0|=e^{-1}$")
ax.text(-9,.26,r"$f(\theta)=1/[\pi(1+\theta^2)]$",fontsize=9)
ax.text(4,.12,r"$\mathbb{E}|\theta|=\infty$",ha="center",fontsize=12)
for ax in axs[1:]:ax.grid(alpha=.15)
fig.savefig("2007-winding-cauchy.png",dpi=160,facecolor="white")
