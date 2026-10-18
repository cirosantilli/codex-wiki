from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False, "figure.facecolor": "white", "savefig.facecolor": "white"})
fig=plt.figure(figsize=(10,6.2),layout="constrained")
gs=fig.add_gridspec(2,2)
t=np.linspace(-3,3,3500)
for j,sgn in enumerate([1,-1]):
 ax=fig.add_subplot(gs[j,0]);env=np.exp(-t*t/3)
 ax.plot(t,env*np.cos(22*t+sgn*2*t*t),lw=1,color=["#175c9e","#bd492e"][j])
 ax.plot(t,env,"--",color="0.6",lw=.8);ax.plot(t,-env,"--",color="0.6",lw=.8)
 ax.set(xlabel="Time (arbitrary units)",ylabel="Electric field",title=(r"Positive $\eta$: frequency increases" if sgn==1 else r"Negative $\eta$: frequency decreases"),xlim=(-3,3),ylim=(-1.12,1.12))
 ax.set_yticks([-1,0,1])
ax=fig.add_subplot(gs[:,1])
for lo,hi,col in [(-4,-1.025,"#bd492e"),(-.975,0,"#8d57a4"),(0,4,"#175c9e")]:
 u=np.linspace(lo,hi,1000);ax.plot(u,1/(1+u),color=col,lw=2)
ax.axvline(-1,color="0.45",ls="--",lw=1);ax.axhline(0,color="0.5",lw=.8)
ax.axhline(1,color="0.65",ls=":",lw=.8);ax.plot(0,1,"ko",ms=4)
ax.text(-3.75,-1.5,"Backward focus");ax.text(-.52,2.8,"Forward, superluminal",rotation=70,fontsize=9,ha="center",va="center")
ax.text(1.05,.85,"Forward, subluminal",fontsize=10)
ax.set(xlabel=r"$u=2\eta c/\beta$ ($\beta>0$)",ylabel=r"$v_f/c=1/(1+u)$",title="Flying-focus velocity",xlim=(-4,4),ylim=(-5,5))
ax.text(-.93,-4.7,"Simultaneous focusing",rotation=90,fontsize=9)

fig.savefig(Path.cwd() / Path(__file__).with_suffix(".png").name, dpi=120, facecolor="white", transparent=False)
plt.close(fig)
