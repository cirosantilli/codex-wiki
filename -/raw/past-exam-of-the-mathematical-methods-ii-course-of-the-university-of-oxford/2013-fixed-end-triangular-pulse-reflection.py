from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":12,"axes.titlesize":14,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white","savefig.transparent":False})

fig,axs=plt.subplots(1,3,figsize=(10.6,3.8),layout="constrained",sharey=True)
x=np.linspace(-2.1,0,1000)
def tri(s):return np.maximum(0,1-np.abs(s+1))
for ax,tau in zip(axs,[.5,.75,1.]):
 inc=tri(x-tau);ref=-tri(-x-tau);total=inc+ref
 ax.plot(x,inc,color="#35789a",ls=":",lw=1.8,label="Incident");ax.plot(x,ref,color="#b56b2e",ls="--",lw=1.8,label="Reflected");ax.plot(x,total,color="#75549a",lw=2.7,label="Total")
 ax.axvline(0,color="#555555",lw=3);ax.axhline(0,color="gray",lw=.5);ax.set(xlabel="x/b",title=f"cₛt/b = {tau:g}",xlim=(-2.1,.03),ylim=(-1.1,1.2));ax.grid(alpha=.12)
axs[0].set_ylabel("Displacement / a");axs[0].legend(fontsize=9,loc="lower left");axs[2].text(-1.9,.85,"Flat at this instant;\nvelocity remains nonzero",fontsize=10)
fig.suptitle("Fixed-end reflection reverses the pulse's displacement sign",fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix(".png").name,dpi=120)
plt.close(fig)
